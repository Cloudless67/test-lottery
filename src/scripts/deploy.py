from brownie import config, network, Lottery, LotteryToken, MockV3Aggregator
from scripts.utilities import get_account, deploy_mocks


def deploy_lottery():
    current_network = network.show_active()
    account = get_account()

    if current_network != "development":
        price_feed_address = config["networks"][current_network]["eth_usd_price,_feed"]

    else:
        price_feed_address = deploy_mocks()

    lottery = Lottery.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][current_network].get("verify"),
    )
    print(lottery)


def deploy_lottery_token():
    account = get_account()
    lottery_token = LotteryToken.deploy({"from": account})
    print(lottery_token)


def main():
    deploy_lottery()
    deploy_lottery_token()
