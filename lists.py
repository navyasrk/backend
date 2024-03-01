users = ['navya', 'srija', 'nithya']

data = ['nithya', 32, True]

emptylist = []

print("nithya" in emptylist)

print(users[0])
print(users[-2])

print(users.index('navya'))

print(users[0:2])
print(users[1:])

print(len(users))

users.append('elsa')
print(users)


users += ['jason']
print(users)

users.extend(['robert', 'jimmy'])
print(users)

# users.extend(data)
# print(users)
users.insert(0, 'noddy')
print(users)

users[2:2] = ['eddy', 'alexa']
print(users)

users[1:3] = ['robert', 'oswald']
print(users)

users.remove('robert')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['Nithya']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 8, 5, 90]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# tuples

mytuple = tuple(('navya', 24, True))

othertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(othertuple))

newlist = list(mytuple)
newlist.append('sree')
newtuple = tuple(newlist)
print(newtuple)


(one, *two, hi) = othertuple
print(one)
print(two)
print(hi)

print(othertuple.count(2))
