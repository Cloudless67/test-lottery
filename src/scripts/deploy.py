from brownie import config, network, Lottery, MockV3Aggregator
from scripts.utilities import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT

LOTTERY_PRICE_IN_WEI = 2 * 10 ** 15
GAME_PERIOD = 7 * 24 * 60 * 60  # 1 week


def deploy_lottery():
    current_network = network.show_active()
    account = get_account()

    if current_network not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        vrf_coordinator = config["networks"][current_network]["vrf_coordinator"]
        link_token = config["networks"][current_network]["link_token"]
        key_hash = config["networks"][current_network]["key_hash"]
        fee = config["networks"][current_network]["fee"]

    else:
        # price_feed_address = deploy_mocks()
        pass

    lottery = Lottery.deploy(
        vrf_coordinator,
        link_token,
        key_hash,
        fee,
        LOTTERY_PRICE_IN_WEI,
        GAME_PERIOD,
        {"from": account},
        publish_source=config["networks"][current_network].get("verify"),
    )
    print(lottery)


def main():
    deploy_lottery()
