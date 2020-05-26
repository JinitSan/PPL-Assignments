l = []
def takelist():
    for i in range(int(input("Enter starting page ")), int(input("Enter ending page(not included) "))):
        l.append(i)
    if input("If you're done entering pages, press E, else press anything else ")=='E':
        return 
    else:
        takelist()
takelist()
for i in range(1,26):
    if i not in l:
        print(i)
