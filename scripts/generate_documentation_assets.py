"""Generate versioned figures used in the project documentation."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

from validate_retail_metrics import build_analytical_population


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images"
BLUE = "#1267E8"
NAVY = "#121A30"
CORAL = "#F08FA0"
GRID = "#DDE4EE"


def save_monthly_sales(frame: pd.DataFrame) -> None:
    monthly = (
        frame.groupby(frame["InvoiceDate"].dt.to_period("M"))["LineSales"]
        .sum()
        .rename_axis("Month")
        .reset_index()
    )
    monthly["Label"] = monthly["Month"].dt.strftime("%b %Y")

    figure, axis = plt.subplots(figsize=(12, 5.6))
    axis.plot(monthly["Label"], monthly["LineSales"], color=BLUE, marker="o", linewidth=2.8)
    axis.scatter(monthly.iloc[-1:]["Label"], monthly.iloc[-1:]["LineSales"], color=CORAL, zorder=3)
    axis.annotate(
        "Partial month\nthrough 9 Dec",
        (monthly.iloc[-1]["Label"], monthly.iloc[-1]["LineSales"]),
        xytext=(-55, 45),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": CORAL},
        color=NAVY,
    )
    axis.set_title("Monthly sales with partial-period disclosure", loc="left", color=NAVY, weight="bold")
    axis.set_xlabel("")
    axis.set_ylabel("Sales")
    axis.yaxis.set_major_formatter(FuncFormatter(lambda value, _position: f"£{value / 1_000_000:.1f}M"))
    axis.grid(axis="y", color=GRID, linewidth=0.8)
    axis.spines[["top", "right", "left"]].set_visible(False)
    axis.tick_params(axis="x", rotation=45)
    figure.tight_layout()
    figure.savefig(OUTPUT / "monthly_sales_validated.png", dpi=160, bbox_inches="tight")
    plt.close(figure)


def save_market_sales(frame: pd.DataFrame) -> None:
    markets = (
        frame.loc[frame["Country"].ne("United Kingdom")]
        .groupby("Country")["LineSales"]
        .sum()
        .nlargest(10)
        .sort_values()
    )

    figure, axis = plt.subplots(figsize=(10, 5.8))
    axis.barh(markets.index, markets.values, color=BLUE)
    axis.set_title(
        "Top international markets by sales",
        loc="left",
        color=NAVY,
        weight="bold",
        y=1.07,
    )
    axis.text(
        0,
        1.025,
        "United Kingdom excluded for comparability",
        transform=axis.transAxes,
        color="#60708A",
    )
    axis.bar_label(
        axis.containers[0],
        labels=[f"£{value / 1_000:.0f}K" for value in markets.values],
        padding=4,
        color=NAVY,
        fontsize=9,
    )
    axis.set_xlabel("Sales")
    axis.xaxis.set_major_formatter(FuncFormatter(lambda value, _position: f"£{value / 1_000:.0f}K"))
    axis.grid(axis="x", color=GRID, linewidth=0.8)
    axis.set_axisbelow(True)
    axis.spines[["top", "right", "left"]].set_visible(False)
    figure.tight_layout()
    figure.savefig(OUTPUT / "international_market_sales.png", dpi=160, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    data = build_analytical_population()
    save_monthly_sales(data)
    save_market_sales(data)


if __name__ == "__main__":
    main()
