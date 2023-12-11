from brownie import FundMe , MockV3Aggregator , config , network
from scripts.helpful_scrips import get_account 

def deploy_found_me():
    if network.show_active() != "development":
        price_feed_address = "0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
    else:
        # * Price feed falso
        print("Deploy de Mocks")
        mock_agregator = MockV3Aggregator.deploy(8 , 200000000, {"from": get_account()})
        price_feed_address = mock_agregator.address
        print("Moks Deployed")
    
    account = get_account()
    found_me = FundMe.deploy(price_feed_address,
    {"from":account},
    publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deploy from ${found_me}")

def main():
    deploy_found_me()