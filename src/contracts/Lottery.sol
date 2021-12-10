// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    AggregatorV3Interface internal eth2usdPriceFeed;

    uint256 public lotteryPrice;
    address payable[] public participants;

    constructor(uint256 _lotteryPrice) {
        lotteryPrice = _lotteryPrice;
        eth2usdPriceFeed = AggregatorV3Interface(
            0x8A753747A1Fa494EC906cE90E9f37563A8AF630e  // Rinkeby
        );
    }

    function participate(uint8[] memory numbers) public payable {
        //
    }
}
