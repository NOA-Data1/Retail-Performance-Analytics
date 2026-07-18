from scripts.validate_retail_metrics import calculate_metrics

import pandas as pd


def test_metric_contract_on_completed_sales() -> None:
    frame = pd.DataFrame(
        {
            "InvoiceNo": ["1", "1", "2"],
            "StockCode": ["A", "B", "A"],
            "CustomerID": [10, 10, None],
            "Country": ["United Kingdom", "United Kingdom", "France"],
            "Quantity": [2, 1, 3],
            "UnitPrice": [5.0, 2.0, 4.0],
        }
    )
    frame["LineSales"] = frame["Quantity"] * frame["UnitPrice"]

    metrics = calculate_metrics(frame)

    assert metrics == {
        "rows": 3,
        "sales": 24.0,
        "orders": 2,
        "identified_customers": 1,
        "products_sold": 2,
        "countries": 2,
        "average_order_value": 12.0,
    }
