from textblob import TextBlob

def spell(text):
  blob = TextBlob(text)
  corrected = blob.correct()
  print("text: ", text)
  print("Correct: ", corrected)

spell("aryan")
