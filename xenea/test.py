from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc-ubusuna.xeneascan.com/"))

print("Connected:", w3.is_connected())
print("Chain ID:", w3.eth.chain_id)
print("Gas Price:", w3.eth.gas_price)
