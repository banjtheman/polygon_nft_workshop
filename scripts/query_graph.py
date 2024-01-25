import argparse
import logging
from typing import List
import requests


def query_subgraph(api_endpoint: str, address: str, entity_name: str) -> List:
    """
    Purpose:
       Get ATS from address
    Args:
        api_endpoint - endpoint of api
        address - address of user
        entity_name - name of entity
    Returns:
        subgraph data - list of nft owned by address
    """

    query = (
        """{
        """
        + entity_name
        + """(where: { owner: \""""
        + str(address)
        + """\" }) {
            id
            tokenURI
            owner
            tokenID
        }
    }
    """
    )

    request = requests.post(api_endpoint, json={"query": query}, timeout=60)

    if request.status_code == 200:
        if "errors" in request.json():
            logging.error(request.json()["errors"])
        return request.json()["data"]
    else:
        logging.error("Failed request: " + str(request))
        logging.error(query)
        return None


def main():
    logging.info("Starting Subgraph Query")

    parser = argparse.ArgumentParser(description="Mint NFTs")
    parser.add_argument(
        "--subgraph_api",
        type=str,
        help="API endpoint for subgraph",
        required=True,
    )

    parser.add_argument("--address", type=str, help="address of owner", required=True)

    parser.add_argument(
        "--entity_name", type=str, help="name of your nft entity", required=True
    )

    args = parser.parse_args()
    subgraph_data = query_subgraph(args.subgraph_api, args.address, args.entity_name)
    logging.info(subgraph_data)


if __name__ == "__main__":
    loglevel = logging.INFO
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    main()
