from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
    """Deploy simple storage"""
    account = get_account()
    smpl_strg = SimpleStorage.deploy({"from": account})
    fav_number = smpl_strg.getFavoriteNumber()
    print(fav_number)

    transaction = smpl_strg.storeFavoriteNumber(15, {"from": account})
    transaction.wait(1)
    fav_number = smpl_strg.getFavoriteNumber()
    print(fav_number)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()