from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000


def get_account():
    # account = accounts[0]   # Local chain
    # account = accounts.load('kovan-test-account')   # most secure
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
        price_feed_address = MockV3Aggregator[-1].address
