"""Deterministic wallet and Ethereum prose templates."""
import random
from .slots import make_slots, fill_slots

TOPICS=[
('Gas and fees','Gas measures the computation required by a transaction. Review the estimated fee and network before confirming.'),
('Nonce ordering','A wallet nonce orders transactions from one account. Pending transactions may delay later requests.'),
('ERC-20 transfers','An ERC-20 transfer names a token, recipient, and amount. Check decimals and destination before sending.'),
('EIP-712 signing','EIP-712 presents structured data for signing. Review the domain, chain, message, spender, amount, and expiry.'),
('ENS resolution','An ENS name resolves to an address. Confirm the resolved recipient before sending ETH or tokens.'),
('Sepolia testnet','Sepolia is an Ethereum test network for learning and application testing; test tokens have no market value.'),
('Holesky testnet','Holesky supports Ethereum infrastructure tests. Confirm that the wallet is connected to the intended test network.'),
('Wallet safety','Keep recovery words private and compare recipient and amount on the wallet confirmation screen.'),
('Explorer status','A block explorer shows transaction hash, sender, recipient, value, block, timestamp, and status.'),
('Governance post','The proposal closes on the posted date. An off-chain vote signature records a choice and does not transfer funds.'),
('Token README','Before transferring a token, inspect its symbol, decimals, recipient, and displayed amount.'),
('Wallet changelog','The latest release clarifies transaction history and displays typed-data fields before a signature.'),
]
TEMPLATES=[]
for title,body in TOPICS:
    TEMPLATES.extend([(title+' / overview',body),(title+' / note',body+' Keep a copy of the transaction reference for your records.'),
      (title+' / guide','For '+title.lower()+', '+body[0].lower()+body[1:]),(title+' / reminder',body+' Verify the network shown by the wallet.'),
      (title+' / reference','Documentation: '+body+' The wallet displays the details before confirmation.')])
def generate(rng: random.Random,index: int):
    title,body=TEMPLATES[index%len(TEMPLATES)]
    from .slots import fill_slots, make_slots
    tail=' Reference {invoice_id} from {merchant} is dated {date}. Example amount: {amount} {token}; verify recipient {recipient}.'
    return f'crypto-{index%len(TEMPLATES):03d}',fill_slots(body+tail,make_slots(rng))
