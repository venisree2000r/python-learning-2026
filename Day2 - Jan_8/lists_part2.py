# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlists = []
newlists2 = []

for x in fruits:
    if "a" in x:
        newlists.append(x)

newlists2 = [x for x in fruits if "a" in x]

print(newlists)
print(newlists2)