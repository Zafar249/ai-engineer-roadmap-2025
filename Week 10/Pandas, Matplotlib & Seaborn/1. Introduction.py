# import csv

# def calculate_rating_stats(data, industry=None):
#     ratings = []
#     for row in data:
#         if row[3] != "NULL" and (row[1] == industry or not industry):
#             ratings.append(float(row[3]))
#     max_rating = max(ratings)
#     min_rating = min(ratings)
#     avg_rating = sum(ratings) / len(ratings)
#     return max_rating, min_rating, avg_rating
# file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\1_intro\\movies.csv")
# data = list(csv.reader(file))  # Read file data, stored in csv format, and convert it into an array
# print(data)  # Every element is a row in the csv file

# header = data[0]
# data = data[1:]
# print(calculate_rating_stats(data))

import pandas as pd

# Read csv file
df = pd.read_csv("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_assets\\1_intro\\movies.csv")

# print(df)  # Data frame object, has a tabular structure with rows and columns

# print(df.head(2)) # Prints top 2 rows
# # Note: If df.head() is empty, it prints top 5 rows

# print(df.tail(3)) # Prints bottom 3 rows
# # Note: If df.tail() is empty, it prints bottom 5 rows

# print(df.sample(4))  # Randomly prints 4 rows

# # Data frames have similar properties and Indexing compared to numpy arrays and python lists.
# print(df.shape)
# print(df[2:6])

# print(df["imdb_rating"])  # df.imfb_rating returns same results

# print(type(df.imdb_rating))  # The column in a data frame is called series.

# print(dir(df.imdb_rating)) # Returns a list of all the properties and functions applicable on the series.

print(df.imdb_rating.min(), df.imdb_rating.max(), df.imdb_rating.mean())

print(df[df.industry=="Bollywood"])  # Returns a list of all Bollywood Movies

df_b = df[df.industry=="Bollywood"]
df_h = df[df.industry=="Hollywood"]

print(df_b.imdb_rating.min(), df_b.imdb_rating.max(), df_b.imdb_rating.mean())

print(df_h.imdb_rating.min(), df_h.imdb_rating.max(), df_h.imdb_rating.mean())