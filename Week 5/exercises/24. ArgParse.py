import argparse
# parsing: analyze a string or text into logical components 

if __name__ == "__main__":
    parser = argparse.ArgumentParser() # Creates a parser object
    # It stores all the information to be passed from the command line

    # parser.add_argument("cs", help="computer science")  
    # # Positional Argument. Order of argument does matter

    parser.add_argument("--physics",help="physics") # Optional Argument. Order of argument doesn't matter
    parser.add_argument("--maths", help="maths")
    parser.add_argument("--chemistry", help="chemistry")

    parser.add_argument("--subjects", help="subjects", choices=["maths","physics", "chemistry"])
    # add_argument(name(name of argument) , help(message to give to user) , choice=[])
    # choice ensures program will only take one of the specified arguments
    
    args = parser.parse_args()  # Parses the arguments

    math = args.maths  # maths is an attribute of args
    physics = args.physics
    chemistry = args.chemistry

    average = int(math) + int(physics) + int(chemistry)
    average /= 3
    print(average)