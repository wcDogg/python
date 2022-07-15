import listdata

# -----------------------------------------
# Common list operations
# -----------------------------------------

def is_empty(list):
  ''' Returns `True` if a list is empty.
  Returns `False` if a list has one or more items.
  '''
  return len(list) == 0

def item_count(list, item):
  ''' Uses `count()` to:  
  * Count the number of times an item appears in a list.
  * Count the number of times a character appears in a string.
  * Does NOT count the number of times a number appears in a number
  * Returns the count if value exists.
  * Returns `False` if item is not found or error occurs.
  '''
  try: 
    c = list.count(item)
    print ('Item: %s : Count: %s' % (item,c))
    return c
  except Exception as e:
    print('Item: %s : Count: False : %s' % (item,e))
    return False

def item_find(list,item): 
  ''' Uses the `in` operator to determine if a item is in a list. 
  * Returns an `(index, value)` tuple if value is found.
  * Returns `None` if value is not found. 
  * Linear runtime. Constanst space.  
  '''
  if item in list:
    i = list.index(item)
    print('Item found : [%s] %s' % (i,item))
    return i, list[i]
  else:
    print('Item not found : %s' % item)
    return None

def item_insert(list,index,item): 
  ''' Uses `insert()` to place an item 
  into a list before the given index.
  * Returns bool indicating operation was successful.
  * If index >= range, inserts item at end of list. 
  * Linear runtime. Amortized constant space.
  '''
  try: 
    list.insert(index,item)
    print('Item inserted : [%s] %s' % (index,item))
    return True
  except Exception as e:
    print('Item not inserted : [%s] %s : %s' % (index,item,e))
    return False

def item_append(list,item):
  ''' Uses `append()` to concatenate an item to the end of a list.
  * Returns bool indicating operation was successful. 
  * Constant runtime. Amortized constant space.
  '''
  try: 
    list.append(item)
    print('Item appended : %s' % item)
    return True
  except Exception as e:
    print('Item not appended : %s' % e)
    return False

def item_extend(list,item):
  ''' Uses `extend()` to extend the end of a list 
  with a list or string.
  * Each character in a string becomes an item - 
  i.e. `'cat'` becomes `[...'c','a','t']`.
  * Does NOT extend list with tuple.
  * Does NOT extend list with number. 
  * Returns bool indicating operation was successful. 
  * Constant runtime. Amortized constant space.
  '''
  try: 
    list.extend(item)
    print('Item extended : %s' % item)
    return True
  except Exception as e:
    print('Item not extended : %s' % e)
    return False

def item_remove(list,item):
  ''' Uses `remove()` to delete the first
  instance of an item from a list. 
  * If there are duplicate values, only the first is removed.
  * Returns bool indicating operation was successful. 
  * Linear runtime. Amortized constant space.
  '''
  try: 
    list.remove(item)
    print('Item removed : %s' % item)
    return True
  except Exception as e:
    print('Item not removed : %s : %s' % (item,e))
    return False

def index_remove(list,index):
    ''' Uses `pop()` to remove an index from a list. 
    * Returns bool indicating operation was successful. 
    * Constant runtime. Amortized constant space.
    ''' 
    try: 
      list.pop(index)
      print('Index removed : %s' % index)
      return True
    except Exception as e:
      print('Index not removed : %s : %s' % (index,e))
      return False

def iter_sort(iter):
  ''' Uses `sorted(iterable)` to sort any iterable.
  * Returns a new sorted list or `False`.
  * See https://docs.python.org/3/howto/sorting.html
  '''
  try:
    new = sorted(iter)
    print('Iter sort complete.')
    return new
  except Exception as e:
    print('Iter not sorted : %s' % e)
    return False

def list_sort(list):
  ''' Uses `list.sort()` to sort a list.
  * Sorts list in place. 
  * Returns bool indicating operation was successful. 
  * See https://docs.python.org/3/howto/sorting.html
  '''
  try:
    list.sort()
    print('List sort complete.')
    return True
  except Exception as e:
    print('List not sorted : %s' % e)
    return False

def iter_reverse(iter):
  ''' Uses `reversed(iterable)` to reverse the order of an iterable.
  * Returns new reversed list or `False`.
  * See https://docs.python.org/3/library/functions.html?highlight=reverse#reversed
  '''
  try:
    new = list(reversed(iter))
    print('Iter reversed')
    return new
  except Exception as e:
    print('Iter not reversed : %s' % e)
    return False

def list_reverse(list):
  ''' Uses `list.reverse()` to reverse the order of a list.
  * Reverses list in place.   
  * Returns bool indicating operation was sucessful.
  * See 
  '''
  try:
    list.reverse()
    print('List reversed.')
    return True
  except Exception as e:
    print('List not reversed : %s' % e)
    return False

def list_clear(list):
  ''' Uses `list.clear()` to remove all items from a list.
  * Returns bool indicating operation was successful.
  '''
  try:
    list.clear()
    print('List cleared')
    return True
  except Exception as e:
    print('List not cleared : %s' % e)
    return False


