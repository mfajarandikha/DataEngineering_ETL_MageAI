import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df,df_location, *args, **kwargs):
    df = pd.merge(
        df,
        df_location[["LocationID", "Borough", "Zone"]],
        left_on="DOLocationID",
        right_on="LocationID",
        how="left",
    )
    df.rename(
        columns={"Borough": "borough_dropoff", "Zone": "zone_dropoff"}, inplace=True
    )

    dropoff_location_dim = df[["borough_dropoff", "zone_dropoff"]].reset_index(
        drop=True
    )
    dropoff_location_dim["dropoff_location_id"] = dropoff_location_dim.index
    dropoff_location_dim = dropoff_location_dim[
        ["dropoff_location_id", "borough_dropoff", "zone_dropoff"]
    ]

    return {
        "dropoff_location_dim": dropoff_location_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
