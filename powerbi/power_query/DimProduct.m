let
    ProductRows = Table.SelectColumns(
        FactSales,
        {"StockCode", "Description", "InvoiceDateTime"}
    ),
    GroupedProducts = Table.Group(
        ProductRows,
        {"StockCode"},
        {{"Product Rows", each _, type table [StockCode = text, Description = text, InvoiceDateTime = datetime]}}
    ),
    AddedCanonicalDescription = Table.AddColumn(
        GroupedProducts,
        "Description",
        each
            let
                DescriptionUsage = Table.Group(
                    [Product Rows],
                    {"Description"},
                    {
                        {"Usage", each Table.RowCount(_), Int64.Type},
                        {"Last Sale", each List.Max([InvoiceDateTime]), type datetime}
                    }
                ),
                RankedDescriptions = Table.Sort(
                    DescriptionUsage,
                    {{"Usage", Order.Descending}, {"Last Sale", Order.Descending}, {"Description", Order.Ascending}}
                )
            in
                RankedDescriptions{0}[Description],
        type text
    ),
    AddedProductClass = Table.AddColumn(
        AddedCanonicalDescription,
        "ProductClass",
        each if List.Contains({"DOT", "POST", "M", "m"}, [StockCode])
            then "Operational charge"
            else "Merchandise",
        type text
    ),
    RemovedNestedRows = Table.RemoveColumns(AddedProductClass, {"Product Rows"})
in
    RemovedNestedRows
