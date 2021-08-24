// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC721Tradable.sol";

/**
 * @title MyNFT
 * MyNFT - My NFT contract.
 */
contract REPLACE_NAME is ERC721Tradable {
    uint256 public nextTokenId;
    address public admin;

    constructor(address _proxyRegistryAddress)
        public
        ERC721Tradable("REPLACE_NAME", "REPLACE_SYM", _proxyRegistryAddress)
    {
        admin = msg.sender;
    }

    // only our wallet should be able to mint
    function mint(address to, string memory tokenURI) external onlyOwner {
        _safeMint(to, nextTokenId);
        _setTokenURI(nextTokenId, tokenURI);
        nextTokenId++;
    }

    function baseTokenURI() public pure override returns (string memory) {
        return "";
    }
}
