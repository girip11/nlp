import spacy
from spacy.symbols import LEMMA, ORTH

nlp = spacy.load("en")

# Tokenization and Lemmatization
doc_obj = nlp("This is my first program using spacy")

for word in doc_obj:
    print(word.text, word.lemma_)

# 2. special casing token to replace slang words
# Frisco is a slang word for San Francisco
special_case = [{ORTH: "Frisco", LEMMA: "San Francisco"}]

# This special case should be added to the tokenizer
nlp.tokenizer.add_special_case("Frisco", special_case)
doc_obj = nlp("I am flying to Frisco")

for word in doc_obj:
    # San Francisco becomes the lemma of Frisco
    print(word.lemma_)

# 3. Parts of speech tagging
for word in doc_obj:
    # San Francisco becomes the lemma of Frisco
    # pos_ contains coarse grained parts of speech
    # tag_ contains morphology and fine grained POS tags
    print(word.text, word.pos_, word.tag_)
