from brownie import FoundMe , accounts
from scripts.helpful_scrips import get_account

def deploy_found_me():
    account = get_account()
    foundme = FoundMe.deploy({"from":account})
    print(" Contract deploy from " + foundme)

def main():
    pass