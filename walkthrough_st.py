"""
Purpose:
    Gitpod: Polygon NFT Workshop
"""

# Python imports
import logging
import os
import streamlit as st
from typing import Type, Union, Dict, Any, List
import glob
from pathlib import Path

# Local Python Library Imports
from modules import utils, mint_nft, pinata_api

###
# Streamlit Main Functionality
###


def sidebar() -> None:
    """
    Purpose:
        Shows the side bar
    Args:
        N/A
    Returns:
        N/A
    """

    st.sidebar.header(f"Polygon NFT Workshop")

    # sidebar_important_links()
    sidebar_navigation()


###
# Utility Functionality
###


def sidebar_important_links() -> None:
    """
    Purpose:
        Important Links Component of Sidebar
    Args:
        N/A
    Returns:
        N/A
    """

    important_links = {
        "Gitpod": "https://www.gitpod.io",
        "Metamask": "https://metamask.io/",
        "Polygon": "https://polygon.technology/",
    }
    important_link_markdown = "  \n".join(
        [f"[{link_text}]({url})" for link_text, url in important_links.items()]
    )

    st.sidebar.title("Important Links")
    st.sidebar.write(important_link_markdown)


def render_module(module) -> None:
    """
    Purpose:
        Render the module
    Args:
        module - name of module:
    Returns:
        N/A
    """

    st.header(module)

    # Hmmm basicaly each module is a streamlit page..
    if module == "1. Introduction":
        st.write(
            "Welcome to the Polygon NFT Workshop. By the end of this workshop you will have completed the following..."
        )
        st.markdown("* Deploy an NFT smart contract to the Polygon Testnet")
        st.markdown("* Pin NFT metadata to IPFS ")
        st.markdown("* Mint an NFT")

        st.markdown(
            "This workshop leveages [Gitpod](https://www.gitpod.io) so you can easily code and get started without having to worry about dependencies"
        )

        st.write("Use the Navigation Panel in the sidebar to switch beteen modules.")

    if module == "2. Install MetaMask":
        st.write(
            "[MetaMask](https://metamask.io/) provides a crypto wallet which is your digtial identity on the blockchain."
        )
        st.write(
            "In order to interact with blockchain applications you will need to install [MetaMask](https://metamask.io/download.html)"
        )

        st.image("https://images.ctfassets.net/9sy2a0egs6zh/6ngCUoU36ABPjs6cDNnuoK/a4b9e978595248dbb685aa2c53e3f4dc/download-extension.png")

    if module == "3. Sign up for Infura":
        st.write(
            "[Infura](https://infura.io/) provides APIs that make it easy to interact with the blockchain. In order to deploy our smart contract to the Polygon Testnet we will need Infura"
        )

        st.write("Once you sign up, be sure to add the Polygon PoS network add-on")
        st.image("./images/infura_polygon_addon.png")
        st.write(
            "Next create a new Project, and save the Project ID. We will need the ID for deployment"
        )

    if module == "4. Edit Smart Contract":
        st.write("In this module we are going to edit the smart contract code.")
        st.markdown("* Open contracts/MyNFT.sol")
        st.markdown("* On line 9 replace 'REPLACE_NAME' with your NFT contract name")
        st.markdown("* On line 16 replace 'REPLACE_NAME' with your NFT contract name")
        st.markdown("* On line 16 replace 'REPLACE_SYM' with your NFT contract symbol")

        st.write("Open migrations/2_deploy_contracts.js")
        st.markdown("* On line 1 replace 'REPLACE_NAME' with your NFT contract name")

    if module == "5. Get MATIC from Facuet":
        st.write(
            "Before we can deploy to the testnet we will need to get MATIC from the facuet"
        )
        st.write(
            "The Faucet allows you to get free MATIC on test networks, simply enter your public key to get funds"
        )
        st.write("https://faucet.matic.network/")

        st.image("images/matic_faucet.png")

    if module == "6. Deploy Smart Contract":
        st.write(
            "In the terminal run the command below, with your values to deploy your smart contract to the blockchain"
        )

        st.info(
            "To export your private key follow: https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key"
        )

        st.code(
            "INFURA_KEY=YOUR_KEY OWNER_ADDRESS=YOUR_PUBLIC_KEY PRIVATE_KEY=YOUR_PRIVATE_KEY CONTRACTS_DIR=./contracts/ CONTRACTS_BUILD=./build/contracts truffle migrate --reset --network mumbai"
        )

        st.info("The following is an example deployment")

        st.code(
            """
Starting migrations...
======================
> Network name:    'mumbai'
> Network id:      80001
> Block gas limit: 20000000 (0x1312d00)


1_initial_migration.js
======================

Deploying 'Migrations'
----------------------
> transaction hash:    0xf3d215e6a4a6c1aed672eb76e52ce64d78c2ff6b80948b08ab5aa403643830ab
> Blocks: 3            Seconds: 4
> contract address:    0xf690F0BE8121A320a549eD5056c650A058A76C35
> block number:        18438906
> block timestamp:     1630632091
> account:             0xd714c8126D36b286d88c4F5Dc7f7f361b92acF11
> balance:             2.6870108915
> gas used:            245600 (0x3bf60)
> gas price:           1 gwei
> value sent:          0 ETH
> total cost:          0.0002456 ETH

Pausing for 2 confirmations...
------------------------------
> confirmation number: 2 (block: 18438909)

> Saving migration to chain.
> Saving artifacts
-------------------------------------
> Total cost:           0.0002456 ETH


2_deploy_contracts.js
=====================

Deploying 'WorkshopTest'
------------------------
> transaction hash:    0x65498b86d83a8c63dd206c3a177a9fb35245cc3e29f6fe9bdecc8894468d59f0
> Blocks: 2            Seconds: 4

######################## THIS IS YOUR NFT CONTRACT ########################
> contract address:    0x637868A804816f2c78bf8fb8a877714f4D8381BB    
######################## THIS IS YOUR NFT CONTRACT ########################

> block number:        18438916
> block timestamp:     1630632115
> account:             0xd714c8126D36b286d88c4F5Dc7f7f361b92acF11
> balance:             2.6827823105
> gas used:            4182668 (0x3fd28c)
> gas price:           1 gwei
> value sent:          0 ETH
> total cost:          0.004182668 ETH

Pausing for 2 confirmations...
------------------------------
> confirmation number: 2 (block: 18438919)

> Saving migration to chain.
> Saving artifacts
-------------------------------------
> Total cost:         0.004182668 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.004428268 ETH
        """
        )

    if module == "7. View contract on Polygon Scan":
        st.write("Once the contract is deployed you can view it at the following URL")
        st.write("https://mumbai.polygonscan.com/address/YOUR_CONTRACT_ADDRESS")
        st.image("images/polygon_scan.png")

    if module == "8. Sign up for Pinata":
        st.write(
            "Now that our contract is deployed, the next thing we need to do is mint an NFT"
        )
        st.write(
            "We will leveagre Pinata (https://www.pinata.cloud/) to store our NFT Metadata"
        )
        st.write("Create an acocunt and save your API keys")

    if module == "9. Create Metadata JSON":
        st.write("Now we can populate the fields needed for the metadata json")

        st.info(
            "To learn more about the metadata fields read this article: https://docs.opensea.io/docs/metadata-standards"
        )
        st.write("Fill in the fields below to create your NFT metadata")

        create_metadata_json()

    if module == "10. Mint NFT":
        st.write("Now we can mint an NFT using the metadata you just pinned to IPFS")

        st.write("Run the following commands to mint your NFT")

        st.info(
            "The Application Binary Interface (ABI) is a JSON file that will be in the ./build/contracts/ directory "
        )

        st.markdown(
            """
        ```
        cd scripts/
        export PUBLIC_KEY=PUBLIC_KEY
        export PRIVATE_KEY=PRIVATE_KEY
        export INFURA_KEY=INFURA_KEY
        export NETWORK="mumbai"
        python mint_nft.py --contract_address CONTRACT_ADDRESS --abi_path ABI_PATH --to_address TO_ADDRESS --token_metadata_url
        ```
        """
        )

    if module == "11. View NFT on OpenSea":

        st.write(
            "Once items have been minted, you can view your collection and items on OpenSea."
        )

        st.write(
            f"OpenSea URL: https://testnets.opensea.io/assets/mumbai/CONTRACT_ADDRESS/0"
        )

        st.info(
            "You may have to enter your contrarct address into the OpenSea search box"
        )

    if module == "12. Sign up for The Graph":

        st.write(
            "Now we are going to utilze The Graph to give us an API to query our contract"
        )

        st.write(
            f"Sign in with your wallet here https://thegraph.com/studio/ and create a new subgraph"
        )

        st.image("images/graph_logo.png")

    if module == "13. Initialize your subgraph":
        st.write(
            "Once your subgraph is created you can use the graph-cli to initalize your subgraph"
        )
        st.code("graph init --studio test_graph")
        st.write("1. Select mumbai for network ")
        st.write("2. Enter in your contract address")
        st.write("3. Enter in the ABI Path that we used in step 10.")

        st.info("Example...")
        st.code(
        """
✔ Ethereum network · mumbai  
✔ Contract address · 0x30B5423D1e60b79c1D9137F3793B81f5186ABd2E  
✖ Failed to fetch ABI from Etherscan: request to https://api-mumbai.etherscan.io/api?module=contract&action=getabi&address=0x30B5423D1e60b79c1D9137F3793B81f5186ABd2E failed, reason: getaddrinfo ENOTFOUND api-mumbai.etherscan.io  
✔ ABI file (path) · ./build/contracts/PolygonWorkshop.json  
        """)

        st.write("Now login to the graph using your api key")
        st.code("graph auth --studio YOUR_API_KEY")
        st.code("cd test_graph")

    if module == "14. Deploy your subgraph":
        st.write("Now we need to update the generated code")
        st.markdown("**1. Add the startblock to the subgraph.yaml**")
        st.write(
            "Find the start block from the polygon scan https://mumbai.polygonscan.com/address/YOUR_CONTRACT_ADDRESS"
        )
        st.image("images/startblock.png")

        st.write("Now add the `startBlock` field in subgraph.yaml")
        st.image("images/add_startblock.png")

        st.markdown("**2. Update the schema.graphql**")

        st.write(
            "Update the schema.graphql file and replace `YOUR_ENTITY_NAME` with your NFT name"
        )
        st.code(
            """
type YOUR_NFT_NAME @entity {
    id: ID!
    tokenURI: String!
    owner: String!
    tokenID: Int!
}
        """
        )

        st.write("Update your graph")
        st.code("graph codegen")


        st.markdown("**3. Update src/mapping.ts**")
        st.write("Replace the code with the following, while adding in your values")
        st.code(
            """
import { BigInt } from "@graphprotocol/graph-ts"
import {
  NFT_NAME,
  Transfer
} from "../generated/PolygonWorkshop/PolygonWorkshop"
import { ENTITY_NAME } from "../generated/schema"

export function handleTransfer(event: Transfer): void {
  // Entities can be loaded from the store using a string ID; this ID
  // needs to be unique across all entities of the same type
  
  var token_id = event.params.tokenId.toString()
  var token_id_int = event.params.tokenId.toI32()
  
  let my_nft = ENTITY_NAME.load(token_id)
  let tokenContract = NFT_NAME.bind(event.address);
  
  if (!my_nft) {
      my_nft = new ENTITY_NAME(event.params.tokenId.toString())
  
      my_nft.owner = event.params.to.toHexString()
      my_nft.tokenURI = tokenContract.tokenURI(event.params.tokenId);
      my_nft.tokenID = token_id_int
  }
  
  else {
      my_nft.owner = event.params.to.toHexString()
      my_nft.tokenURI = tokenContract.tokenURI(event.params.tokenId);
      my_nft.tokenID = token_id_int
  }
  
  my_nft.save();
}
    """
        )

        st.markdown("**4. Deploy your subgraph**")
        st.write("Run the following commands to deploy your subgraph")
        st.code("graph build")
        st.code("graph deploy --studio test_graph")

    if module == "15. Query your NFT Contract":
        st.write("Now you can query you subgraph in The Graph Studio")
        st.image("images/subgraph_example.png")

        st.write("You can also use the provided script to query your subgraph")

        st.code("cd scripts")
        st.code(
            "python query_graph.py --address YOUR_ADDRESS --entity_name YOUR_ENTIY_NAME --subgraph_api YOUR_API_ENDPOINT"
        )

        st.info("You can find your API link in the details tab in the Graph Studio")
        st.info("You may have to add an 's' to your entity name e.g polygontest -> polygontests")


