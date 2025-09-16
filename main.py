import sys
from stats import get_num_words, get_char_count, get_sorted_dict

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  count = get_num_words(text)
  char_count = get_char_count(text)
  print_report(count, char_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def print_report(count, char_count):
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {count} total words")
  print("--------- Character Count -------")
  sorted_dict = get_sorted_dict(char_count)
  for item in sorted_dict:
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")

main()