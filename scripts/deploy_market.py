from brownie import Contract, accounts, interface

def rc(name):
    with open('abi/' + name + '.txt') as datafile:
        return Contract.from_abi(name, globals()[name], eval(datafile.read()))

# Arbitrum addresses
FUSE_MASTER_PRICE_ORACLE_ADDR = '0x59FA438cD0731EBF5F4cDCaf72D4960EFd13FCe6'
FUSE_DEFAULT_ORACLE_ADDR = '0x137a6Bf7D4C866fFd430cDd0107dE6C4828Ce54d'
FUSE_INITIALIZABLE_CLONES_ADDR = '0x94BFbeC0Be156E85D4a7B398Ab70a27bA02D828a'
COMPTROLLER_IMPL_ADDR = '0x53cc546053a09431c9d1a2b288471680d15000a4'
FUSE_POOL_DIR_ADDR = '0xc201b8c8dd22c779025e16f1825c90e1e6dd6a08'
JUMP_RATE_MODEL_ADDR = '0xef562dd508f3dbba4b4ad62a869627d379692557'
CETHER_IMPLEMENTATION_ADDR = '0x440253a301b4fc749a24e653fdb11b742e621892'

def main():

#     contract = Contract.from_explorer(FUSE_INITIALIZABLE_CLONES_ADDR)
#     with open('abi/FUSE_INITIALIZABLE_CLONES_ADDR.txt', 'w') as datafile:
#         datafile.write(repr(contract.abi))

    master_price_oracle = rc('FUSE_MASTER_PRICE_ORACLE_ADDR')
    oracle = rc('FUSE_MASTER_PRICE_ORACLE_ADDR')
    fuse_clones = rc('FUSE_INITIALIZABLE_CLONES_ADDR')
    fuse = rc('FUSE_POOL_DIR_ADDR')
    comptroller = rc('COMPTROLLER_IMPL_ADDR')
    delegator = interface.ICDelegator(FUSE_MASTER_PRICE_ORACLE_ADDR) # random address just to use encode_input

    class Context:
        pass
    auto = Context()
    auto.DEPLOYER = accounts.load('deploy') # 0x775ee1C182B7C9C2b588dBBC21d804AeFB05B919
    auto.FR_DEPLOYER = {"from": auto.DEPLOYER}

    initializer_data = master_price_oracle.initialize.encode_input(
        [],
        [],
        FUSE_DEFAULT_ORACLE_ADDR,
        auto.DEPLOYER,
        True
    )
    clone_tx = fuse_clones.clone(FUSE_MASTER_PRICE_ORACLE_ADDR, initializer_data, auto.FR_DEPLOYER)
    oracle_addr = clone_tx.events['Deployed']['instance']

    oracle_addr = '0x37A6eEd97Ce8217e66b8eF01Ed957DA186E7c8fb'

#     fuse.deployPool(
#         'Test0',
#         COMPTROLLER_IMPL_ADDR,
#         False,
#         500000000000000000,
#         1080000000000000000,
#         oracle_addr,
#         auto.FR_DEPLOYER
#     )
#
#     pools = fuse.getPoolsByAccount(auto.DEPLOYER)
#     unitroller_addr = pools[1][0][2] # TODO

    unitroller_addr = '0x4C4AE0907AEF6d61cB4A93c608f144C967c4537c'

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
    ).replace('0x3e2839ee', '0x')
    isCEther = True
    collateralFactorMantissa = 700000000000000000

    unitroller = Contract.from_abi('Unitroller', unitroller_addr, comptroller.abi)
    unitroller._deployMarket(isCEther, constructor_data, collateralFactorMantissa, auto.FR_DEPLOYER)

