# Python Lists

### Access list item by index
```
names = ['Han', 'Leia', 'Chewbacca']

print(names[0])
print(names[1])
print(names[2])
```

### List iteration
```
names = ['Han', 'Leia', 'Chewbacca']

# Here 'n' is name and we get its index.
for n in names :
    i = names.index(n)
    print(i, n)

# Here 'i' is index and we get its name.
for i in range(len(names)) :
    print(i, names[i])    
```

### Append item to list
```
names.append('R2-D2')
print(names)
```

### Delete item from list
```
names.pop(1)
print(names)
```

### Slice a list
```
names = ['Han', 'Leia', 'Chewbacca', 'Han', 'Leia', 'Chewbacca']

# Name 1 to 4
slice_01 = names[0:3]

# Name 5 to end
slice_02 = [4:len(names)-1]
```

### Remove duplicate items from list
```
dupes = ['Han', 'Leia', 'Chewbacca', 'Han', 'Leia', 'Chewbacca']
unique = []

for name in dupes : 
    if name not in unique :
        unique.append(name)

print(unique)
```
