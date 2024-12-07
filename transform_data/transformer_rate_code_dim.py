import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    rate_code_type = {
        1: "Standard rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride",
    }

    rate_code_dim = df[["RatecodeID"]].reset_index(drop=True)
    rate_code_dim["rate_code_id"] = rate_code_dim.index
    rate_code_dim["rate_code_name"] = rate_code_dim["RatecodeID"].map(rate_code_type)
    rate_code_dim = rate_code_dim[["rate_code_id", "RatecodeID", "rate_code_name"]]

    return {
        "rate_code_dim": rate_code_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
