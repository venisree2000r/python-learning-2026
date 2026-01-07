# Lists is mutable
## Access List Items
nums = [25,36,87,90,4]
print(nums)
print(nums[3:])
print(nums[:-1])
print(nums[::-1])

names = ['veni', 'sree', 25, 5.0]
print(names)
print(names[::-1])

## Add List Items
nums.append(500)
names.append('Tamil Nadu')
print(nums)
print(names)

mixed_lists = [names, nums]
print(mixed_lists)

## Change List Items
colors = ['White', 'Black']
# Change Item Value
colors[1] = 'Green'
print(colors)



