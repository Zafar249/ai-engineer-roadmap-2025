import pandas as pd

df = pd.read_csv("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\6_group_by\\weather" \
"_by_cities.csv")

# print(df[df.city=="new york"].temperature.max())

# group_city = df.groupby("city") # Returns a dataframe object which is grouped by cities
# print(group_city)

# # For each city a dataframe object is created
# for city, data in group_city:
#     print("city:", city)
#     print(data.temperature.max())

# print(group_city.get_group("new york"))  # Returns the relevant dataframe

# print(group_city.max())  # Returns the max value for each integer column in each dataframe

# print(group_city.mean("Temperature"))  # Uses concept of split, apply and combine 

# print(group_city.min())  # Result is a single dataframe

# print(group_city.describe())  # Returns statistics for each dataframe

# print(group_city.size())  # Returns number of rows in each dataframe

def group(df, idx, col):  # dataframe, index, column
    # Locate the particular index in the specified column in the database
    if 80 <= df[col].loc[idx] <= 90:  # If value is between 80-90
        return "80-90"
    elif 50 <= df[col].loc[idx] <= 60:  # If value is between 50-60
        return "50-60"
    else:
        return "others"
    
group_temp = df.groupby(lambda idx: group(df, idx, "temperature"))  # Group the dataframe by temperature
for key, data in group_temp:
    print("key:",key)
    print(data)