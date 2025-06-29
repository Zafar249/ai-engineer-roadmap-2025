import pandas as pd
import numpy as np

df = pd.read_csv("Week 10\\chapter_3_assets\\4_handling_missing_data_fillna_dropna" \
"_interpolate\\weather_data.csv", parse_dates = ["day"])  # Day column will be converted to date

print(type(df.day[0]))

df.set_index("day", inplace=True)

# df.fillna(0, inplace=True)  # Replaces all null values with 0

# df.fillna({
#     "temperature":df.temperature.mean(),  # Assignes mean of temperature column to null values
#     "windspeed":df.windspeed.mean(),
#     "event": "No event"
# }, inplace=True)

# df.fillna(method="ffill", inplace=True)  
# # Forward fill assigns a null value the value of the previous row

# df.fillna(method="bfill", inplace=True)
# # Backward fill assigns a null value the value of the next row

# df.fillna(method="bfill", inplace=True, axis="columns")
# # Backward fill assigns a null value the value of the next column

# df.fillna(method="ffill", inplace=True, limit=1)
# # Assigns a null value the value of the previous row only once per non-null value

# df.interpolate(inplace=True) 
# # Fill null values by interpolating, taking average of next and previous rows

# df.dropna("any",inplace=True)  # Drops any rows with even a single null value

# df.dropna("all", inplace=True)  # Only drops rows where every value except the Index is null

# df.dropna(thresh=2, inplace=True)  # Only drops rows with less than 2 non-null values.

# print(df)

df.fillna({
    "temperature":-99999,
    "windspeed":-99999,
    "event":"no event"
}, inplace=True)

# df.replace(-99999, np.nan, inplace=True) 
# # Replaces all instances of the first value with the second value

# df.replace(to_replace=[-99999, -8888], value=np.nan, inplace=True)  
# # A list can also be passed in as the first value

# df.replace({
#     "temperature":-99999,
#     "windspeed":[-99999,-88888],
#     "event":"no event"
# }, value=np.nan, inplace=True)  # Similarly a dicitonary can also be passed in as the first value

df.replace({
    -99999:np.nan,
    -88888: np.nan,
    "no event": "Sunny"
}, inplace=True)  # Replaces all instances of the key with the value

# print(df)

df = pd.DataFrame({
    "score":["exceptional", "average", "good", "poor", "average", "exceptional"],
    "student":["Maarij", "Soman", "Ashmal", "Wasay", "Noor", "Yashal"]
})

df.replace(["poor", "average", "good", "exceptional"],[1,2,3,4], inplace=True)
print(df)

