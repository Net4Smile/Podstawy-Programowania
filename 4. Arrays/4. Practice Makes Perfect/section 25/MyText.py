def countWords(text):
  words = text.split()
  return len(words)

def orderWordsLtoS(text):
  words = text.split()
  words.sort()
  return ' '.join(words)

def orderAlphabetically(text):
  words = text.split()
  words.sort(key=str.lower)
  return ' '.join(words)

