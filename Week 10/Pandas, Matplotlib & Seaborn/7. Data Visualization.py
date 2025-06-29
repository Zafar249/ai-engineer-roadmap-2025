from matplotlib import pyplot as plt
import pandas as pd 
import seaborn as sns

df_sales = pd.read_excel("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_as"
                         "sets\\8_matplotlib_seaborn\linechart.xlsx")

print(df_sales.head())

# # Plotting a line chart

# plt.figure(figsize=(12,4))  # Specifying the size of the figure: width, height

# plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge") # Specifying both axes
# plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="green", label="Dishwasher") 
# # Assigns green color to line
# plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="orange", label="Washing Machine")
# # Adds a label for the line in the legend

# plt.title("Product Sales")  # Adds a title to the chart
# plt.ylabel("Revenue (mln $)")  # Adds a y-label to the chart
# plt.xlabel("Financial Quarter")
# plt.legend()  # Adds a legend to the chart

# plt.show()

# # Plotting a pie chart

# total_sales = df_sales[["Fridge","Dishwasher","Washing Machine"]].sum() 
# # Sums total sales of each appliance across all quarters

# print(total_sales.index)  # Returns the index of the dataframe which are appliances

# plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", explode=(0.1,0,0), shadow=True,
#         startangle=140)  
# # Plots a pie chart using total sales as values and appliances as labels
# # Auto percentage show percentage of each slice to 1 d.p
# # Explode moves the first pie slice a bit away while the other two remain in their position
# # Applies a shadow effect to the pie slices and rotates pie by 140 degree.

# plt.show()

# # Plotting a bar chart

# df_sales.plot(kind="bar", x="Quarter")  # Plot a bar chart

# plt.xticks(rotation=45)  # Rotates labels on x-axis by 45 degrees

# df_sales2 = df_sales.set_index("Quarter")
# print(df_sales2.loc["Q1 2022"])

# df_sales2.plot(kind="bar")  # Plot a bar chart. Index is taken as default value

# plt.xticks(rotation=45)

# plt.show()

# # Plotting a histogram

# df_score = pd.read_excel("D:\\Codes\\ai-engineer-roadmap-2025\\Week 10\\chapter_3_"
#                          "assets\\8_matplotlib_seaborn\\histograms.xlsx")

# plt.hist(df_score["Exam_Score"])  # Plot a histogram of exam scores 
# plt.show()

# sns.histplot(df_score["Exam_Score"], kde=True) # Plot a histogram of exam scores using seaborn
# # kernel density estimator plots a line which gives an approximation of the histogram

# # sns.histplot(data=df_score, x="Exam_Score", kde=True) # Alternatively

# plt.xlabel("Score")
# plt.ylabel("Count")
# plt.title("Exam Scores")
# plt.show()

# Plotting a scatterplot

df = pd.read_excel("Week 10//chapter_3_assets//8_matplotlib_seaborn//scatter_plot.xlsx")

sns.scatterplot(data=df, x="area_square_ft", y="price")  # Plotting a scatterplot
plt.show()