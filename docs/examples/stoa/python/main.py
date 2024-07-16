"""
Example Python script for using the Grasp AS Stoa package.
Find more information here: https://pypi.org/project/ds-stoa/
"""
from ds_stoa.manager import StoaClient

# Initialise the class.
stoa = StoaClient(
    authentication="oauth2",
    product_group_name="xledger",
    product_name="entities_1.1",
    workspace="cart",
    owner_id="{{owner_id}}",
    client_id="{{you_client_id}}",
    client_secret="{{you_client_secret}}",
)

# Available formats are dataframe and json.
fetched_xledger_data_df = stoa.fetch(format="dataframe")
print(f"Fetched Data (DataFrame):\n{fetched_xledger_data_df}")
