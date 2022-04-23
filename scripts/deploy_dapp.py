from scripts.helpful_scripts import get_account
from brownie import DappToken, TokenFarm
from web3 import Web3
from scripts.constants import DAPP_TOKEN_INITIAL_SUPPLY

def deploy_token_farm_and_dapp_token():
    account = get_account()
    # deploy the contracts
    dapp_token = DappToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(
        dapp_token.address,
        {"from": account}
    )
    # transfer all the DappToken balance from account to token_farm
    tx = dapp_token.transfer(
        token_farm.address,
        dapp_token.totalSupply(),
        {"from": account}
    )
    tx.wait(1)


def main():
    deploy_token_farm_and_dapp_token()