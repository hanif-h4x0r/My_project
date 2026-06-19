from web3 import Web3
import os
import time
from dotenv import load_dotenv

load_dotenv()

RPC_URL = "https://rpc-ubusuna.xeneascan.com/"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

account = w3.eth.account.from_key(PRIVATE_KEY)
sender = account.address

receiver = w3.to_checksum_address(
    "0x4acf6b261bec60873cece640f231162136f4b0dd"
)

amount = w3.to_wei(0.1, "ether")

base_nonce = w3.eth.get_transaction_count(sender)

for i in range(3):
    tx = {
        "chainId": w3.eth.chain_id,
        "nonce": base_nonce + i,
        "to": receiver,
        "value": amount,
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
    }

    signed_tx = w3.eth.account.sign_transaction(
        tx,
        private_key=PRIVATE_KEY
    )

    tx_hash = w3.eth.send_raw_transaction(
        signed_tx.raw_transaction
    )

    print(f"[{i+1}/3] TX Hash:", tx_hash.hex())

    if i < 2:  # tidak perlu delay setelah transaksi terakhir
        print("Menunggu 15 detik...")
        time.sleep(15)

print("Selesai.")
