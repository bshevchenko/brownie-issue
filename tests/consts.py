from brownie import a, Contract


# General/shared
ADDR_0 = "0x0000000000000000000000000000000000000000"
E_18 = int(1e18)
INIT_ETH_BAL = 100 * E_18
MAX_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935
BIG_NUM = int(MAX_UINT/2)
MIN_RAND_INPUT_ETH = 2*E_18
MIN_RAND_INPUT_TOKEN = 2*E_18
DAY = 60 * 60 * 24


# Addresses
WETH_ADDR = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
DAI_ADDR = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
UNIV2_ROUTER2_ADDR = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
UNIV2_FACTORY_ADDR = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
UNIV2_DAI_ETH_LP_ADDR = '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11'


FUSE_INITIALIZABLE_CLONES_ADDR = '0x91ce5566dc3170898c5aee4ae4dd314654b47415'
FUSE_POOL_DIR_PROXY_ADDR = '0x835482fe0532f169024d5e9410199369aad5c77e'
FUSE_POOL_DIR_ADDR = '0xd662efb05e8cafe35d1558b8b5323c73e2919abd'
FUSE_POOL_LENS_ADDR = '0x6Dc585Ad66A10214Ef0502492B0CC02F0e836eec'
FUSE_MASTER_PRICE_ORACLE_ADDR = '0xb3c8eE7309BE658c186F986388c2377da436D8fb'
FUSE_DEFAULT_ORACLE_ADDR = '0x1887118E49e0F4A78Bd71B792a49dE03504A764D'
COMPTROLLER_IMPL_ADDR = '0xe16db319d9da7ce40b666dd2e365a4b8b3c18217'
JUMP_RATE_MODEL_ADDR = '0xbAB47e4B692195BF064923178A90Ef999A15f819'
JUMP_RATE_MODEL_UNI_ADDR = '0xc35DB333EF7ce4F246DE9DE11Cc1929d6AA11672'
WHITEPAPER_RATE_MODEL_ETH_ADDR = '0x14ee0270C80bEd60bDC117d4F218DeE0A4909F28'
CETHER_IMPLEMENTATION_ADDR = '0xd77E28A1b9a9cFe1fc2EEE70E391C05d25853cbF'
CERC20_IMPLEMENTATION_ADDR = '0x67Db14E73C2Dce786B5bbBfa4D010dEab4BBFCF9'
