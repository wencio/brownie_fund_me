from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from  web3 import Web3


def deploy_fund_me():
    account = get_account()


    #pass the price feed address to our fundme contract as a global variable 
    # if we are on a persistent network like rinkeby, use the associated address 
    #otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # Estoy importando la informacion del price feed de acuerdo al archivo config 
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]

        fund_me = FundMe.deploy(price_feed_address,{"from":get_account()},
            publish_source=config["networks"][network.show_active()].get("verify"),)
    else:
       deploy_mocks()
       price_feed_address = MockV3Aggregator[-1].address
             #print("Mocks Deployed...")
    # aga el deploy of the contract utilizando el mock y verifico para poder hacer el verify del contrato
    fund_me = FundMe.deploy(price_feed_address,{"from":get_account()},
    publish_source=config["networks"][network.show_active()].get("verify"),)
    return fund_me
    
def main():
    deploy_fund_me()