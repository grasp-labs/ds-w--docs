"""
Example Python script for using the Grasp AS Stoa package.
Find more information here: https://pypi.org/project/ds-stoa/

Example command: pipenv run python sample.py --client_id abc --client_secret def --config config.json
"""
import argparse
import json
import typing

import pandas as pd
from ds_stoa.manager import StoaClient


def fetch(client_id: str, client_secret: str, config: typing.Dict) -> pd.DataFrame:
    """
    Function to fetch data from the API.
    @param client_id: client_id
    @param client_secret: client_secret
    @param config: config.
    @return: fetched data
    """
    stoa = StoaClient(
        authentication="oauth2",
        client_id=client_id,
        client_secret=client_secret,
        **config,
    )

    return stoa.fetch(format="dataframe")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from the API.")
    parser.add_argument("--client_id", type=str, help="Client ID", required=True)
    parser.add_argument(
        "--client_secret", type=str, help="Client Secret", required=True
    )
    parser.add_argument(
        "--config", type=str, help="Path to the config file", required=True
    )

    # Parse the arguments
    args = parser.parse_args()
    # Load the config file
    with open(args.config, "r") as f:
        config = json.load(f)

    data = fetch(args.client_id, args.client_secret, config)
    print(data.head())
