from brownie import SimpleStorage, accounts, config

def read_contract():
    smpl_strg = SimpleStorage[-1]
    value = smpl_strg.getFavoriteNumber()
    print(value)

def main():
    read_contract()