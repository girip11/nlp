import spacy
from spacy.lang.en import English
from spacy.symbols import LEMMA, ORTH
from spacy.tokens.doc import Doc

nlp_model: English = spacy.load("en_core_web_md")

print(f"Language of the model is {nlp_model.lang}")

# Tokenization
# Doc object is a container of the token objects
doc: Doc = nlp_model("This is my first program using spacy")

print(f"Fetch the text from doc:{doc.text}")

# Lemmatization
for token in doc:
    print(f"Token:{token.text}")
    print(f"Lemma: {token.lemma_}")

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