def get_items() -> List:
    """
    Purpose:
        Load list of items
    Args:
        N/A
    Returns:
        items
    """
    items = {}

    json_files = glob.glob("metadata_jsons/*.json")

    for json_file in json_files:

        json_obj = utils.load_json(json_file)
        key = Path(json_file).stem
        item_name = json_obj["item"]["name"]
        items[f"{item_name}_{key}"] = json_obj

    return items


def mint_nft_module():
    """
    Purpose:
        Mint your NFT
    Args:
        N/A
    Returns:
        N/A
    """
    items = get_items()
    item_list = list(items.keys())
    item_list_name = st.selectbox("Items", item_list)

    if item_list_name:

        item_obj = items[item_list_name]

        token_uri = item_obj["ipfs_url"]
        item_json = item_obj["item"]

        st.write("Item metadata")
        st.write(item_json)

        token_address = st.text_input("Address to send token", "")

        if st.button(f"Mint token"):
            with st.spinner("Minting..."):
                eth_json = mint_nft.set_up_blockchain(
                    contract,
                    abi_path,
                    public_key,
                    private_key,
                    infura_key,
                    network,
                )

                txn_hash = mint_nft.web3_mint(token_address, token_uri, eth_json)

                if network == "mumbai":
                    scan_url = "https://explorer-mumbai.maticvigil.com/tx/"
                elif network == "rinkeby":
                    scan_url = "https://rinkeby.etherscan.io/tx/"

                st.success(f"txn hash: {txn_hash}")
                st.write(f"{scan_url}{txn_hash}")
                st.balloons()


