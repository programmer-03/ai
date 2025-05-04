import nltk
from spellchecker import SpellChecker
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# a. POS Tagging
def pos_tagging(text):
    print(nltk.pos_tag(nltk.word_tokenize(text)))

# b. Similarity Score
def similarity(w1, w2):
    s1, s2 = wordnet.synsets(w1), wordnet.synsets(w2)
    return s1[0].wup_similarity(s2[0]) if s1 and s2 else 0

# c. Spell Checker
def spell_check(text):
    sp = SpellChecker()
    for w in text.split():
        if w not in sp:
            print(f"{w} -> {sp.correction(w)}")

pos_tagging("The quick brown fox")
print("Similarity:", similarity("car", "automobile"))
spell_check("I havv a speling errror")
