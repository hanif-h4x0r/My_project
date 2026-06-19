from web3 import Web3
import os

RPC_URL = "https://rpc-ubusuna.xeneascan.com/"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

account = w3.eth.account.from_key(PRIVATE_KEY)
sender = account.address

receiver = "0xAlamatTujuan"

amount = w3.to_wei(0.1, "ether")  # 0.1 TXENE

nonce = w3.eth.get_transaction_count(sender)

tx = {
    "chainId": 1096,
    "nonce": nonce,
    "to": receiver,
    "value": amount,
    "gas": 21000,
    "gasPrice": w3.eth.gas_price,
}

signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)

tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("TX Hash:", tx_hash.hex())
