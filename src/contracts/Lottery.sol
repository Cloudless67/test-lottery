// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    AggregatorV3Interface public eth2usdPriceFeed;

    uint256 public lotteryPrice;
    address payable[] public participants;

    constructor(address _priceFeed, uint256 _lotteryPrice) {
        lotteryPrice = _lotteryPrice;
        eth2usdPriceFeed = AggregatorV3Interface(_priceFeed);
    }

    function participate(uint8[] memory numbers) public payable {
        //
    }
}
