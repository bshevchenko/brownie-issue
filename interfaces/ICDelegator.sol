pragma solidity 0.8.6;

interface ICDelegator {
    function initialize(
        address underlying_,
        address comptroller_,
        address interestRateModel_,
        string memory name_,
        string memory symbol_,
        address implementation_,
        bytes memory becomeImplementationData,
        uint256 reserveFactorMantissa_,
        uint256 adminFeeMantissa_
    ) external;

    function etherInitialize(
        address comptroller_,
        address interestRateModel_,
        string memory name_,
        string memory symbol_,
        address implementation_,
        bytes memory becomeImplementationData,
        uint256 reserveFactorMantissa_,
        uint256 adminFeeMantissa_
    ) external;
}
