from collections import Counter

# ## Exercise: Python Read Write File
# 1. [poem.txt] contains famous poem "Road not taken" by poet Robert Frost. 
#    You have to read this file in your python program and find out words with maximum occurance.

# file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 2\\poem.txt", "r")
# words = file.read().split(" ")
# count = Counter(words) # Count the occurrences of each element in words
# print(count.most_common(1)) # Print the most common word in count
# file.close()

file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 2\\poem.txt", "r")
words = file.read().split(" ")
count = {}
for i in range(len(words)):
    word = words[i].lower()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
max = 0
word = ""
occurrances = list(count.values())
for key,val in count.items():
    if val > max:
        max = val
        word = key
print(f"The word '{word}' occurs a total of {max} times.")

file.close()


# 2. [stocks.csv] contains stock price, earnings per share and book value. 
# You are writing a stock market application that will process this file and create a new file
# with financial metrics such as pe ratio and price to book ratio. These are calculated as,

# pe ratio = price / earnings per share
# price to book ratio = price / book value



# Your input format (stocks.csv) is,

# |Company Name|Price|Earnings Per Share|Book Value|
# |-------|----------|-------|----------|
# |Reliance|1467|66|653|
# |Tata Steel|391|89|572|

# Output.csv should look like this,

# |Company Name|PE Ratio|PB Ratio|
# |-------|----------|-------|
# |Reliance|22.23|2.25|
# |Tata Steel|4.39|0.68|

file = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 2\\stocks.csv", "r")
file.readline()
file2 = open("D:\\Codes\\ai-engineer-roadmap-2025\\Week 2\\output.csv","w")
file2.write("Company Name,PE Ratio,PB Ratio\n")
for line in file:
    name, price, earning, book_value = line.strip().split(",")
    pe_ratio = round(int(price) / int(earning), 2)
    pb_ratio = round(int(price) / int(book_value), 2)
    file2.write(f"{name},{pe_ratio},{pb_ratio}\n")
    
file.close()
file2.close()
