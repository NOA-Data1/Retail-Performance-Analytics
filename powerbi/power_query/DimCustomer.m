let
    IdentifiedCustomers = Table.SelectRows(FactSales, each [CustomerID] <> null),
    SelectedColumns = Table.SelectColumns(IdentifiedCustomers, {"CustomerID"}),
    DistinctCustomers = Table.Distinct(SelectedColumns)
in
    DistinctCustomers
