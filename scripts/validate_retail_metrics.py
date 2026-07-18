"""Validate the retail cleaning contract and executive metrics."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SOURCE = Path(__file__).resolve().parents[1] / "data" / "raw" / "Online Retail.xlsx"


def build_analytical_population(source: Path = SOURCE) -> pd.DataFrame:
    frame = pd.read_excel(source, dtype={"InvoiceNo": str, "StockCode": str})
    frame = frame.dropna(subset=["Description"]).drop_duplicates()
    frame = frame.loc[frame["Quantity"].gt(0) & frame["UnitPrice"].ge(0)].copy()
    frame["LineSales"] = frame["Quantity"] * frame["UnitPrice"]
    return frame


def calculate_metrics(frame: pd.DataFrame) -> dict[str, float | int]:
    sales = float(frame["LineSales"].sum())
    orders = int(frame["InvoiceNo"].nunique())
    return {
        "rows": len(frame),
        "sales": sales,
        "orders": orders,
        "identified_customers": int(frame["CustomerID"].nunique()),
        "products_sold": int(frame["StockCode"].nunique()),
        "countries": int(frame["Country"].nunique()),
        "average_order_value": sales / orders,
    }


def main() -> None:
    metrics = calculate_metrics(build_analytical_population())
    expected = {
        "rows": 525_460,
        "sales": 10_642_110.804,
        "orders": 20_134,
        "identified_customers": 4_339,
        "products_sold": 3_925,
        "countries": 38,
        "average_order_value": 528.564160325817,
    }

    for name, expected_value in expected.items():
        actual_value = metrics[name]
        if isinstance(expected_value, float):
            assert abs(float(actual_value) - expected_value) < 0.001, (name, actual_value)
        else:
            assert actual_value == expected_value, (name, actual_value)

    for name, value in metrics.items():
        print(f"{name}: {value:,.2f}" if isinstance(value, float) else f"{name}: {value:,}")


if __name__ == "__main__":
    main()
