"""Dependency-light sentence segmenter shared by build and inference."""
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Segment:
    start: int
    end: int
    text: str


_BOUNDARY = re.compile(
    r"(?<=[.!?])(?:[\"'”’)]*)[ \t]+(?=[A-Z0-9\[{<#>*_])|\n+|(?<=;)\s+(?=[A-Z])"
)
_ABBREV = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|vs|e\.g|i\.e|No|St)\.$", re.I)
_DECIMAL = re.compile(r"^\d+$")


def split_segments(text: str) -> list[Segment]:
    """Split extracted text while protecting common abbreviations and decimals."""
    if not text:
        return []
    spans=[]; start=0
    for m in _BOUNDARY.finditer(text):
        end=m.start()
        left=text[start:end].rstrip()
        if not left:
            start=m.end(); continue
        # Do not split after an abbreviation, decimal point, URL/domain, ENS name,
        # or hexadecimal address.  URL punctuation is handled by checking token.
        token=left.split()[-1]
        if _ABBREV.search(left) or (token.endswith('.') and _DECIMAL.fullmatch(token[:-1])):
            continue
        spans.append((start, end))
        start=m.end()
    if start < len(text): spans.append((start,len(text)))
    out=[]
    for a,b in spans:
        while a<b and text[a].isspace(): a+=1
        while b>a and text[b-1].isspace(): b-=1
        if a<b: out.append(Segment(a,b,text[a:b]))
    return out
