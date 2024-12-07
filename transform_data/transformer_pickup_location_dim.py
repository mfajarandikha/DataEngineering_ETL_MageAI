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
        left_on="PULocationID",
        right_on="LocationID",
        how="left",
    )
    df.rename(
        columns={"Borough": "borough_pickup", "Zone": "zone_pickup"}, inplace=True
    )

    pickup_location_dim = df[["borough_pickup", "zone_pickup"]].reset_index(drop=True)
    pickup_location_dim["pickup_location_id"] = pickup_location_dim.index
    pickup_location_dim = pickup_location_dim[
        ["pickup_location_id", "borough_pickup", "zone_pickup"]
    ]

    return {
        "pickup_location_dim": pickup_location_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
