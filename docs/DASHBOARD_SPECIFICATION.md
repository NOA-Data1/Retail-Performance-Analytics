# Dashboard specification

## Design direction

The report uses a restrained blue visual system inspired by the supplied concept image. The design should feel operational and executive rather than decorative.

Core colours:

- Primary blue: `#1267E8`
- Dark navy: `#121A30`
- Secondary blue: `#2D7FF0`
- Positive green: `#169B62`
- Warning amber: `#E59F24`
- Light background: `#F7F9FC`
- Card background: `#FFFFFF`
- Border: `#DDE4EE`

## Page 1 — Executive Overview

### Header

- Title: `Retail Performance Analytics`
- Subtitle: `Executive Overview`
- Source period: `Dec 2010 – Dec 2011`
- Status note: `Dec 2011 is a partial month`
- Dataset scope: `525,460 analytical rows · 38 countries`

### KPI row

1. Sales — £10.64M
2. Orders — 20,134
3. Identified customers — 4,339
4. Products sold — 3,925
5. Average order value — £528.56

Do not show “100% of total” beneath every KPI. It communicates no comparison and creates visual noise. Use subtitles only when they add context, such as `completed orders` or `identified customers`.

### Main visuals

1. Monthly sales trend
   - chronological `MMM yyyy` axis;
   - November 2011 peak annotation;
   - December 2011 marked as partial;
   - tooltip includes sales, orders and average order value.

2. Market contribution
   - KPI or callout for UK sales share;
   - horizontal bar chart titled `Top international markets by sales`;
   - UK excluded from this chart and stated in the subtitle;
   - no scroll bar in the default top-ten view.

3. Customer and product highlights
   - top five customers by sales;
   - top five merchandise products by sales;
   - operational charges excluded from the merchandise visual.

### Filters

- Country
- Month
- Product classification

Filters belong in a narrow top or left panel. They must not consume the full page width beneath the analysis.

## Page 2 — Customer & Product Analysis

### Customer section

- customer sales ranking;
- orders;
- average order value;
- share of identified-customer sales;
- anonymous sales shown separately, never assigned to a customer.

### Product section

- merchandise ranking;
- quantity sold;
- sales;
- order penetration;
- operational charges shown in a separate table or toggle.

## Page 3 — Data Quality & Definitions

- source-to-cleaned row reconciliation;
- missing customer volume and sales;
- zero-price rows;
- cancellation and adjustment exclusions;
- partial-period warning;
- complete KPI definition table.

## Interaction rules

- Country filters every applicable visual.
- Month filters all pages through synced slicers.
- Selecting a customer must not filter product visuals unless that interaction is intentionally enabled and documented.
- Use report-page tooltips for detail instead of adding labels to every point.
- Disable visual interactions that create misleading partial totals.

## Accessibility and formatting

- Minimum 4.5:1 contrast for body text.
- Do not rely on colour alone to identify the partial month.
- Use concise English titles and consistent sentence case.
- Keep currency in GBP across cards, axes and tooltips.
- Avoid emoji inside KPI cards; use simple line icons only if they remain legible.
- Avoid scroll bars on the executive page.

## Final acceptance checks

- Every KPI reconciles to `METRIC_DEFINITIONS.md`.
- December 2011 is visibly marked as partial.
- UK inclusion or exclusion is explicit on every country visual.
- Customer totals exclude blank IDs while sales totals retain anonymous sales.
- Product rankings state whether operational charges are included.
- No visual is clipped at 16:9 desktop view.
- Slicer selections can be reset through a visible button.
