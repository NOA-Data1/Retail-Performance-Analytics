# Data quality and analytical scope

## Source

The UCI Online Retail workbook contains 541,909 transaction lines recorded between 1 December 2010 and 9 December 2011. Each row represents one invoice line, not one complete order.

## Verified source profile

| Check | Result |
|---|---:|
| Source rows | 541,909 |
| Columns | 8 |
| Exact duplicate rows | 5,268 |
| Missing descriptions | 1,454 |
| Missing customer IDs | 135,080 |
| Cancelled invoice rows | 9,288 |
| Negative-quantity rows | 10,624 |
| Negative-price rows | 2 |
| Zero-price rows | 2,515 |

## Completed-sales population

The final analytical population follows the cleaning decisions recorded in notebook 02:

1. Remove rows with missing `Description`.
2. Remove exact duplicate rows.
3. Retain only rows where `Quantity > 0`.
4. Retain rows where `UnitPrice >= 0`.

The resulting dataset contains **525,460 rows**.

## Why missing customers remain

Missing `CustomerID` does not invalidate a completed sale. Removing those rows would remove £1,754,901.91 from the company-level sales result. They therefore remain in sales, order, product, country and time analysis, but are excluded from customer-level counts and rankings.

## Why zero-price rows remain

After the principal cleaning rules, 582 rows have a zero price. They contribute £0 to sales and are retained so that the cleaning process does not silently classify every non-revenue movement as invalid. They should be monitored separately in the data-quality page.

## Partial period

The source ends on 9 December 2011. December 2011 is not comparable with complete months. The report must either:

- label it as a partial month; or
- exclude it from complete-month comparisons while keeping it visible in the data-quality view.

It must not be described as a confirmed decline.

## Product-ranking rule

Operational charges such as `DOTCOM POSTAGE`, `POSTAGE` and `Manual` are valid revenue lines but not merchandise. They remain in total sales and are excluded only from rankings labelled as physical-product or merchandise performance.

## Reconciliation controls

Every refresh must confirm:

- 525,460 analytical rows;
- £10,642,110.80 total sales;
- 20,134 distinct completed orders;
- 4,339 identified customers;
- 3,925 sold stock codes;
- 38 countries;
- £528.56 average order value.

Any change requires an explicit source or rule explanation before the dashboard is published.
