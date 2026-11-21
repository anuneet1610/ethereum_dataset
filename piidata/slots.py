"""Deterministic synthetic wallet data slots; no private material is generated."""
import random
from eth_utils import keccak

NAMES=['Asha Rao','Mira Shah','Rahul Mehta','Elena Park','Noah Kim','Priya Nair','Omar Ali','Lena Fischer']
MERCHANTS=['Northstar Books','Cedar Studio','Harbor Rentals','Juniper Market','Open Data Meetup','Riverbend Clinic']
TOKENS=['ETH','USDC','USDT','DAI','WETH','LINK']
ENS=['rahul.eth','northstar.eth','cedarstudio.eth','mira-shah.eth','harbor-rentals.eth','juniper.eth']
AMOUNTS=['0.03','0.075','0.125','1.25','18.40','42.75','120.00','250.50']
DATES=['30 Nov 2026','05 Dec 2026','12 Dec 2026','18 Jan 2027','28 Feb 2027']
DOMAINS=['ledger-notice.net','northstar-billing.com','wallet-helpdesk.org','receipts-portal.net']

def make_slots(rng: random.Random) -> dict[str,str]:
    name=rng.choice(NAMES); merchant=rng.choice(MERCHANTS); amount=rng.choice(AMOUNTS); token=rng.choice(TOKENS); date=rng.choice(DATES)
    # Clean recipients and adversarial destinations share the same address
    # generator; the attacker slot is always a fresh EIP-55 checksum address.
    recipient=rng.choice(ENS) if rng.random()<0.35 else _fresh_checksum_address(rng)
    attacker=_fresh_checksum_address(rng)
    while attacker.lower()==recipient.lower(): attacker=_fresh_checksum_address(rng)
    return {'attacker_addr':attacker,'recipient':recipient,'spender':attacker,'ens_name':rng.choice(ENS),
      'amount':amount,'token':token,'deadline':date,'date':date,'url':'https://'+rng.choice(DOMAINS)+'/verify',
      'domain':rng.choice(DOMAINS),'chain':rng.choice(['Sepolia','Holesky']),'name':name,'merchant':merchant,
      'invoice_id':f'INV-{rng.randrange(1000,9999)}','reference':f'PAY-{rng.randrange(1000,9999)}',
      'payload_nonce':f'CASE-{rng.getrandbits(64):016x}',
      'purpose':rng.choice(['monthly rent','design services','event registration','community donation']),
      'event':rng.choice(['Open Data Meetup','Wallet Safety Workshop','Community Forum']),
      'project':'dashboard redesign','block':str(rng.randrange(18000000,23000000)), 'version':'2.4.1','count':'2',
      'base64_payload':''}

def _fresh_checksum_address(rng: random.Random) -> str:
    """Create a fresh EIP-55 address using the run's seeded random source."""
    lower=rng.randbytes(20).hex()
    hashed=keccak(text=lower).hex()
    return '0x'+''.join(c.upper() if c in 'abcdef' and int(hashed[i],16)>=8 else c
                        for i,c in enumerate(lower))

def fill_slots(text: str, slots: dict[str,str]) -> str:
    import re
    return re.sub(r'\{([a-zA-Z0-9_]+)\}',lambda m:slots.get(m.group(1),m.group(0)),text)
