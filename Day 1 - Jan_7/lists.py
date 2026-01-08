# Lists is mutable
############# Access List Items #############
nums = [25,36,87,90,4]
print(nums)
print(nums[3:])
print(nums[:-1])
print(nums[::-1])

names = ['veni', 'sree', 25, 5.0]
print(names)
print(names[::-1])

############# Add List Items #############
nums.append(500)
names.append('Tamil Nadu')
print(nums)
print(names)

mixed_lists = [names, nums]
print(mixed_lists)

nums.extend([1,2,3,4])
print(nums)
## Change List Items
colors = ['White', 'Black']
# Change Item Value
colors[1] = 'Green'
colors.insert(2,'yellow')
print(colors)

############# Remove List Items ###############
# 1. Remove specific item
colors.remove("White")
print(colors)
# 2. Remove specific index
colors.pop()
print(colors)
# 3. del keyword
del colors
# 4. clear the list
colors2 = ['White', 'Black']
colors2.clear()
print(colors2)

############# Loop lists #############
# 1.Loop Through a List
my_lists = ["apple", "orange", "grapes", "carrot", "pineapple"]
print(my_lists)
for x in my_lists:
    print(x)
# 2.Loop Through the Index Numbers
for i in range(len(my_lists)):
    print(i, "=", my_lists[i])

print(min(nums))
print(max(nums))
nums2 = [25,36,87,90,4]
nums2.sort()
print(nums2)

#task
name = "Lists"
print(name[-3])