from brownie import FundMe, network
from scripts.helpful_scripts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print('estoy en function fund')
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    #print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from":account, "value":entrance_fee})

def withdraw():
    fund_me =FundMe[-1]
    account =get_account()
    fund_me.withdraw({"from":account})


def main():
    fund()
    withdraw()