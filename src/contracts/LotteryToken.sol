// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract LotteryToken is ERC721URIStorage {
    uint256 public lotteryCounter;

    constructor() ERC721("LotteryToken", "LT") {
        lotteryCounter = 0;
    }

    function issueLottery(string memory tokenURI) public returns (uint256) {
        uint256 newTokenId = lotteryCounter;

        _safeMint(msg.sender, newTokenId);
        _setTokenURI(lotteryCounter, tokenURI);
        lotteryCounter += 1;

        return lotteryCounter;
    }
}
