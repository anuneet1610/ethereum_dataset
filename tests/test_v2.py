import json, random, re, unittest
from pathlib import Path

from piidata.segmenter import split_segments
from piidata.v2.extract import to_plain_text, doc_segments, keep_sentence
from piidata.v2.generate import expand, clean_and_twin_rows, attack_rows, composed_attack_rows, template_split, prose_swap, is_imperative, v2_slots

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / 'data' / 'v2'


class ExtractTests(unittest.TestCase):
    def test_reflows_hard_wrapped_paragraphs(self):
        raw = 'This page shows how to set\nthe memory limit for a Pod.\n\nIt also covers CPU.'
        segs = [s.text for s in split_segments(to_plain_text(raw))]
        self.assertEqual(segs, ['This page shows how to set the memory limit for a Pod.', 'It also covers CPU.'])

    def test_strips_code_links_and_front_matter(self):
        raw = '---\ntitle: Sending tokens\nweight: 3\n---\nUse the [Send button](/send) to start.\n\n```bash\nrm -rf /\n```\n- First item here is long enough.'
        text = to_plain_text(raw)
        self.assertIn('Sending tokens', text)
        self.assertIn('Use the Send button to start.', text)
        self.assertNotIn('rm -rf', text)
        self.assertNotIn('weight', text)
        self.assertIn('First item here is long enough.', text.splitlines())

    def test_keep_sentence_filters(self):
        self.assertFalse(keep_sentence('Installation')[0])
        self.assertFalse(keep_sentence('const x = foo(); bar(x); baz({a: 1});')[0])
        self.assertTrue(keep_sentence('Review the network fee before you confirm the transfer.')[0])


class GenerateTests(unittest.TestCase):
    def test_expand_nested_alternations(self):
        rng = random.Random(0)
        for _ in range(20):
            out = expand('[[a|b [[c|d]]]] e', rng)
            self.assertIn(out, {'a e', 'b c e', 'b d e'})

    def _rows(self):
        gs = lambda g: template_split(g, 1729)
        return clean_and_twin_rows(1729, gs) + attack_rows(1729, gs) + composed_attack_rows(1729, gs)

    def test_rows_are_single_segments_and_pairs_share_split(self):
        rows = self._rows()
        self.assertGreater(len(rows), 1000)
        pair_split = {}
        for r in rows:
            self.assertEqual(len(split_segments(r['text'])), 1, r['text'])
            if r.get('pair_id'):
                self.assertEqual(pair_split.setdefault(r['pair_id'], r['split']), r['split'])

    def test_test_only_families_never_in_train(self):
        for r in self._rows():
            if r.get('family') in ('role_play', 'quoted_email'):
                self.assertEqual(r['split'], 'test')

    def test_prose_swap_is_agent_addressed_or_harmful(self):
        rng = random.Random(3)
        s = 'Run the migration script before deploying the new version.'
        self.assertTrue(is_imperative(s))
        for _ in range(20):
            t = prose_swap(s, rng, v2_slots(rng))
            self.assertRegex(t, re.compile(r'\b(AI|agent|agents|assistant|assistants)\b|0x[0-9a-fA-F]{40}|https://', re.I))


@unittest.skipUnless((V2 / 'train.jsonl').exists(), 'data/v2 not built')
class BuiltDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sets = {p.stem: [json.loads(l) for l in p.open(encoding='utf-8')] for p in V2.glob('*.jsonl')}

    def test_no_template_or_source_leakage(self):
        train = self.sets['train']
        tr_templates = {r['template_id'] for r in train if not r.get('origin_repo')}
        tr_repos = {r['origin_repo'] for r in train if r.get('origin_repo')}
        for name, rows in self.sets.items():
            if name == 'train': continue
            for r in rows:
                if r.get('origin_repo'):
                    self.assertNotIn(r['origin_repo'], tr_repos, (name, r['text']))
                elif r['source'] != 'v2_test_only_clean':
                    self.assertNotIn(r['template_id'], tr_templates, (name, r['text']))

    def test_no_exact_text_overlap_with_train(self):
        train = {r['text'] for r in self.sets['train']}
        for name, rows in self.sets.items():
            if name != 'train':
                self.assertFalse(train & {r['text'] for r in rows}, name)

    def test_escalation_family_held_out_of_train(self):
        pat = re.compile(r'unlimited|allowance|standing permission|never expires', re.I)
        self.assertFalse([r['text'] for r in self.sets['train'] if r['label'] == 1 and pat.search(r['text'])])


if __name__ == '__main__':
    unittest.main()
