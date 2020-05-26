
#exception handling for a function ask(), if a number is not input, the function asks the user again
def ask():
    while True:
        p1=(input("Enter a number\n"))
        try:
            print(int(p1)**2)
            
        except:
            print("Character entered is not a number, try again\n")
        else:
            print("All done")
            break

ask()
#Raising exceptions for file handling, if the file is not found in the given directory
try:
    filename = input("Enter a filename: ")
    if filename == "":
        raise NameError

    with open(filename, "r") as f:
        for line in f.readlines():
            print(line, end="")

    # f = open(filename, "r")
    # lines = f.readlines()
    # for line in lines:
    #     print(line, end="")
    # f.close()

except FileNotFoundError:           # when using `with` to open file
    print("File does not exist!")
except OSError as e:                # when opening file directly
    print("File does not exist!")
except NameError as e:
    print("File name cannot be empty!")
finally:
    print("Done with files...")
