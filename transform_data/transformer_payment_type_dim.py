import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    payment_type_name = {
        1: "Credit card",
        2: "Cash",
        3: "No charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided trip",
    }
    payment_type_dim = df[["payment_type"]].reset_index(drop=True)
    payment_type_dim["payment_type_id"] = payment_type_dim.index
    payment_type_dim["payment_type_name"] = payment_type_dim["payment_type"].map(
        payment_type_name
    )
    payment_type_dim = payment_type_dim[
        ["payment_type_id", "payment_type", "payment_type_name"]
    ]

    return {
        "payment_type_dim": payment_type_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
