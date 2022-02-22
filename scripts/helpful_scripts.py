
from brownie import network, config, accounts, FundMe, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]

DECIMALS =8
STARTING_PRICE = 200000000000

# Checking is the the network is on a local blockchain - Development one 
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        print('ESTA TRATANDO DE LEER LA CUENTA')
        return accounts[0]

    else:
        return  accounts.add(config["wallets"]["from_key"])


def deploy_mocks():

    print ('DEPLOYING MOCKS')
    # print ('Deploying Mocks ;;;')
        #Vamos hacer deploy una sola vez
    if len(MockV3Aggregator)<=0:
            print('antes del deployed')
        # Estamos utilizando el contrato y pasando los valores al contructor .. 18,2000 mas los 18 ceros 
            MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE,{"from":get_account()})
            print ('LISTO DEPLOYED')
        # Nos traemos la direccion del Mock deployed para our price_feed 
  