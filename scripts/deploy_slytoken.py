from brownie import SlyToken
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000, "ether")


def deploy_slytoken():
    account = get_account()
    sly_token = SlyToken.deploy({"from": account}, publish_source=True)
    tx = sly_token.mint(INITIAL_SUPPLY, {"from": account})
    tx.wait(1)
    print(f"Minted 1000 {sly_token.name()}")


def main():
    deploy_slytoken()
