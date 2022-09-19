def obfu_string(string: str, show_first: bool = True, show_last: bool = True) -> str:
  '''Obfuscates a string by replacing chars with *asterisks.
  '''
  if not show_first and not show_last:
    print("The 'show_first' and 'show_last' args cannot both be false.")
    return None

  str_list_in = []
  str_list_in.extend(string)
  str_len = len(str_list_in)

  bound = str_len // 3
  bound_lower = None
  bound_upper = None

  str_list_out = []

  if not show_first:
    bound_lower = 0
  else:
    bound_lower = bound

  if not show_last:
    bound_upper = str_len
  else:
    bound_upper = str_len - bound

  for i in range(str_len):
    if i in range(bound_lower, bound_upper): 
      str_list_out.append('*')
      continue
    # else
    str_list_out.append(str_list_in[i])
     
  return ''.join(str_list_out)

# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------

if __name__ == "__main__":

  print(obfu_string('mypasswordhere!', True, True))
  print(obfu_string('mypasswordhere!', True, False))
  print(obfu_string('mypasswordhere!', False, True))

