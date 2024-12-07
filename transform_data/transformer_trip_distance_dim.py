import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    trip_distance_dim = df[["trip_distance"]].reset_index(drop=True)
    trip_distance_dim["trip_distance_id"] = trip_distance_dim.index
    trip_distance_dim = trip_distance_dim[["trip_distance_id", "trip_distance"]]

    return {
        "trip_distance_dim": trip_distance_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
