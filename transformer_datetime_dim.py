import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])   
    datetime_dim = df[["tpep_pickup_datetime", "tpep_dropoff_datetime"]].reset_index(
        drop=True
    )
    datetime_dim["tpep_pickup_datetime"] = datetime_dim["tpep_pickup_datetime"]
    datetime_dim["pick_hour"] = datetime_dim["tpep_pickup_datetime"].dt.hour
    datetime_dim["pick_day"] = datetime_dim["tpep_pickup_datetime"].dt.day
    datetime_dim["pick_month"] = datetime_dim["tpep_pickup_datetime"].dt.month
    datetime_dim["pick_year"] = datetime_dim["tpep_pickup_datetime"].dt.year
    datetime_dim["pick_weekday"] = datetime_dim["tpep_pickup_datetime"].dt.weekday

    datetime_dim["tpep_dropoff_datetime"] = datetime_dim["tpep_dropoff_datetime"]
    datetime_dim["drop_hour"] = datetime_dim["tpep_dropoff_datetime"].dt.hour
    datetime_dim["drop_day"] = datetime_dim["tpep_dropoff_datetime"].dt.day
    datetime_dim["drop_month"] = datetime_dim["tpep_dropoff_datetime"].dt.month
    datetime_dim["drop_year"] = datetime_dim["tpep_dropoff_datetime"].dt.year
    datetime_dim["drop_weekday"] = datetime_dim["tpep_dropoff_datetime"].dt.weekday

    datetime_dim["datetime_id"] = datetime_dim.index

    datetime_dim = datetime_dim[
        [
            "datetime_id",
            "tpep_pickup_datetime",
            "pick_hour",
            "pick_day",
            "pick_month",
            "pick_year",
            "pick_weekday",
            "tpep_dropoff_datetime",
            "drop_hour",
            "drop_day",
            "drop_month",
            "drop_year",
            "drop_weekday",
        ]
    ]

    return {
        "datetime_dim": datetime_dim.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
