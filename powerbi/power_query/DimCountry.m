let
    SelectedColumns = Table.SelectColumns(FactSales, {"Country"}),
    DistinctCountries = Table.Distinct(SelectedColumns),
    AddedMarketGroup = Table.AddColumn(
        DistinctCountries,
        "Market Group",
        each if [Country] = "United Kingdom" then "United Kingdom" else "International",
        type text
    )
in
    AddedMarketGroup