def create_metadata_json():
    """
    Purpose:
        Create metadata JSON
    Args:
        N/A
    Returns:
        N/A
    """

    item_json = create_item()

    st.subheader("Current Metadata")
    st.write(item_json)

    st.write("Enter in your pinata.cloud API keys")
    st.write("https://pinata.cloud/keys")

    pinata_key = st.text_input("Pinata Key", "", type="password")
    pinata_secret_key = st.text_input("Pinata Secret key", "", type="password")

    if st.button("Pin Metadata to IPFS"):
        hash_info = pinata_api.pinJSONToIPFS(item_json, pinata_key, pinata_secret_key)

        ipfs_hash = hash_info["IpfsHash"]
        item_final_json = {}
        item_final_json["hash_info"] = hash_info
        item_final_json["item"] = item_json
        item_final_json["url"] = f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}"
        item_final_json["ipfs_url"] = f"ipfs://{ipfs_hash}"

        utils.save_json(f"metadata_jsons/{ipfs_hash}.json", item_final_json)

        st.write(item_final_json["url"])


def create_item():
    """
    Purpose:
        Shows the create item screen
    Args:
        N/A
    Returns:
        N/A
    """
    st.subheader("Create new item")

    item_name = st.text_input("Item name", "", help="Name of the item.")
    ext_url = st.text_input(
        "External URL",
        "",
        help="This is the URL that will appear below the asset's image on OpenSea and will allow users to leave OpenSea and view the item on your site.",
    )
    item_desc = st.text_input(
        "Description",
        "",
        help="A human readable description of the item. Markdown is supported.",
    )
    image_url = st.text_input(
        "Image Url",
        "",
        help="This is the URL to the image of the item. Can be just about any type of image (including SVGs, which will be cached into PNGs by OpenSea, and even MP4s), and can be IPFS URLs or paths. We recommend using a 350 x 350 image.",
    )

    item_color = st.color_picker(
        "background_color",
        "#ffffff",
        help="Background color of the item on OpenSea. Must be a six-character hexadecimal without a pre-pended #.",
    )

    animation_url = st.text_input(
        "animation_url",
        "",
        help="A URL to a multi-media attachment for the item. The file extensions GLTF, GLB, WEBM, MP4, M4V, OGV, and OGG are supported, along with the audio-only extensions MP3, WAV, and OGA.Animation_url also supports HTML pages, allowing you to build rich experiences and interactive NFTs using JavaScript canvas, WebGL, and more. Scripts and relative paths within the HTML page are now supported. However, access to browser extensions is not supported.",
    )

    youtube_url = st.text_input(
        "youtube_url",
        "",
        help="A URL to a YouTube video.",
    )

    # This is where session state will shine
    if "attrs" not in st.session_state:
        st.session_state.attrs = 1

    if st.button("Add attribute"):
        st.session_state.attrs += 1

    if st.button("Remove attribute"):
        st.session_state.attrs -= 1

    attr_types = ["Text", "Number", "Date"]
    attr_list = []

    for index in range(st.session_state.attrs):

        st.subheader(f"Attribute {index}")

        attr_json = {}
        attr_type = st.selectbox(
            "Attribute type", attr_types, key=f"attr_types_index_{index}"
        )

        if attr_type == "Text":

            trait_type = st.text_input("trait type", "", key=f"trait_index_{index}")
            value = st.text_input("Value", "", key=f"value_index_{index}")

            attr_json["trait_type"] = trait_type
            attr_json["value"] = value

        if attr_type == "Number":

            display_types = ["number", "boost_number", "boost_percentage", "ranking"]
            display_type = st.selectbox(
                "dislay type", display_types, key=f"display_index_{index}"
            )

            trait_type = st.text_input("trait type", "", key=f"trait_index_{index}")
            value = st.text_input("Value", "", key=f"value_index_{index}")

            if not display_type == "ranking":
                attr_json["display_type"] = display_type
            attr_json["trait_type"] = trait_type
            attr_json["value"] = value

        if attr_type == "Date":

            trait_type = st.text_input("trait type", "", key=f"trait_index_{index}")

            st.write("Pass in a unix timestamp for the value")
            value = st.text_input("Value", "", key=f"value_index_{index}")

            attr_json["display_type"] = "date"
            attr_json["trait_type"] = trait_type
            attr_json["value"] = value

        attr_list.append(attr_json)

    item_json = {}
    item_json["name"] = item_name
    item_json["image"] = image_url
    item_json["external_url"] = ext_url
    item_json["description"] = item_desc
    item_json["background_color"] = item_color.replace("#", "")
    item_json["animation_url"] = animation_url
    item_json["youtube_url"] = youtube_url
    # attrs = st.session_state.attrs
    item_json["attributes"] = attr_list

    return item_json


