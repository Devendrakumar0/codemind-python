def sort_words(s):
  words = s.split()
  words.sort(key=lambda x: (len(x), x))
  return ' '.join(words)

s = input()
print(sort_words(s))
