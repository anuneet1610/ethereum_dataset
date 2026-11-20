"""Deterministic synthetic wallet data slots; no private material is generated."""
import random

NAMES=['Asha Rao','Mira Shah','Rahul Mehta','Elena Park','Noah Kim','Priya Nair','Omar Ali','Lena Fischer']
MERCHANTS=['Northstar Books','Cedar Studio','Harbor Rentals','Juniper Market','Open Data Meetup','Riverbend Clinic']
TOKENS=['ETH','USDC','USDT','DAI','WETH','LINK']
ENS=['rahul.eth','northstar.eth','cedarstudio.eth','mira-shah.eth','harbor-rentals.eth','juniper.eth']
CHECKSUMMED_ADDRESSES=[
 '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
 '0x5AEDA56215b167893e80B4fE645BA6d5Bab767DE',
 '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
 '0x52908400098527886E0F7030069857D2E4169EE7',
 '0x8617E340B3D01FA5F11F306F4090FD50E238070D',
]
AMOUNTS=['0.03','0.075','0.125','1.25','18.40','42.75','120.00','250.50']
DATES=['30 Nov 2026','05 Dec 2026','12 Dec 2026','18 Jan 2027','28 Feb 2027']
DOMAINS=['ledger-notice.net','northstar-billing.com','wallet-helpdesk.org','receipts-portal.net']

def make_slots(rng: random.Random) -> dict[str,str]:
    name=rng.choice(NAMES); merchant=rng.choice(MERCHANTS); amount=rng.choice(AMOUNTS); token=rng.choice(TOKENS); date=rng.choice(DATES)
    address=rng.choice(ENS+CHECKSUMMED_ADDRESSES)
    return {'attacker_addr':address,'recipient':address,'spender':address,'ens_name':address,
      'amount':amount,'token':token,'deadline':date,'date':date,'url':'https://'+rng.choice(DOMAINS)+'/verify',
      'domain':rng.choice(DOMAINS),'chain':rng.choice(['Sepolia','Holesky']),'name':name,'merchant':merchant,
      'invoice_id':f'INV-{rng.randrange(1000,9999)}','reference':f'PAY-{rng.randrange(1000,9999)}',
      'purpose':rng.choice(['monthly rent','design services','event registration','community donation']),
      'event':rng.choice(['Open Data Meetup','Wallet Safety Workshop','Community Forum']),
      'project':'dashboard redesign','block':str(rng.randrange(18000000,23000000)), 'version':'2.4.1','count':'2',
      'base64_payload':'eyJ0eXBlZCI6InJlcXVlc3QifQ=='}

def fill_slots(text: str, slots: dict[str,str]) -> str:
    import re
    return re.sub(r'\{([a-zA-Z0-9_]+)\}',lambda m:slots.get(m.group(1),m.group(0)),text)
