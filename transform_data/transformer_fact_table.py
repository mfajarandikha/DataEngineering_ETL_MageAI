import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(passenger_count_dim,trip_distance_dim,rate_code_dim,pickup_location_dim,dropoff_location_dim,datetime_dim,payment_type_dim, *args, **kwargs):
    fact_table = (
        df.merge(passenger_count_dim, left_on="trip_id", right_on="passenger_count_id")
        .merge(trip_distance_dim, left_on="trip_id", right_on="trip_distance_id")
        .merge(rate_code_dim, left_on="trip_id", right_on="rate_code_id")
        .merge(pickup_location_dim, left_on="trip_id", right_on="pickup_location_id")
        .merge(dropoff_location_dim, left_on="trip_id", right_on="dropoff_location_id")
        .merge(datetime_dim, left_on="trip_id", right_on="datetime_id")
        .merge(payment_type_dim, left_on="trip_id", right_on="payment_type_id")[
            [
                "trip_id",
                "VendorID",
                "datetime_id",
                "passenger_count_id",
                "trip_distance_id",
                "rate_code_id",
                "store_and_fwd_flag",
                "pickup_location_id",
                "dropoff_location_id",
                "payment_type_id",
                "fare_amount",
                "extra",
                "mta_tax",
                "tip_amount",
                "tolls_amount",
                "improvement_surcharge",
                "total_amount",
            ]
        ]
    )

    return {
        "fact_table": fact_table.to_dict(orient="dict"),
    }


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