# -------------------------------
# Test `is_empty`
# -------------------------------
# list_nums = [1,2,3,4,5]
# list_empty = []

# print(is_empty([list_empty]))
# print(is_empty(list_nums))

# -------------------------------
# Test `item_find`
# -------------------------------
# list_nums = [1,2,3,4,5]
# list_empty = []

# # > Item found : [4] 5
# item_find(list_nums, 5)

# # > Item not found : apple
# item_find(list_nums, 'apple')

# # > Item not found : apple
# item_find(list_empty, 'apple')

# -------------------------------
# Test `item_count`
# -------------------------------
# list_dupes = [6,6,6,7,7,8,24]
# list_empty = []

# # > Item: 7 : Count: 2
# item_count(list_dupes, 7)

# # > Item: 7 : Count: 0
# item_count(list_empty, 7)

# # > Item: p : Count: 2
# item_count('apple', 'p')

# # > Item: 5 : Count: False : 'int' object has no attribute 'count'
# item_count(455, 5)

# -------------------------------
# Test `item_append`
# -------------------------------
# # > Item appended : apple
# # > [1, 2, 3, 4, 5, 'apple']
# list_nums = [1,2,3,4,5]
# item_append(list_nums, 'apple')
# print(list_nums)

# # > Item appended : 30
# # > [1, 2, 3, 4, 5, 30]
# list_nums = [1,2,3,4,5]
# item_append(list_nums, 30)
# print(list_nums)

# # > Item appended : [6, 7, 8, 9]
# # > [1, 2, 3, 4, 5, [6, 7, 8, 9]]
# list_nums = [1,2,3,4,5]
# item_append(list_nums, [6, 7, 8, 9])
# print(list_nums)

# # > Item not appended : not all arguments converted during string formatting
# # > [1, 2, 3, 4, 5, 32, 64, 128]
# list_nums = [1,2,3,4,5]
# item_extend(list_nums, (32,64,128))
# print(list_nums)

# -------------------------------
# Test `item_insert`
# -------------------------------
# list_nums = [1,2,3,4,5]

# # > Item inserted : [0] apple
# # > ['apple', 1, 2, 3, 4, 5]
# item_insert(list_nums, 0, 'apple')
# print(list_nums)

# # > Item inserted : [42] bananna
# # > ['apple', 1, 2, 3, 4, 5, 'bananna']
# item_insert(list_nums, 42, 'bananna')
# print(list_nums)

# # > Item inserted : [-1] alpha
# # > ['apple', 1, 2, 3, 4, 5, 'alpha', 'bananna']
# item_insert(list_nums, -1, 'alpha')
# print(list_nums)

# -------------------------------
# Test `item_extend`
# -------------------------------
# # > Item extended : [6, 7, 8, 9]
# # > [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_nums = [1,2,3,4,5]
# item_extend(list_nums, [6,7,8,9])
# print(list_nums)

# # > Item extended : apple
# # > [1, 2, 3, 4, 5, 'a', 'p', 'p', 'l', 'e']
# list_nums = [1,2,3,4,5]
# item_extend(list_nums, 'apple')
# print(list_nums)

# # > Item not extended : 'int' object is not iterable
# # > [1, 2, 3, 4, 5]
# list_nums = [1,2,3,4,5]
# item_extend(list_nums, 30)
# print(list_nums)

# -------------------------------
# Test `item_remove`
# -------------------------------
# # > Item removed : 3
# # > [1, 2, 4, 5]
# list_nums = [1,2,3,4,5]
# item_remove(list_nums,3)
# print(list_nums)

# # > Item removed : 2
# # > [1, 3, 1, 2, 3]
# list_dupes = [1,2,3,1,2,3]
# item_remove(list_dupes,2)
# print(list_dupes)

# # > Item not removed : 42 : list.remove(x): x not in list
# list_empty = []
# item_remove(list_empty,42)

# -------------------------------
# Test `index_remove`
# -------------------------------
# # > Index removed : 2
# # > [1, 2, 4, 5]
# list_nums = [1,2,3,4,5]
# index_remove(list_nums, 2)
# print(list_nums)

# # > Index not removed : 47 : pop index out of range
# list_nums = [1,2,3,4,5]
# index_remove(list_nums, 47)
# print(list_nums)

# -------------------------------
# Test `iter_sort`
# -------------------------------
# sorted_iter = iter_sort(listdata.list_integers_unique_unsorted)
# print(sorted_iter)

# -------------------------------
# Test `list_sort`
# -------------------------------
# unsorted = listdata.list_integers_unique_unsorted
# list_sort(unsorted)
# print(unsorted)

# -------------------------------
# Test `iter_reverse`
# -------------------------------
# iter_reversed = iter_reverse(listdata.list_integers_unique_sorted)
# print(iter_reversed)

# -------------------------------
# Test `list_reverse`
# -------------------------------
# list_reversed = listdata.list_integers_unique_sorted
# list_reverse(list_reversed)
# print(list_reversed)

