def simple_pos_tag(sentence):
    nouns = {"dog", "fox", "car", "apple"}
    verbs = {"runs", "jumps", "drives", "eats"}
    tags = []
    for word in sentence.split():
        if word.lower() in nouns:
            tags.append((word, "NN"))
        elif word.lower() in verbs:
            tags.append((word, "VB"))
        else:
            tags.append((word, "UNK"))
    print(tags)


def simple_similarity(w1, w2):
    set1 = set(w1)
    set2 = set(w2)
    return len(set1 & set2) / len(set1 | set2)


w1 = input("Enter a word")
w2 = input("Enter a word")
print("Similarity Score:", simple_similarity(w1, w2))


sent = input("Enter a string: ")
simple_pos_tag(sent)
