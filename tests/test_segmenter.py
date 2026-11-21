import unittest
from piidata.segmenter import split_segments

class SegmenterTests(unittest.TestCase):
    def test_decimals_urls_ens_and_abbreviations(self):
        text='Dr. Rao sent 0.05 ETH to https://wallet.example/path. Check rahul.eth. Done.'
        self.assertEqual([x.text for x in split_segments(text)],['Dr. Rao sent 0.05 ETH to https://wallet.example/path.','Check rahul.eth.','Done.'])
    def test_bullets_and_newlines(self):
        self.assertEqual(len(split_segments('- First item\n- Second item.')),2)
    def test_empty(self): self.assertEqual(split_segments(''),[])

if __name__=='__main__': unittest.main()
