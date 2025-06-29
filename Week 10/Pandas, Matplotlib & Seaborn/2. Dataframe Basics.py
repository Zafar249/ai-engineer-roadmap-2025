import pandas as pd

df = pd.read_csv("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\1_intro\\movies.csv")

# print(df.shape)
# print(df.columns)

# print(df.industry.unique())  # Returns all unique industries
# print(df["language"].unique())  # Returns all unique langauges

# print(df.industry.value_counts())  # Returns the count of each unique industry in the dataframe
# print(df["language"].value_counts()) 

# print(df[["title","imdb_rating","industry"]])  # Returns a subset of the data frame

# df_new = df[["title","imdb_rating","industry"]]

# # Returns all movies released between 2000 and 2010
# print(df[(df.release_year > 2000) & (df.release_year < 2010)])  

# print(df[df.studio=="Marvel Studios"])  # Returns all movies produced by Marvel Studios

print(df.describe())  # Shows statistics for all numeric columns

print(df.info())  # Shows information about all the columns and the dataframe

print(df[(df.imdb_rating==df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])  
# Returns the movie with the highest and lowest imdb rating.

df["age"] = df["release_year"].apply(lambda x: 2025 - x) # x is the release year of the movie
# Subtracts the release year from the current year and applies the transformation to the release year
# column and adds it as a new column, age,  to the data frame
print(df.head())

df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1)  # x is a row of the dataframe
print(df.head())

print(df.index)

df.set_index("title", inplace=True)  # Modifies the original dataframe and sets title as the index
print(df.index)

print(df.loc["The Dark Knight"])  # Locates the index and returns the entire row

print(df.loc[["The Dark Knight", "PK"]])

print(df.iloc[0])  # Locates the integer based index and returns the entire row

df.reset_index(inplace=True) # Modifies the original frame and adds an integer based index