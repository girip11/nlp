# Tokenization

Split the text in to tokens.

![Tokenization](../assets/tokenization.png)

```Python
# customizing tokenization in spacy 3.0
import spacy
from spacy.symbols import ORTH

nlp = spacy.load("en_core_web_md")

doc = nlp("gimme that")  # phrase to tokenize

# get the models vocabulary
print(len(doc.vocab))

print([w.text for w in doc])  # ['gimme', 'that']

# Add special case rule
special_case = [{ORTH: "gim"}, {ORTH: "me"}]
nlp.tokenizer.add_special_case("gimme", special_case)

# Check new tokenization
print([w.text for w in nlp("gimme that")])  # ['gim', 'me', 'that']
```

Detailed explanation on the tokenization can be found in [this tutorial](https://ashutoshtripathi.com/2020/04/06/guide-to-tokenization-lemmatization-stop-words-and-phrase-matching-using-spacy/)

## Span

- Continuous tokens from the doc forms a span

```Python
doc = nlp("gimme that")  # phrase to tokenize

# since doc is an iterable, we can slice the doc
# we get the tokens spanning index 4 and 5
doc_span = doc[4:6]

print(type(doc_span)) # spacy.tokens.span.Span
```
