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
