from brownie import config, network, Lottery, MockV3Aggregator
from scripts.utilities import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT


def deploy_lottery():
    current_network = network.show_active()
    account = get_account()

    if current_network not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        vrf_coordinator = config["networks"][current_network]["vrf_coordinator"]
        link_token = config["networks"][current_network]["link_token"]
        key_hash = config["networks"][current_network]["key_hash"]
        fee = config["networks"][current_network]["fee"]
        lottery_price_in_wei = config["networks"][current_network][
            "lottery_price_in_wei"
        ]
        game_period = config["networks"][current_network]["game_period"]

    else:
        price_feed_address = deploy_mocks()

    lottery = Lottery.deploy(
        vrf_coordinator,
        link_token,
        key_hash,
        fee,
        lottery_price_in_wei,
        game_period,
        {"from": account},
        publish_source=config["networks"][current_network].get("verify"),
    )
    print(lottery)


def main():
    deploy_lottery()
