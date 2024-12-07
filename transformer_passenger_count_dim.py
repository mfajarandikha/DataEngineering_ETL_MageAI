import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    passenger_count_dim = df[["passenger_count"]].reset_index(drop=True)
    passenger_count_dim["passenger_count_id"] = passenger_count_dim.index
    passenger_count_dim = passenger_count_dim[["passenger_count_id", "passenger_count"]]

    return {
        "passenger_count_dim": passenger_count_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
