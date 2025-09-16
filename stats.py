def get_num_words(text):
  words = text.split()
  count = len(words)
  return count

def get_char_count(text):
  char_count = {}
  for char in text.lower():
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return char_count

def get_sorted_dict(dict):
  def sort_on(dict):
    return dict["num"]

  sorted_list = []

  for char, count in dict.items():
      if char.isalpha():
          sorted_list.append({"char": char.lower(), "num": count})

  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list