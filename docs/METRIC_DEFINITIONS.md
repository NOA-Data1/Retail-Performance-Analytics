# Metric definitions

All executive KPIs use the cleaned completed-sales population unless stated otherwise.

| Metric | Business definition | Calculation | Verified result |
|---|---|---|---:|
| Sales | Revenue recorded on completed transaction lines | `SUM(Quantity × UnitPrice)` | £10,642,110.80 |
| Orders | Completed invoices represented in the analytical data | Distinct count of `InvoiceNo` | 20,134 |
| Identified customers | Customers with a non-null source identifier | Distinct count of non-null `CustomerID` | 4,339 |
| Products sold | Stock codes present in completed sales | Distinct count of `StockCode` | 3,925 |
| Average order value | Average completed-invoice revenue | Sales ÷ Orders | £528.56 |
| Countries | Transaction markets represented in completed sales | Distinct count of `Country` | 38 |
| Units sold | Units on completed transaction lines | Sum of `Quantity` | Calculated at refresh |
| UK sales share | Concentration of cleaned sales in the UK | UK sales ÷ Sales | 84.6% |
| Anonymous sales | Sales on rows without `CustomerID` | Sales where `CustomerID` is blank | £1,754,901.91 |
| Anonymous sales share | Share of revenue not attributable to a customer | Anonymous sales ÷ Sales | 16.5% |

## Scope rules

- Company sales include anonymous completed transactions.
- Customer KPIs and rankings exclude rows with missing `CustomerID`.
- Merchandise rankings exclude operational charges only when the visual explicitly states this rule.
- December 2011 must be marked as a partial period.
- Currency is GBP because the source records `UnitPrice` in sterling.

## Display standards

- Sales: `£0.00M` for executive cards and `£#,##0` in detail tables.
- Counts: whole numbers with thousands separators.
- Average order value: `£#,##0.00`.
- Shares and changes: `0.0%`.
- Month labels: `MMM yyyy` and sorted by the underlying month-start date.
