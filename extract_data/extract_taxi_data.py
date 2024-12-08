import io
import pandas as pd
import requests

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-12.csv.gz"
    response = requests.get(url)
    df = pd.read_csv(io.BytesIO(response.content), compression="gzip")
    df = df.dropna()
    df = df.drop_duplicates().reset_index(drop=True)
    df["trip_id"] = df.index
    return df

    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
