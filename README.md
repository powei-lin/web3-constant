# web3-constant

### Install
```
pip install web3-constant
```

### Connect to Web3
``` py3
from web3 import Web3
from web3constant.Fantom.Url import FTM_RPC

w3 = Web3(Web3.HTTPProvider(FTM_RPC))
if w3.isConnected():
    print("Web3 is connected.")
```

### Listen to a topic
``` py3
from web3 import Web3
from web3constant.Fantom.Url import FTM_RPC
from web3constant.topics import PAIR_SYNC

w3 = Web3(Web3.HTTPProvider(FTM_RPC))

prev_block_num = w3.eth.get_block_number()
while(True):
    current_block = w3.eth.get_block_number()
    if (prev_block_num == current_block):
        continue

    topic_d = {
        'fromBlock': prev_block_num,
        'topics': [PAIR_SYNC]
    }
    logs = w3.eth.get_logs(topic_d)
    for l in logs:
      print(l)
```


### Create contract
``` py3
from web3 import Web3
from web3constant.Fantom.Url import FTM_RPC
from web3constant.Fantom.Dex import SPOOKY_SWAP_FACTORY_ADDRESS
from web3abi.UniswapV2 import SPOOKY_SWAP_FACTORY_ABI, UNISWAP_V2_PAIR_ABI

w3 = Web3(Web3.HTTPProvider(FTM_RPC))

# create factory contract
spooky_swap_factory_contract = w3.eth.contract(
    address=SPOOKY_SWAP_FACTORY_ADDRESS, abi=SPOOKY_SWAP_FACTORY_ABI
)

# get pair address for factory contract
pair_address = spooky_swap_factory_contract.functions.allPairs(0).call()
print("pair contract address:", pair_address)

# create pair contract
pair_contract = w3.eth.contract(address=pair_address, abi=UNISWAP_V2_PAIR_ABI)

# get token0, token1
token0 = pair_contract.functions.token0().call()
token1 = pair_contract.functions.token1().call()

# get reserves
r0, r1, timestamp = pair_contract.functions.getReserves().call()

# print
print("token0:", token0)
print("token0 reserves:", r0)
print("token1:", token1)
print("token1 reserves:", r1)
print("sync timestamp:", timestamp)
```
