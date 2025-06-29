import pandas as pd

file = "D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\3_read_write_to_excel\\" \
    "stock_data.csv"

# df = pd.read_csv(file, skiprows=1)  # Reads the file from the 2nd row

# df = pd.read_csv(file, header=1, names=["stock_symbol","eps","revenue","price","people"]) 
# # The 2nd row is treated as the header
# # names allows you to specify custom column names.

# df = pd.read_csv(file, header=1, nrows=2)  # Reads only 2 rows.

# df = pd.read_csv(file, header=1,na_values={
#     "eps":["not available"], "revenue":[-1], "price":["n.a."], "people":["n.a."]  
# })  # na_values decides what values in which columns are treated as N/A values

# df = pd.read_csv(file, header=1, na_values=["not available",-1,"n.a."])
# # na_values looks for the values provided in the list across all columns and treats them as N/A values.

# # Calculates a new column: price to earning ratio.
# df["pe"] = df["price"] / df["eps"]
# print(df)

# df.to_csv("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\Pandas\\pe.csv", index=False, header=False)  
# # Exports the data frame to a csv file with no index and no header


file = "D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\3_read_write_to_excel\\movies_db.xlsx"

def standardize_currency(curr):
    if curr == "$$" or curr=="Dollars":  # Standardizing the currency into USD
        return "USD"
    return curr # For currencies other than USD
    
# Read the movies sheet in the excel file
df_movies = pd.read_excel(file, "movies")

print(df_movies)

df_financials = pd.read_excel(file, "financials", )

print(df_financials)

# Read the financials sheet in the excel file and standardize the currencies
df_financials = pd.read_excel(file, "financials", converters=
                              {"currency": standardize_currency})

print(df_financials)

# Merges two data frames based on the movie_id column
df_merged = pd.merge(df_movies, df_financials, on="movie_id")  
print(df_merged)

df_merged.to_excel("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\Pandas\\movies_merged.xlsx", 
                   sheet_name="merged", index=False)
# Exports the merged data frames as an excel file with no index

df_stocks = pd.DataFrame({
    'tickers':["GOOGL","WMT"],
    'price':[845,65],
    'pe':[30.37,14.26],
    'eps':[27.82, 4.61]
})  # Data frames can be created using dictionaries

df_weather = pd.DataFrame({
    "day":['1/1/2017',"2/1/2017"],
    "temperature":[32,35],
    "event":["Rainy", "Sunny"]
})

# Create an excel file and write the data frames as seperate sheets to the file.
with pd.ExcelWriter("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\Pandas\\stocks_weather.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name="Stocks")  # Export the stocks data frame with sheet name Stocks
    df_weather.to_excel(writer, sheet_name="Weather")