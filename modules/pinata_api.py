import json
from typing import Type, Union, Dict, Any, List
import requests
import os
from pathlib import Path


def pinJSONToIPFS(
    json_obj: Dict[str, Any], pinata_api_key: str, pinata_secret: str
) -> Dict[str, Any]:
    """
    Purpose:
        PIN a json obj to IPFS
    Args:
        json_obj - The json obj
        pinata_api_key - pinata api key
        pinata_secret - pinata secret key
    Returns:
        ipfs json - data from pin
    """
    HEADERS = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret,
    }

    ipfs_json = {
        "pinataMetadata": {
            "name": json_obj["name"],
        },
        "pinataContent": json_obj,
    }

    endpoint_uri = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    response = requests.post(endpoint_uri, headers=HEADERS, json=ipfs_json)
    return response.json()


def pinContentToIPFS(
    filepath: str, pinata_api_key: str, pinata_secret: str
) -> Dict[str, Any]:
    """
    Purpose:
        PIN a file obj to IPFS
    Args:
        filepath - file path
        pinata_api_key - pinata api key
        pinata_secret - pinata secret key
    Returns:
        ipfs json - data from pin
    """

    HEADERS = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret,
    }

    endpoint_uri = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    filename = filepath.split("/")[-1:][0]

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            endpoint_uri, files={"file": (filename, image_binary)}, headers=HEADERS
        )
        print(response.json())

        # response = requests.post(endpoint_uri, data=multipart_form_data, headers=HEADERS)
        # print(response.text)
        # print(response.headers)
        return response.json()


def pinSearch(
    query: str, pinata_api_key: str, pinata_secret: str
) -> List[Dict[str, Any]]:
    """
    Purpose:
        Query pins for data
    Args:
        query - the query str
        pinata_api_key - pinata api key
        pinata_secret - pinata secret key
    Returns:
        data - array of pined objects
    """

    endpoint_uri = f"https://api.pinata.cloud/data/pinList?{query}"
    HEADERS = {
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret,
    }
    response = requests.get(endpoint_uri, headers=HEADERS).json()

    # now get the actual data from this
    data = []
    if "rows" in response:

        for item in response["rows"]:
            ipfs_pin_hash = item["ipfs_pin_hash"]
            hash_data = requests.get(
                f"https://gateway.pinata.cloud/ipfs/{ipfs_pin_hash}"
            ).json()
            data.append(hash_data)

    # print(response.json())
    return data
