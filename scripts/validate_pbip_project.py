"""Run structural and portfolio-readiness checks on the Power BI Project."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "powerbi" / "project"
REPORT = PROJECT / "1Retail_Performance.Report"
MODEL = PROJECT / "1Retail_Performance.SemanticModel"
PAGE = REPORT / "definition" / "pages" / "821b879a4b9101a7d7d0"


def main() -> None:
    required = [
        PROJECT / "1Retail_Performance.pbip",
        REPORT / "definition.pbir",
        REPORT / "definition" / "report.json",
        PAGE / "page.json",
        MODEL / "definition.pbism",
        MODEL / "definition" / "model.tmdl",
        MODEL / "definition" / "tables" / "Retail Sales.tmdl",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    assert not missing, f"Missing PBIP files: {missing}"

    for path in PROJECT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))

    page = json.loads((PAGE / "page.json").read_text(encoding="utf-8"))
    page_width = page["width"]
    page_height = page["height"]
    visuals = list((PAGE / "visuals").glob("*/visual.json"))
    assert len(visuals) >= 20, "Executive page is missing expected visuals"

    visual_definitions = {}

    for path in visuals:
        visual = json.loads(path.read_text(encoding="utf-8"))
        visual_definitions[visual["name"]] = visual
        position = visual["position"]
        assert position["x"] >= 0 and position["y"] >= 0, path
        assert position["x"] + position["width"] <= page_width, path
        assert position["y"] + position["height"] <= page_height, path

    public_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in PROJECT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".json", ".tmdl", ".pbip", ".pbir", ".pbism"}
        and ".pbi" not in path.parts
    )
    forbidden = [
        "C:\\Workspace",
        "525.460 linhas",
        "13 meses completos",
        '"displayName": "Página 1"',
        "Fonte: Online Retail",
    ]
    found = [term for term in forbidden if term in public_text]
    assert not found, f"Non-portable or legacy public text found: {found}"

    model = (MODEL / "definition" / "tables" / "Retail Sales.tmdl").read_text(
        encoding="utf-8"
    )
    for required_term in [
        "Web.Contents",
        "ExactDuplicatesRemoved",
        "CompletedSales",
        "NOT ISBLANK('Retail Sales'[CustomerID])",
        "REMOVEFILTERS('Retail Sales'[Country])",
        "measure 'Total Sales Card'",
        "measure 'Total Orders Card'",
        "measure 'Total Customers Card'",
        "measure 'Total Products Card'",
        "measure 'Average Order Value Card'",
        "measure 'Sales (M)'",
    ]:
        assert required_term in model, f"Missing semantic-model rule: {required_term}"

    assert "#2F7F8F" in public_text, "Petroleum-blue report palette is missing"
    assert "#1267E8" not in public_text, "Legacy bright-blue report colour remains"
    for emoji in ["💰", "🛒", "👥", "📦", "📈"]:
        assert emoji not in public_text, f"Decorative emoji remains in the report: {emoji}"

    report = json.loads(
        (REPORT / "definition" / "report.json").read_text(encoding="utf-8")
    )
    registered = next(
        package
        for package in report["resourcePackages"]
        if package["name"] == "RegisteredResources"
    )
    expected_icons = {
        "kpi-sales.svg",
        "kpi-orders.svg",
        "kpi-customers.svg",
        "kpi-products.svg",
        "kpi-aov.svg",
    }
    registered_icons = {item["name"] for item in registered["items"]}
    assert expected_icons <= registered_icons, "KPI icon resources are incomplete"
    for icon in expected_icons:
        assert (REPORT / "StaticResources" / "RegisteredResources" / icon).exists()

    expected_icon_visuals = {
        "iconSalesBg",
        "iconOrdersBg",
        "iconCustomersBg",
        "iconProductsBg",
        "iconAovBg",
    }
    for name in expected_icon_visuals:
        assert visual_definitions[name]["visual"]["visualType"] == "image"
        assert visual_definitions[name]["position"]["width"] == 44
        assert visual_definitions[name]["position"]["height"] == 44
    assert not any(name.endswith("Sym") for name in visual_definitions), (
        "Legacy text-symbol icon overlays remain"
    )

    assert visual_definitions["chartProducts"]["position"]["height"] == 190
    assert visual_definitions["chartCustomers"]["position"]["height"] == 190
    assert visual_definitions["slicerCountry"]["position"]["height"] == 58
    assert visual_definitions["slicerMonth"]["position"]["height"] == 58

    print(f"PBIP validation passed: {len(visuals)} visuals within a {page_width}×{page_height} page")


if __name__ == "__main__":
    main()