def sidebar_navigation() -> None:
    """
    Purpose:
        Navigation Component of Sidebar
    Args:
        N/A
    Returns:
        N/A
    """

    # Create the Navigation Section
    st.sidebar.title("Navigation")

    modules = [
        "1. Introduction",
        "2. Install MetaMask",
        "3. Sign up for Infura",
        "4. Edit Smart Contract",
        "5. Get MATIC from Facuet",
        "6. Deploy Smart Contract",
        "7. View contract on Polygon Scan",
        "8. Sign up for Pinata",
        "9. Create Metadata JSON",
        "10. Mint NFT",
        "11. View NFT on OpenSea",
        "12. Sign up for The Graph",
        "13. Initialize your subgraph",
        "14. Deploy your subgraph",
        "15. Query your NFT Contract",
    ]

    module = st.sidebar.selectbox("Modules", modules)

    render_module(module)


def show_iframe(url):
    """
    Purpose:
        Show Iframe of a page
    Args:
        url: url of iframe to show
    Returns:
        N/A
    """

    st.write(
        f'<iframe width="100%" frameborder="0" style="overflow: hidden;height: 50vh" src="'
        + url
        + '"></iframe>',
        unsafe_allow_html=True,
    )


def main_page() -> None:
    """
    Purpose:
        Controls the app flow
    Args:
        N/A
    Returns:
        N/A
    """

    # main page
    st.write("Hello")
    # gitpod_url = ""
    # show_iframe(gitpod_url)


def app() -> None:
    """
    Purpose:
        Controls the app flow
    Args:
        N/A
    Returns:
        N/A
    """

    # Spin up the sidebar, will control which page is loaded in the
    # main app
    sidebar()
    # Start main page
    # main_page()


def main() -> None:
    """
    Purpose:
        Controls the flow of the streamlit app
    Args:
        N/A
    Returns:
        N/A
    """

    # Start the streamlit app
    app()


if __name__ == "__main__":
    main()
