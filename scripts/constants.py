from web3 import Web3
from brownie import (
    MockV3Aggregator,
    MockDAI,
    MockWETH,
)

DAPP_TOKEN_INITIAL_SUPPLY = Web3.toWei(10000000, "ether")

INITIAL_PRICE_FEED_VALUE = 2000000000000000000000
DECIMALS = 18

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]

contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "dai_usd_price_feed": MockV3Aggregator,
    "fau_token": MockDAI,
    "weth_token": MockWETH,
}
