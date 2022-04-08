pragma solidity 0.8.6;

// TODO License
// SPDX-License-Identifier: UNLICENSED

interface CErc20Storage {
    function underlying() external returns (address);
}

interface ICErc20 is CErc20Storage {
    function mint(uint mintAmount) external returns (uint);
    function redeem(uint redeemTokens) external returns (uint);
    function redeemUnderlying(uint redeemAmount) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function repayBorrowBehalf(address borrower, uint repayAmount) external returns (uint);
    function liquidateBorrow(address borrower, uint repayAmount, address cTokenCollateral) external returns (uint);

    function balanceOfUnderlying(address account) external returns (uint);
    function borrowBalanceCurrent(address account) external returns (uint);
}
