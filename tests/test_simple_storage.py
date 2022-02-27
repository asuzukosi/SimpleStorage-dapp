import pytest
from brownie import accounts, SimpleStorage


def test_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    value = simple_storage.getFavoriteNumber()
    assert value == 5


def test_update_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.storeFavoriteNumber(15, {"from": account})
    value = simple_storage.getFavoriteNumber()
    assert value == 15

