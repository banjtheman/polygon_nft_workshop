# Python imports
import os
import json
import logging
from typing import Type, Union, Dict, Any, List

from web3 import Web3


def load_json(path_to_json: str) -> Dict[str, Any]:
    """
    Purpose:
        Load json files
    Args:
        path_to_json (String): Path to  json file
    Returns:
        Conf: JSON file if loaded, else None
    """
    try:
        with open(path_to_json, "r") as config_file:
            conf = json.load(config_file)
            return conf

    except Exception as error:
        logging.error(error)
        raise TypeError("Invalid JSON file")


def set_up_blockchain(
    contract: str,
    abi_path: str,
    public_key: str,
    private_key: str,
    infura_key: str,
    network: str,
):
    """
    Purpose:
       Setup all blockchain items
    Args:
        contract: contract address
        abi_path: abi path
        public_key: public key,
        private_key: private key,
        infura_key: infura key,
        network: network,
    Returns:
        Conf: JSON file with eth details
    """
    ############ Ethereum Setup ############

    PUBLIC_KEY = public_key
    PRIVATE_KEY = Web3.toBytes(hexstr=private_key)
    INFURA_KEY = infura_key

    network = network
    ABI = None
    CODE_NFT = None
    CHAIN_ID = None
    w3 = None
    open_sea_url = ""
    scan_url = ""

    eth_json = {}

    if network == "rinkeby":

        RINK_API_URL = f"https://rinkeby.infura.io/v3/{INFURA_KEY}"

        w3 = Web3(Web3.HTTPProvider(RINK_API_URL))
        ABI = load_json(abi_path)["abi"]  # get the ABI
        CODE_NFT = w3.eth.contract(address=contract, abi=ABI)  # The contract
        CHAIN_ID = 4

        open_sea_url = f"https://testnets.opensea.io/assets/{contract}/"
        scan_url = "https://rinkeby.etherscan.io/tx/"

    elif network == "mumbai":
        MUMBAI_API_URL = f"https://polygon-mumbai.infura.io/v3/{INFURA_KEY}"

        w3 = Web3(Web3.HTTPProvider(MUMBAI_API_URL))
        ABI = load_json(abi_path)["abi"]  # get the ABI
        CODE_NFT = w3.eth.contract(address=contract, abi=ABI)  # The contract
        CHAIN_ID = 80001

        open_sea_url = f"https://testnets.opensea.io/assets/{contract}/"
        scan_url = "https://explorer-mumbai.maticvigil.com/tx/"

    elif network == "matic_main":
        POLYGON_API_URL = f"https://polygon-mainnet.infura.io/v3/{INFURA_KEY}"

        w3 = Web3(Web3.HTTPProvider(POLYGON_API_URL))
        ABI = load_json(abi_path)["abi"]  # get the ABI
        CODE_NFT = w3.eth.contract(address=contract, abi=ABI)  # The contract
        CHAIN_ID = 137

        open_sea_url = f"https://opensea.io/assets/matic/{contract}/"
        scan_url = "https://polygonscan.com/tx/"

    else:
        logging.error("Invalid network")
        raise ValueError(f"Invalid {network}")

    logging.info(f"checking if connected to infura...{w3.isConnected()}")

    eth_json["w3"] = w3
    eth_json["contract"] = CODE_NFT
    eth_json["chain_id"] = CHAIN_ID
    eth_json["open_sea_url"] = open_sea_url
    eth_json["scan_url"] = scan_url
    eth_json["public_key"] = PUBLIC_KEY
    eth_json["private_key"] = PRIVATE_KEY

    return eth_json


def web3_mint(userAddress: str, tokenURI: str, eth_json: Dict[str, Any]) -> str:
    """
    Purpose:
        mint a token for user on blockchain
    Args:
        userAddress - the user to mint for
        tokenURI - uri for token
        eth_json - blockchain info
    Returns:
        hash - txn of mint
        tokenid - token minted
    """

    PUBLIC_KEY = eth_json["public_key"]
    CHAIN_ID = eth_json["chain_id"]
    w3 = eth_json["w3"]
    CODE_NFT = eth_json["contract"]
    PRIVATE_KEY = eth_json["private_key"]

    nonce = w3.eth.get_transaction_count(PUBLIC_KEY)
    # logging.info(f"Nonce: {w3.eth.get_transaction_count(PUBLIC_KEY)}")

    # Create the contracrt
    mint_txn = CODE_NFT.functions.mint(userAddress, tokenURI).buildTransaction(
        {
            "chainId": CHAIN_ID,
            "gas": 10000000,
            "gasPrice": w3.toWei("1", "gwei"),
            "nonce": nonce,
        }
    )

    signed_txn = w3.eth.account.sign_transaction(mint_txn, private_key=PRIVATE_KEY)

    w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    hash = w3.toHex(w3.keccak(signed_txn.rawTransaction))

    logging.info(f"mint txn hash: {hash} ")

    receipt = w3.eth.wait_for_transaction_receipt(hash)  # hmmm have to wait...

    hex_tokenid = receipt["logs"][0]["topics"][3].hex()  # this is token id in hex

    # convert from hex to decmial
    tokenid = int(hex_tokenid, 16)
    logging.info(f"Got tokenid: {tokenid}")

    return hash
