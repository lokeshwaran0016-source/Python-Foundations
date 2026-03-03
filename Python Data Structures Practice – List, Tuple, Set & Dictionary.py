
# LIST


my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
print("Positive Index:", my_list[1])
print("Negative Index:", my_list[-1])
print("Slice:", my_list[1:4])

my_list.append(60)
my_list.insert(2, 25)
my_list.extend([70, 80])
my_list.remove(40)
my_list.pop(0)

print("Index of 30:", my_list.index(30))
print("Count of 20:", my_list.count(20))

my_list.sort()
print("Ascending:", my_list)

my_list.sort(reverse=True)
print("Descending:", my_list)

my_list.reverse()
print("Reversed:", my_list)



# TUPLE


my_tuple = (1, 2, 3, 4, 5)

print("Tuple:", my_tuple)
print("Positive Index:", my_tuple[1])
print("Negative Index:", my_tuple[-1])
print("Slice:", my_tuple[1:4])
print("Count of 2:", my_tuple.count(2))
print("Index of 3:", my_tuple.index(3))

tuple2 = (6, 7)
print("Concatenate:", my_tuple + tuple2)
print("Repeat:", my_tuple * 2)

tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list)

print("Length:", len(my_tuple))
print("Check 3 exists:", 3 in my_tuple)

nested_tuple = (1, (10, 20))
print("Nested Access:", nested_tuple[1][0])

for item in my_tuple:
    print("Loop:", item)



# SET


my_set = {1, 2, 3, 4, 5}

my_set.add(6)
my_set.remove(2)

set2 = {4, 5, 6, 7}

print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))
print("Difference:", my_set.difference(set2))
print("Symmetric Difference:", my_set.symmetric_difference(set2))

print("Subset:", my_set.issubset(set2))
print("Superset:", my_set.issuperset(set2))

copy_set = my_set.copy()
print("Copy:", copy_set)

for item in my_set:
    print("Set Loop:", item)

my_set.clear()
print("Cleared Set:", my_set)



# DICTIONARY


my_dict = {
    "name": "Lokesh",
    "age": 25,
    "city": "Chennai",
    "course": "Data Science",
    "marks": 85
}

print("Access Value:", my_dict["name"])

my_dict["email"] = "lokesh@gmail.com"
my_dict["age"] = 26

my_dict.pop("city")
my_dict.popitem()

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

print("Check key exists:", "name" in my_dict)

for key in my_dict:
    print("Key:", key)

for value in my_dict.values():
    print("Value:", value)

for item in my_dict.items():
    print("Item:", item)

copy_dict = my_dict.copy()
print("Copy Dictionary:", copy_dict)
