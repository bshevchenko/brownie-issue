from consts import *
from brownie import a, reverts, Contract
from brownie.test import given, strategy
import time


@given(
    amount_desired=strategy('uint', min_value=10000, max_value=INIT_ETH_BAL) # TODO
)
def test_deposit_random(auto, amount_desired, dai, uni_factory): # TODO random?

    dai.approve(auto.dn, amount_desired, auto.FR_WHALE)

    amount_min = 0
    amount_eth_min = 1
    auto.dn.deposit(DAI_ADDR, amount_desired, amount_min, amount_eth_min, time.time() * 2, {'value': 1 * E_18, 'from': auto.WHALE})

    assert dai.balanceOf(auto.dn) >= (amount_desired * 0.9)


def test_deposit_rev_unallowed(auto):
    with reverts('token not allowed'):
        auto.dn.deposit(WETH_ADDR, 0, 0, 0, 0, {'from': auto.DEPLOYER})
