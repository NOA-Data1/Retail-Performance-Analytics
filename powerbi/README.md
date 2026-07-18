# Power BI implementation

This folder contains the versioned assets required to rebuild and validate the Power BI report.

## Included implementation assets

- `power_query/FactSales.m` applies the documented cleaning contract and creates the fact table.
- `power_query/DimCustomer.m`, `DimProduct.m` and `DimCountry.m` create report dimensions.
- `dax/model_tables.dax` creates the marked date table.
- `dax/measures.dax` contains the reconciled report measures.
- `theme/retail-performance-theme.json` applies the approved visual system.
- `project/1Retail_Performance.pbip` opens the complete version-controlled report.

The standalone Power Query scripts are retained for rebuilding the documented star schema from scratch. In that workflow, create a text parameter named `SourceFilePath`, then create `FactSales` before the dimension queries because they reference it. The complete PBIP project uses the public workbook in this repository and does not depend on a local Windows path.

## Available assets

- `dax/measures.dax` — core measures with stable business definitions.
- `theme/retail-performance-theme.json` — report colours and typography.
- `../docs/DATA_MODEL.md` — semantic-model specification.
- `../docs/DASHBOARD_SPECIFICATION.md` — page layout and interaction rules.
- `../docs/METRIC_DEFINITIONS.md` — KPI contract and expected values.

## Open the report

Open this file in Power BI Desktop:

```text
powerbi/project/1Retail_Performance.pbip
```

The sibling report and semantic-model folders are included. On the first refresh, Power BI may request credentials for the public GitHub source. Select **Anonymous** access. The model downloads the original UCI workbook stored in this repository and applies the documented cleaning rules in Power Query.

After refresh, confirm the six executive values in `docs/METRIC_DEFINITIONS.md` before publishing or exporting the report.

## Build sequence

1. Load and clean the source in Power Query using the rules in `DATA_QUALITY.md`.
2. Build the star schema in `DATA_MODEL.md`.
3. Reconcile the six executive KPIs before adding visuals.
4. Import the JSON theme.
5. Add the DAX measures.
6. Build the three report pages in the documented order.
7. Validate filters, partial-period labels and market/product scope.
8. Refresh and save the complete PBIP project.
