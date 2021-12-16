// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Lottery is VRFConsumerBase {
    AggregatorV3Interface public eth2usdPriceFeed;

    bytes32 keyHash;
    uint256 fee;
    uint256 public lotteryPrice;
    address payable[] public participants;
    uint256 public game_number;
    uint8[6] public game_reuslt;

    constructor(
        address _priceFeed,
        uint256 _lotteryPrice,
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyHash,
        uint256 _fee
    ) VRFConsumerBase(_vrfCoordinator, _linkToken) {
        keyHash = _keyHash;
        fee = _fee;
        lotteryPrice = _lotteryPrice;
        eth2usdPriceFeed = AggregatorV3Interface(_priceFeed);
    }

    function issueLotteryToken(uint8[] memory numbers) public payable {}

    function getRandomNumber() public returns (bytes32 requestId) {
        require(
            LINK.balanceOf(address(this)) >= fee,
            "Not enough LINK - fill contract with faucet"
        );
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness)
        internal
        override
    {
        require(true);
        game_reuslt = extractNumbers(randomness);
    }

    function extractNumbers(uint256 source)
        internal
        pure
        returns (uint8[6] memory)
    {
        uint8[6] memory numbers;

        for (uint256 i = 0; i < 6; i++) {
            numbers[i] = uint8((source % 64) % 45) + 1;
            source >>= 8;
        }

        return numbers;
    }
}
