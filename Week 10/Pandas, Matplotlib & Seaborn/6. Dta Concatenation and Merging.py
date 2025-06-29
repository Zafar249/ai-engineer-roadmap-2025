import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})

# df = pd.concat([india_weather, us_weather], ignore_index=True)
# # Concatenates multiple data frames together. It will create an index for the data frame on its own.

# df = pd.concat([india_weather, us_weather], keys=["India","USA"])
# # Creates seperate keys for each data frame. Acts like a hashmap
# print(df)

# print(df.loc["USA"])  # Returns all american cities

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])  # Each city should have the same index in both dataframes.

# df = pd.concat([temperature_df, windspeed_df], axis=1)
# # Concatenates multiple data frames together using columns

# print(df)

# df1 = pd.DataFrame({
#     "city": ["new york","chicago","orlando"],
#     "temperature": [21,14,35],
# })

# df2 = pd.DataFrame({
#     "city": ["chicago","new york","orlando"],
#     "humidity": [65,68,75],
# })

# df = pd.merge(df1,df2, on="city")  # Merges two data frames together using the city column
# print(df)

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})

df = pd.merge(df1, df2, on="city", how="left") # Merges two data frames together using left join

df = pd.merge(df1, df2, on="city", how="right")

df = pd.merge(df1, df2, on="city", how="outer")  # Fully merges two data frames together

print(df)