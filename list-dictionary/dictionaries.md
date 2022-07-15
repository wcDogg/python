# Python Dictionaries

### Access value by key
```
nato = {"A": "Alfa", "B": "Bravo", "C": "Charlie"}

print(nato['A'])
print(nato['B'])
print(nato['C'])


def dict_val_from_key(d, k):
    '''Find the value of a given key. Returns (k,v) tuple or None.
    '''
    if type(d) is not dict:
        print('First argument must be a dictionary.')
        return

    if k not in d.keys(): 
        print('%s is not a key in this dictionary.' % k)
        return
    
    return (k, d[k])

# Use
result = dict_val_from_key(nato, 'X')
print(result)

# Unpack Tuples
key, value = result
print(key)
print(value)
```

### Add or update key pair
```
nato['X'] = 'Xray'
print(nato)
```

### Boolean membership check using views
```
nato = {"A": "Alfa", "B": "Bravo", "C": "Charlie"}

# Does a key exist? True
"A" in nato.keys()

# Does a value exist? True
"Alfa" in nato.values()

# Does pair exist? True
("A", "Alfa") in nato.items()
```

### List all keys with same value
```
results = {'file_01':'processed',
          'file_02':'processed',
          'file_03':'skipped',
          'file_04':'error',
          'file_05':'processed',
          'file_06': 'skipped',
          'file_07': ''}

def dict_key_from_val(d, v):
    '''Returns all keys that store given value 
    as a list of (k,v) tuples.
    '''
    if type(d) is not dict:
        print('First argument must be a dictionary')
        return
    
    if v not in d.values(): 
        print('%s is not a value in this dictionary' % v)
        return
    
    tuples = []
    
    for key, value in d.items():
        if value == v:
            tuples.append((key, value))
          
    return tuples

# Use
error = dict_key_from_val(results, 'error')
print(error)

processed = dict_key_from_val(results, 'processed')
print(processed)
```

### Count keys with same value
```
results = {'file_01':'processed',
          'file_02':'processed',
          'file_03':'skipped',
          'file_04':'error',
          'file_05':'processed',
          'file_06': 'skipped',
          'file_07': ''}

def count_dict_vals(d):
    '''Counts the number of keys that store
    known values: processed, skipped, error. Returns dict.
    '''
    if type(d) is not dict:
        print('d is not a dictionary')
        return
    
    r = {
        'files_total': len(d),
        'files_processed': 0,
        'files_skipped': 0,
        'files_error': 0,
        'files_other': 0
    }

    for k in d:
        if d[k] == 'processed':
            r['files_processed'] +=1
        elif d[k] == 'skipped':
            r['files_skipped'] +=1
        elif d[k] == 'error':
            r['files_error'] +=1
        else:
            r['files_other'] +=1
    
    return r

# Use
results_summary = count_dict_vals(results)
print(results_summary)
```

### Update existing key - prevent new key
```
nato = {"A": "Alfa", "B": "Bravo", "C": "Charlie"}

def dict_update_key(d, kv_tuple):
    '''Updates an existing dictionary key. Prevents
    new pairs from being created if key does not exist.
    '''
    if type(d) is not dict:
        print('First argument must be a dictionary')
        return   
    
    if type(kv_tuple) is not tuple or len(kv_tuple) != 2:
        print('Second argument must be a (k,v) tuple')
        return
    
    k,v = kv_tuple
    
    if k not in d.keys(): 
        print('%s is not a key in this dictionary' % k)
        return
     
    d[k] = v

# Use
dict_update_key(nato,('E', 'Echo'))
print(nato)
```

### Delete pair by key
```
nato = {"A": "Alfa", "B": "Bravo", "C": "Charlie"}

def dict_delete_key(d, k):
    '''Deletes the given dictionary key.
    '''
    if type(d) is not dict:
        print('First argument must be a dictionary')
        return
    
    if k not in d.keys(): 
        print('%s is not a key in this dictionary' % k)
        return    
    
    d.pop(k)
    print('%s deleted' % k)

# Use
dict_delete_key(nato, 'E')
print(nato)
```

### Sort by key
```
nato = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'Z': 'Zulu', 'T': 'Yellow', 'X': 'Xray'}

def dict_sort_by_key(d):
    '''Sorts given dictionary by key. Returns new dict.
    '''
    if type(d) is not dict:
        print('Argument must be a dictionary')
        return
    
    return {k: d[k] for k in sorted(d)}

# Use
by_key = dict_sort_by_key(nato)
print(by_key)
```

### Sort by value
```
nato = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'Z': 'Zulu', 'T': 'Yellow', 'X': 'Xray'}

def dict_sort_by_value(d):
    '''Sorts given dictionary by value. Returns new dict.
    '''
    if type(d) is not dict :
        print('Argument must be a dictionary')
        return
    
    from operator import itemgetter
    return {k:v for k,v in sorted(d.items(), key=itemgetter(1))}

# Use
# Sort by value
by_value = dict_sort_by_value(nato)
print(by_value)
```

## Nested Dictionaries
```
person = {
    "screenname": 'mcPython',
    "name": {
        "first": "Sam",
        "last": "Jones"},
    "address": {
        "street": "67 Python Street",
        "city": "Philadelphia",
        "state": "PA"},
    }
```

### Access values
```
# Get a key's value
print(person['name']['first'])
print(person['address']['city'])
```

### Update a value
```
person['address']['city'] = 'Atlanta'
person['address']['state'] = 'GA'

print(person['address']['city'])
print(person['address']['state'])
```

### Get a value's data type
```
def dict_key_val_is_type(k):
    '''For a given key, returns the type of value stored.
    '''    
    return type(k)

# Use
dict_key_val_is_type(person['name'])
dict_key_val_is_type(person['name']['first'])
```

### Iteration
```
# Parent keys
for k in person:
    print(k, person[k])

# Child keys
for k in person: 
    if type(person[k]) != dict:
        print(k, person[k])
    else:
        for kx in person[k]:
            print(kx, person[k][kx])
```

## List of dictionaries
```
alphabet = [
    {"letter": "a", "call": "alpha"},
    {"letter": "b", "call": "bravo"},
    {"letter": "c", "call": "charlie"}
]
```

### Append dictionary to list
```
new = {"letter":"d", "call": "delta"}
alphabet.append(new)
```

### Iteration
```
# The dictionaries
for d in alphabet:
    print(d)

# Since lists are ordered, each dict has an index. 
for d in range(len(alphabet)): 
    print(d, alphabet[d])
```
