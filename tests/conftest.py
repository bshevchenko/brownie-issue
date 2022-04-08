import pytest
from brownie import a, interface
from consts import *
from eth_abi import encode_abi
import time


# Test isolation
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


# Deploy the contracts for repeated tests without having to redeploy each time
def deploy_initial_AUTO_contracts(fuse, fuse_clones, master_price_oracle, delegator, fuse_lens, dai, weth):
    class Context:
        pass

    auto = Context()
    # It's a bit easier to not get mixed up with accounts if they're named
    # Can't define this in consts because a needs to be imported into the test
    auto.DEPLOYER = a[0]
    auto.FR_DEPLOYER = {"from": auto.DEPLOYER}
    auto.WHALE = a[2]
    auto.FR_WHALE = {"from": auto.WHALE}
    auto.CHARLIE = a[3]
    auto.FR_CHARLIE = {"from": auto.CHARLIE}
    auto.DENICE = a[4]
    auto.FR_DENICE = {"from": auto.DENICE}

    dai_whale = a.at('0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643', force=True)
    dai.transfer(auto.WHALE, INIT_ETH_BAL, {'from': dai_whale})
    assert dai.balanceOf(auto.WHALE) == INIT_ETH_BAL

    initializer_data = master_price_oracle.initialize.encode_input(
        [],
        [],
        FUSE_DEFAULT_ORACLE_ADDR,
        auto.DEPLOYER,
        True
    )
    clone_tx = fuse_clones.clone(FUSE_MASTER_PRICE_ORACLE_ADDR, initializer_data, auto.FR_DEPLOYER)
    oracle_addr = clone_tx.events['Deployed']['instance']

    fuse.deployPool(
        'Test0',
        COMPTROLLER_IMPL_ADDR,
        False,
        500000000000000000,
        1080000000000000000,
        oracle_addr,
        auto.FR_DEPLOYER
    )

    pools = fuse.getPoolsByAccount(auto.DEPLOYER)
    unitroller_addr = pools[1][0][2] # TODO

    unitroller_core = interface.IUnitrollerCore(unitroller_addr)
    unitroller_core._acceptAdmin(auto.FR_DEPLOYER)

    constructor_data = delegator.etherInitialize.encode_input(
        unitroller_addr,
        JUMP_RATE_MODEL_ADDR,
        'Test0 Ethereum',
        'fETH-185',
        CETHER_IMPLEMENTATION_ADDR,
        0x00,
        100000000000000000,
        0
    ).replace('0x3e2839ee', '0x') # TODO
    isCEther = True
    collateralFactorMantissa = 700000000000000000

    print("WTF13")
    print(constructor_data)

    comptroller = Contract.from_explorer(COMPTROLLER_IMPL_ADDR)
    unitroller = Contract.from_abi('Unitroller', unitroller_addr, comptroller.abi)
    tx = unitroller._deployMarket(isCEther, constructor_data, collateralFactorMantissa, auto.FR_DEPLOYER)

    assets = fuse_lens.getPoolAssetsWithData(unitroller_addr)

    assert assets == '0' # TODO assert by fuse_lens.getPoolAssetsWithData

    return auto


@pytest.fixture(scope="module")
def auto(fuse, fuse_clones, master_price_oracle, delegator, fuse_lens, dai, weth):
    return deploy_initial_AUTO_contracts(fuse, fuse_clones, master_price_oracle, delegator, fuse_lens, dai, weth)


@pytest.fixture(scope="module")
def uni_factory():
    return Contract.from_explorer(UNIV2_FACTORY_ADDR)


@pytest.fixture(scope="module")
def fuse():
    dir = Contract.from_explorer(FUSE_POOL_DIR_ADDR)
    return Contract.from_abi('AdminUpgradeabilityProxy', FUSE_POOL_DIR_PROXY_ADDR, dir.abi)


@pytest.fixture(scope="module")
def fuse_lens():
    return interface.IFusePoolLens(FUSE_POOL_LENS_ADDR)


@pytest.fixture(scope="module")
def fuse_clones():
    return Contract.from_explorer(FUSE_INITIALIZABLE_CLONES_ADDR)


@pytest.fixture(scope="module")
def master_price_oracle():
    return Contract.from_explorer(FUSE_MASTER_PRICE_ORACLE_ADDR)


@pytest.fixture(scope="module")
def delegator():
    return interface.ICDelegator(WETH_ADDR) # random address just to use encode_input


@pytest.fixture(scope="module")
def weth():
    return Contract.from_explorer(WETH_ADDR)


@pytest.fixture(scope="module")
def dai():
    return Contract.from_explorer(DAI_ADDR)
    