import MyText

text = "An apple a day keeps the doctor away"

wordCount = MyText.countWords(text)

fromLongestToShortest = MyText.orderWordsLtoS(text)

alphabetically = MyText.orderAlphabetically(text)

print("Text:", text)
print("Number of words:", wordCount)
print("Words from longest:", fromLongestToShortest)
print("Words ordered alphabetically:", alphabetically)