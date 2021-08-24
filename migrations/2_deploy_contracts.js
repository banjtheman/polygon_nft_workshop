const NFT = artifacts.require("REPLACE_NAME");
const proxyRegistryAddress = process.env.OWNER_ADDRESS


module.exports = async function (deployer, _network, accounts) {
  await deployer.deploy(NFT,proxyRegistryAddress, {gas: 5000000});
  const nft = await NFT.deployed();
};
