# Lemmatization

Returns the base form of a word(Ex: particle to base verb `flying` to `fly`).

We can also add custom entries to the tokenizer for returning lemmas related to a domain specific word.

For instance, `bombay` should return its lemma as `mumbai`. The below snippet adds custom entries to the tokenizer.

```Python
# Changed in version 3.0
# Book uses spacy v2.0
import spacy
from spacy.symbols import LEMMA

nlp = spacy.load("en_core_web_md")

custom_lemma = [
    [{"TEXT": "Bombay"}]
]

nlp.get_pipe("attribute_ruler").add(custom_lemma, {LEMMA: "Mumbai"})

for token in nlp("I am flying to Bombay"):
    print(f"{token.text}, {token.lemma_}")
```

**NOTE**: All the stages in the pipeline can be obtained using `nlp.pipe_names`. `nlp.pipeline` returns list of stage names and object. `nlp.get_pipe(stage_name)` can be used to get the object corresponding to the stage.

```Python
# get all the stages
nlp.pipe_names

# get the object
nlp.get_pipe("lemmatizer")
```

Counting the frequency of POS tags in a document

```Python
from spacy.attrs import POS, TAG

doc = nlp("I am flying to London")
# This returns count of coarse grained tag.
POS_counts = doc.count_by(POS)

# This returns count of fine grained tag.
# POS_counts = doc.count_by(TAG)

for k,v in POS_counts.items():
    print(f"attribute id: {k}, attribute text: {doc.vocab[k].text}, attr frequency: {v}")
```
