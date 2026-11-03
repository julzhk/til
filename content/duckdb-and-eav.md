Title: Investigation on Entity-Attribute-Value Stored Data and DuckDB
Date: 2025-01-18
Category: Developer
Tags: Python, Data

I have a project I'm contributing to that uses EAV to store _some_ of it's data, eg: there's a fixed set of fields that are stored in a 'core' table, and then there's an EAV table that stores
attributes added conveniently by the user (which we'll call EAV or 'custom attributes')

This works nicely for saving; but the trouble with this pattern is that making queries is a bit more tricky - If the data was entirely EAV or entirely 'core', there'd be a clear path to querying.  
However when it's mixed like this we can't do simple queries.

For instance: Say we want to: 'Sort all records by data stored in an EAV field'; or 'sort by a 'core' field with a filter on a
'custom attribute' one. Can be done, but all just a bit more complex.
It makes me think of the pitfalls of not respecting polymorphic consistency in OOP.

## DuckDB, Postgres, Dataframes and SQL

DuckDB allows us to pull data into a dataframe, join the disparate EAV fields together into a consistent representation and then do sql manipulations on that dataframe. Pretty simple turns out! so we
can
assemble
the data
into a consistent
representation and
then do
manipulations on it - eg
sorting and
filtering, searching, aggregation etc - in
DuckDB SQL.

All the
data is in
memory so it's fast;
all of the data is represented in a consistent way, so we can query on 'core' or 'EAV' data equally.

[Here's a repo of an investigation on this topic
](https://github.com/julzhk/duckdb-investigate/blob/main/duckdb-investigate.ipynb) - it has other fragments too - eg: Doing SQL on both a CSV and Postgres data source. So convenient!

## The code


```python
import pandas as pd
import duckdb

# Connect to the DuckDB database
con = duckdb.connect()

# Now attach the PostgreSQL database
con.execute("""
ATTACH 'dbname=testdb user=postgres port=5433 host=127.0.0.1' AS test_db (TYPE POSTGRES);
""")

# Load the core items table into a DataFrame
items_df = con.execute("SELECT * FROM test_db.items").fetch_df()

# Load the EAV table into another DataFrame
eav_df = con.execute(f"SELECT * FROM test_db.eav").fetch_df()

# Pivot the eav table to transform attributes into columns
pivoted_eav_df = eav_df.pivot(index='id', columns='attribute', values='attribute_value').reset_index()

# Merge the items DataFrame with the pivoted other DataFrame, using the 'id' column as key
merged_df = pd.merge(items_df, pivoted_eav_df, on='id', how='left')
# Remove NANs
merged_df = merged_df.where(pd.notnull(merged_df), None)

# Now we can do SQL queries on the merged DataFrame
sorted_df = merged_df.sort_values(by='colour')

complex_query = con.execute("SELECT * FROM sorted_df WHERE colour='blue' AND id > 100").fetch_df()

```

Of course, usual caveats apply regarding performance, memory, speeed. 

But my tests show on my laptop we can load millions of records with dozens of custom fields from the EAV tables, and do complex queries on  
them in a few seconds.
