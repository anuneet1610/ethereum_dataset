"""Carrier rendering and extractor-style flattening."""
import html, json, re

def render(text, carrier):
    if carrier=='visible_body': return text
    if carrier=='html_hidden': return f'<span style="display:none">{text}</span>'
    if carrier=='html_comment': return f'<!-- {text} -->'
    if carrier=='img_alt': return f'<img alt="{html.escape(text, quote=True)}">'
    if carrier=='pdf_footer_header': return f'--- PAGE FOOTER ---\n{text}'
    if carrier=='markdown_table_cell': return f'| note | {text} |'
    if carrier=='json_tool_response': return json.dumps({'note':text},ensure_ascii=False)
    if carrier=='email_quote': return '> '+text
    return text

def flatten(rendered, carrier):
    if carrier=='json_tool_response':
        try: return json.loads(rendered).get('note','')
        except Exception: return rendered
    if carrier=='img_alt':
        m=re.search(r'alt="(.*?)"',rendered); return html.unescape(m.group(1)) if m else rendered
    if carrier=='html_comment': return re.sub(r'<!--|-->','',rendered).strip()
    if carrier=='html_hidden': return re.sub(r'<[^>]+>','',rendered)
    if carrier=='pdf_footer_header': return rendered.split('\n',1)[-1]
    if carrier=='markdown_table_cell': return rendered.strip('| ').split('|',2)[1].strip()
    if carrier=='email_quote': return rendered[2:]
    return rendered

def render_document(base, injected, carrier, position):
    """Apply one identical carrier and whitespace layout to both pair members."""
    from .segmenter import split_segments
    parts=split_segments(base)
    at=0 if position=='head' else (len(parts)//2 if position=='middle' else len(parts))
    offset=parts[at].start if at<len(parts) else len(base)
    before,after=base[:offset],base[offset:]
    if injected:
        plain=before+'\n'+injected+'\n'+after
    else:
        # Reserve the same empty insertion slot in the clean mate. The
        # attack payload occupies the slot between these two line breaks.
        plain=before+'\n\n'+after
    if carrier=='visible_body': raw=plain
    elif carrier=='html_hidden': raw=f'<div style="display:none">{html.escape(plain)}</div>'
    elif carrier=='html_comment': raw=f'<!--{html.escape(plain)}-->'
    elif carrier=='img_alt': raw=f'<p>Attached receipt:</p><img src="receipt.png" alt="{html.escape(plain,quote=True)}"><p>Image extracted with surrounding document context.</p>'
    elif carrier=='pdf_footer_header': raw=f'--- PAGE FOOTER ---\n{plain}\n--- END FOOTER ---'
    elif carrier=='markdown_table_cell':
        cell=html.escape(plain).replace('|',r'\|').replace('\n','&#10;')
        raw='| Section | Details |\n|---|---|\n'+f'| Document | {cell} |'
    elif carrier=='json_tool_response': raw=json.dumps({'document':plain},ensure_ascii=False)
    elif carrier=='email_quote':
        quoted='\n'.join('> '+line for line in plain.splitlines())
        raw='\n'.join(['From: billing@merchant.net','Subject: Payment details',quoted])
    else: raw=plain
    # Flatten with extractor-like rules, preserving the common surrounding text.
    if carrier=='json_tool_response': extracted=json.loads(raw)['document']
    elif carrier=='markdown_table_cell':
        line=raw.splitlines()[2]
        content=re.split(r'(?<!\\)\|',line.strip().strip('|'),maxsplit=1)[1].strip()
        extracted=html.unescape(content.replace(r'\|','|').replace('&#10;','\n'))
    elif carrier=='html_comment': extracted=html.unescape(re.sub(r'<!--|-->','',raw))
    elif carrier=='html_hidden': extracted=html.unescape(re.sub(r'<[^>]+>','',raw))
    elif carrier=='img_alt':
        match=re.search(r'alt="(.*?)"',raw,re.S)
        body=html.unescape(match.group(1)) if match else ''
        extracted='\n'.join(('Attached receipt:',body,'Image extracted with surrounding document context.'))
    elif carrier=='pdf_footer_header': extracted=raw.split('\n',1)[1].rsplit('\n--- END FOOTER ---',1)[0]
    elif carrier=='email_quote': extracted=re.sub(r'(?m)^>\s?','',raw.split('\n',2)[2])
    else: extracted=raw
    start=extracted.find(injected) if injected else -1
    if injected and start<0: raise ValueError(f'Carrier {carrier} did not preserve inserted payload during flattening')
    return raw,extracted,start,(start+len(injected) if injected else -1)
