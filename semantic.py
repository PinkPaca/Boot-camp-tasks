import spacy
# run with en_core_web_md
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("cat and monkey: ", word1.similarity(word2))  # 0.5929930274321619
print("monkey and banana: ", word3.similarity(word2))  # 0.40415016164997786
print("banana and cat: ", word3.similarity(word1))  # 0.22358827466989753

print("--------------my own example---------------")
word4 = nlp("parrot")
word5 = nlp("song")
word6 = nlp("singer")

print("parrot and song: ", word4.similarity(word5))  # 0.11795391524371154
print("song and singer: ", word6.similarity(word5))  # 0.6154057460076743
print("singer and parrot: ", word6.similarity(word4))  # 0.029887925438269257

# run with en_core_web_sm
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("cat and monkey: ", word1.similarity(word2))  # 0.6770567131180597
print("monkey and banana: ", word3.similarity(word2))  # 0.7276310914874259
print("banana and cat: ", word3.similarity(word1))  # 0.6806929608512433

print("--------------my own example---------------")
word4 = nlp("parrot")
word5 = nlp("song")
word6 = nlp("singer")

print("parrot and song: ", word4.similarity(word5))  # 0.31784500149932227
print("song and singer: ", word6.similarity(word5))  # 0.7851281072238708
print("singer and parrot: " ,word6.similarity(word4))  # 0.22650252413882274