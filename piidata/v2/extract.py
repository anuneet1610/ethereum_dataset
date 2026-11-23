"""Turn Markdown/MDX/reStructuredText/AsciiDoc docs into the plain text a page extractor
would return, then into segments with the shared sentence splitter.

The goal is parity with run time: a rendered docs page reaches the classifier as reflowed
paragraphs, one line per heading/list item/table row, without markup or code blocks.
"""
import re

from ..segmenter import split_segments

_FRONT = re.compile(r'\A---\s*\n(.*?)\n---\s*\n', re.S)
_FENCE = re.compile(r'(?ms)^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*$')
_HTML_COMMENT = re.compile(r'<!--.*?-->', re.S)
_SCRIPT = re.compile(r'<(script|style)\b.*?</\1>', re.S | re.I)
_LIQUID_VAR = re.compile(r'\{%-?\s*data\s+variables\.product\.(prodname_dotcom|company_short|prodname_github)[^%]*%\}')
_TEMPLATE = re.compile(r'\{%.*?%\}|\{\{[<%].*?[>%]\}\}|\{\{.*?\}\}', re.S)
_IMAGE = re.compile(r'!\[[^\]]*\]\([^)]*\)')
_LINK = re.compile(r'\[([^\]]+)\]\((?:[^()]|\([^)]*\))*\)')
_REFLINK = re.compile(r'\[([^\]]+)\]\[[^\]]*\]')
_ANCHOR = re.compile(r'\s*\{\s*#[^}]*\}')
_TOOLTIP = re.compile(r'\{\{<\s*glossary_tooltip[^>]*?text="([^"]+)"[^>]*>\}\}')
_TAG = re.compile(r'</?[A-Za-z][^<>]*?/?>')
_RST_ROLE = re.compile(r':[a-z:]+:`([^`<]*?)(?:\s*<[^>]*>)?`')
_INLINE_CODE = re.compile(r'`{1,2}([^`]+)`{1,2}')
_EMPH = re.compile(r'(\*\*|__)(.+?)\1|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])')
_LIST = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+')
_HEADING = re.compile(r'^\s*#{1,6}\s+')
_ADMONITION = re.compile(r'^\s*(?::::+|!!!|\?\?\?\+?|>\s*\[!\w+\]|\.\.\s+\w[\w-]*::|\[!\w+\])')
_TABLE_SEP = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$')
_MDX_LINE = re.compile(r'^\s*(import\s.+from\s|export\s|<\w+[^>]*\/>\s*$)')
_RST_UNDERLINE = re.compile(r'^\s*([=\-~^"`*+#])\1{2,}\s*$')
_ADOC_ATTR = re.compile(r'^\s*(:[\w-]+:|\[[\w.,=\s"-]*\]\s*$|----+\s*$|\.\.\.\.+\s*$|ifdef::|endif::|include::)')


def _front_matter(text):
    m = _FRONT.match(text)
    if not m:
        return '', text
    keep = []
    for line in m.group(1).splitlines():
        km = re.match(r'^(title|description|intro|summary):\s*(.+)$', line.strip())
        if km:
            value = km.group(2).strip().strip('"\'')
            if value and '{%' not in value:
                keep.append(value)
    return '\n\n'.join(keep), text[m.end():]


def to_plain_text(raw):
    head, body = _front_matter(raw.replace('\r\n', '\n'))
    body = _FENCE.sub('\n', body)
    body = _HTML_COMMENT.sub('', body)
    body = _SCRIPT.sub('', body)
    body = _LIQUID_VAR.sub('GitHub', body)
    body = _TOOLTIP.sub(r'\1', body)
    body = _TEMPLATE.sub('', body)
    body = body.replace('AUTOTITLE', 'the linked article')
    lines = []
    in_indented_code = False
    for line in body.split('\n'):
        if _MDX_LINE.match(line) or _ADMONITION.match(line) or _TABLE_SEP.match(line) \
                or _RST_UNDERLINE.match(line) or _ADOC_ATTR.match(line):
            lines.append(''); continue
        # Indented code (4+ spaces after a blank line, not a list continuation).
        if re.match(r'^( {4,}|\t)\S', line) and (not lines or lines[-1] == '' or in_indented_code) \
                and not _LIST.match(line.strip() and line or 'x'):
            in_indented_code = True; continue
        in_indented_code = False
        line = re.sub(r'^\s*>\s?', '', line)          # blockquote marker
        if line.strip().startswith('|') and line.strip().endswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            line = ' '.join(c for c in cells if c)   # one table row per line
            lines.append('\n' + line + '\n'); continue
        lines.append(line)
    text = '\n'.join(lines)
    text = _IMAGE.sub('', text)
    text = _LINK.sub(r'\1', text)
    text = _REFLINK.sub(r'\1', text)
    text = _ANCHOR.sub('', text)
    text = _TAG.sub('', text)
    text = _RST_ROLE.sub(r'\1', text)
    text = _INLINE_CODE.sub(r'\1', text)
    text = _EMPH.sub(lambda m: m.group(2) or m.group(3) or '', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    # Reflow: blank lines separate blocks; headings and list items are their own lines.
    out = []
    for block in re.split(r'\n\s*\n', text):
        items = []
        for line in block.split('\n'):
            s = line.strip()
            if not s:
                continue
            if _HEADING.match(s) or _LIST.match(s) or not items:
                items.append(_LIST.sub('', _HEADING.sub('', s)))
            else:
                items[-1] += ' ' + s
        out.extend(items)
    return (head + '\n\n' if head else '') + '\n'.join(out)


_REVIEW = re.compile(r'\b(LLMs?|GPT|ChatGPT|Copilot|Claude|Gemini|language models?|prompt injection|system prompt|'
                     r'prompt engineering|jailbreak\w*|AI (?:assistant|agent|model)s?|agentic|MCP)\b', re.I)
_CODEY = re.compile(r'[{}();=<>$\\]|=>|::|\w\(\)')


def keep_sentence(s):
    """Return (keep, reason). Drops fragments, code, and leftover template syntax."""
    words = s.split()
    if len(words) < 4: return False, 'short'
    if len(words) > 70: return False, 'long'
    letters = sum(c.isalpha() for c in s); visible = sum(not c.isspace() for c in s)
    if visible == 0 or letters / visible < 0.65: return False, 'non_alpha'
    if len(_CODEY.findall(s)) > max(2, len(words) // 6): return False, 'code'
    if '{%' in s or '{{' in s or '%}' in s: return False, 'template'
    if not re.search(r'[a-z]{3,}', s): return False, 'no_words'
    if s.rstrip().endswith(':') and len(words) < 6: return False, 'label'
    return True, ''


def needs_review(s):
    return bool(_REVIEW.search(s))


def doc_segments(raw):
    """Plain text -> list of segment strings that pass keep_sentence()."""
    text = to_plain_text(raw)
    out = []
    for seg in split_segments(text):
        ok, _ = keep_sentence(seg.text)
        if ok:
            out.append(seg.text)
    return out
