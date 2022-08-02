import pandas as pd
import random

data = ['fire', 'tree', 'bird', 'whistle', 'clock', 'rainbow', 'winning a race', 'winning a trophy', 'losing a race', 'drawing', 'painting', 'singing', 'opera', "frankenstein's monster"]

# function to add a new prompt to the list of prompts (append to the list)
def add_to_list(prompt):
  to_add_without_spaces = prompt.strip()

  # make sure length > 1 and less than 100 && no duplicates
  if to_add_without_spaces in data:
    return 0 # print("This prompt is already present in the list. Please try again.")
  elif 0 < len(to_add_without_spaces) <= 100:
    # take away any leading or ending whitespaces
    data.append(to_add_without_spaces)
    return 1
  elif len(to_add_without_spaces) <= 0:
    return 2 # print("Empty input. Please try again.")
  elif len(to_add_without_spaces) > 100:
    return 3 # print("Input is too long. Please try again.")

# function to display current list (in the form of a dataframe)
def display_list():
  df = pd.DataFrame(data, columns = ['prompt'])
  return df

# return a copy of data
def display_data():
    to_ret = data.copy()
    return to_ret

# function to randomly select and output a prompt
def select_prompt():
  length = len(data)
  random_num = random.randint(0, length - 1)

  return data[random_num]

# function to remove a prompt from the list
def remove_from_list(prompt):
  to_rem_without_spaces = prompt.strip()

  # make sure length > 1 and less than 100 && no duplicates
  if len(data) == 0:
      return 3 # empty list
  elif to_rem_without_spaces in data:
    data.remove(to_rem_without_spaces)
    return 1
  elif len(to_rem_without_spaces) == 0:
    return 0 # print("Empty input. Please try again.")
  else:
    return 2 # print("This prompt is not present within the list. Please try again.")

# function to remove all prompts from the list
def remove_all():
    data.clear()

# function to restore original list
def restore_original():
    if len(data) == 0:
        new = ['fire', 'tree', 'bird', 'whistle', 'clock', 'rainbow', 'winning a race', 'winning a trophy', 'losing a race', 'drawing', 'painting', 'singing', 'opera', "frankenstein's monster"]
        data.extend(new)

# function for size of list
def size():
    return len(data)
