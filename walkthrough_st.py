"""
Purpose:
    Gitpod: Polygon NFT Workshop
"""

# Python imports
import logging
import os
import streamlit as st

# Local Python Library Imports


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

        st.image("https://metamask.io/images/download-extension.png")

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
        st.markdown("* Open MyNFT.sol in the contracts folder")
        st.markdown("* On line 9 replace 'REPLACE_NAME' with your NFT contract name")
        st.markdown("* On line 16 replace 'REPLACE_NAME' with your NFT contract name")
        st.markdown("* On line 16 replace 'REPLACE_SYM' with your NFT contract symbol")

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
        st.write("OK")


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
        "10. Pin Metadata JSON to IPFS",
        "11. Mint NFT",
        "12. View NFT on OpenSea",
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
