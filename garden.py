import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "Chris knew the answer to the question was yes, but wouldn't speak the word out loud.",
    "I told the girl the cat scratched Bill would help her.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi"
]

# Tokenize and perform named entity recognition
for text in gardenpathSentences:
   doc = nlp(text)
   for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Examine how spaCy has categoriesed each sentence
for text in gardenpathSentences:
  print(text,': ')
  doc = nlp(text)
  for token in doc:
    print(token, token.pos_, token.dep_, token.lemma_)

print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))
print(spacy.explain("auxpass"))
print(spacy.explain("advmod"))
print(spacy.explain("punct"))

# 1. What was the entity and its explanation that you looked up?
# :PERSON; People, including fictional and GPE; Countries, cities, state

# 2. Did the entity make sense in terms of the word associated with it?
# Yes. Chris, Bill, Mar, Jill are names of people and mississippi is name of area