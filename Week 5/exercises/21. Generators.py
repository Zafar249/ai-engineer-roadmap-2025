# ## Exercise: Generators

# 1. Print Square Sequence using yield

# Create Generator method such that every time it will returns a next square number

# for exmaple : 1 4 9 16 ..

def Square():  # Defining the generator
    num = 1
    while True:
        yield num ** 2  # Returns the square of num but continues execution of program
        num += 1


itr = iter(Square())  # Create an iterator of Square
print(itr.__next__())
print(itr.__next__())

for sq in Square():
    if sq < 1000:
        print(sq)
    else:
        break

     



