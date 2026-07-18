# Power BI implementation

This folder contains the versioned assets required to rebuild and validate the Power BI report.

## Included implementation assets

- `power_query/FactSales.m` applies the documented cleaning contract and creates the fact table.
- `power_query/DimCustomer.m`, `DimProduct.m` and `DimCountry.m` create report dimensions.
- `dax/model_tables.dax` creates the marked date table.
- `dax/measures.dax` contains the reconciled report measures.
- `theme/retail-performance-theme.json` applies the approved visual system.

Create a text parameter named `SourceFilePath` containing the local path to `Online Retail.xlsx`, then paste each Power Query script into a query with the matching name. Create `FactSales` before the dimension queries because they reference it.

## Available assets

- `dax/measures.dax` — core measures with stable business definitions.
- `theme/retail-performance-theme.json` — report colours and typography.
- `../docs/DATA_MODEL.md` — semantic-model specification.
- `../docs/DASHBOARD_SPECIFICATION.md` — page layout and interaction rules.
- `../docs/METRIC_DEFINITIONS.md` — KPI contract and expected values.

## PBIP requirement

A `.pbip` file is only the project pointer. A complete Power BI Project must include the sibling report and semantic-model folders, normally similar to:

```text
Retail_Performance.pbip
Retail_Performance.Report/
Retail_Performance.SemanticModel/
```

The report cannot be edited or versioned from the pointer alone. Export the report using **File → Save as → Power BI Project (.pbip)** and provide the complete containing folder.

## Build sequence

1. Load and clean the source in Power Query using the rules in `DATA_QUALITY.md`.
2. Build the star schema in `DATA_MODEL.md`.
3. Reconcile the six executive KPIs before adding visuals.
4. Import the JSON theme.
5. Add the DAX measures.
6. Build the three report pages in the documented order.
7. Validate filters, partial-period labels and market/product scope.
8. Save the complete PBIP folder to this repository.
