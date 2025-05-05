import nltk

# Download required resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):    
    tokens = nltk.word_tokenize(text)    
    tagged = nltk.pos_tag(tokens)    
    for word, tag in tagged:
        print(f"{word} -> {tag}")

sentence = input("Enter a sentence for POS tagging: ")
pos_tagging(sentence)
