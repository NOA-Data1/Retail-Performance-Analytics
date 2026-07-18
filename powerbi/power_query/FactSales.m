let
    Source = Excel.Workbook(File.Contents(SourceFilePath), null, true),
    OnlineRetailSheet = Source{[Item = "Online Retail", Kind = "Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(OnlineRetailSheet, [PromoteAllScalars = true]),
    TypedColumns = Table.TransformColumnTypes(
        PromotedHeaders,
        {
            {"InvoiceNo", type text},
            {"StockCode", type text},
            {"Description", type text},
            {"Quantity", Int64.Type},
            {"InvoiceDate", type datetime},
            {"UnitPrice", Currency.Type},
            {"CustomerID", Int64.Type},
            {"Country", type text}
        }
    ),
    RequiredDescriptions = Table.SelectRows(TypedColumns, each [Description] <> null),
    ExactDuplicatesRemoved = Table.Distinct(RequiredDescriptions),
    CompletedSales = Table.SelectRows(
        ExactDuplicatesRemoved,
        each [Quantity] > 0 and [UnitPrice] >= 0
    ),
    RenamedDateTime = Table.RenameColumns(CompletedSales, {{"InvoiceDate", "InvoiceDateTime"}}),
    AddedDateKey = Table.AddColumn(
        RenamedDateTime,
        "DateKey",
        each Date.From([InvoiceDateTime]),
        type date
    ),
    AddedLineSales = Table.AddColumn(
        AddedDateKey,
        "LineSales",
        each [Quantity] * [UnitPrice],
        Currency.Type
    )
in
    AddedLineSales
