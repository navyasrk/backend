# Dictionaries
band = {
    "vocals": "plant",
    "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values

print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "MPM"})
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)


print(band.popitem())  # tuple
print(band)

# delete and clear
band["drums"] = "bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries(not a way to create copy)
# band2 = band  #create a ref(same dictionary)
# print("bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "navya"
# print(band)

band2 = band.copy()
band2["drums"] = "navya"
print("good copy")
print(band)
print(band2)


# or use the dict() constructor fun
band3 = dict(band)
print("goodcopy")
print(band3)

# nested dictionaries
member1 = {
    "name": "plant",
    "instrument": "guitar"
}
member2 = {
    "name": "page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

#sets(data collection type)

nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicate allowed
nums = {1, 2, 2, 4}
print(nums)


#true is a dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#add a new value element to a set
nums.add(8)
print(nums)

#add elements from 1 set to other
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

#you can use update with lists, tuples, and dictionaries, too.

#merge 2 sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

newset = one.union(two)
print(newset)

#keep duplicates fron 2 diff sets
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

#keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
