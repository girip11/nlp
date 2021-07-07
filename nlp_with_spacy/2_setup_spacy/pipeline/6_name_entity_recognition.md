# Name Entity Recognition

- Available via `Token.ent_type` (int) or `Token.ent_type_`

```Python
import spacy

nlp = spacy.load("en_core_web_md")

for token in nlp("I am flying to London"):
    print(f"{token.text}, {token.ent_type_}")
```

Apart from `ent_type_` attribute on the token, we also have `ent_iob_`. This attribute indicates whether a token is part of a named entity text(if the entity spans multiple tokens). Interpretation is as follows

- `B` - Token is at the start of the entity name. "San" in "San Francisco"
- `I` - Token is inside the entity name. "Francisco" in "San Fransisco"
- `O` - Token outside entity name.

To get only the entities in the text we could use the `doc.ents` attribute. This seems to be the **standard way of accessing entities** in the text.

```Python
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# ent.start - start index of the word in the tokens list
# ent.end - end index of the word in the tokens list
# ent.start_char = index of start character in the text
# ent.end_char = index of end character in the text
for ent in doc.ents:
    # label_ contains the type of entity
    print(ent.text, ent.start_char, ent.end_char, ent.label_, spacy.explain(ent.label_))
```

## NER tags/labels

Attributes `label_` or `ent_type_` can take one of the following tag values:

- `PERSON` - People
- `NORP` - Nationalities, Religious or Political groups
- `FAC` - Buildings, Airports
- `ORG` - Companies, institutions, organizations
- `GPE` - Countries, cities, states
- `LOC` - NON GPE locations
- `PRODUCT` - Objects, food, vehicles

Additional name entity tags are taken from [here](https://towardsdatascience.com/named-entity-recognition-ner-using-spacy-nlp-part-4-28da2ece57c6):

![Name entity tags](assets/name_entity_tags.png)

## User defined NER

```Python
from itertools import chain
from spacy.tokens.span import Span

doc = nlp("John is eating Cheesy Pizza")

print(doc.ents) # prints (John,)

# https://spacy.io/api/span
product_tag = nlp.vocab.strings["PRODUCT"]
# span = Span(doc, 3, 5, label=product_tag)
span = Span(doc, 3, 5, label="PRODUCT")

doc.ents = tuple(chain(doc.ents, [span]))

# prints
# John PERSON
# Cheesy Pizza PRODUCT
for ent in doc.ents:
    print(ent.text, ent.label_)
```

## Tag all occurences of NER

- `PhraseMatcher` is used to find all the matching spans of the custom entity and tag them all.

```Python
from itertools import chain
from spacy.tokens.span import Span
from spacy.matcher import PhraseMatcher

def on_health_match_cb(matcher, doc, id, matches):
    for match in matches:
        _, start, end = match
        print(" ".join(token.text for token in doc[start: end]))

matcher = PhraseMatcher(nlp.vocab)

obama_phrases = ["Barack Obama"]
obama_phrase_patterns = [nlp(text) for text in obama_phrases]

healthcare_phrases = ["health care reform", "healthcare reform"]
healthcare_phrases_patterns = [nlp(text) for text in healthcare_phrases]

# https://spacy.io/api/phrasematcher#add
matcher.add("HEALTH", healthcare_phrases_patterns, on_match=on_health_match_cb)

doc = nlp("Barack Obama urges Congress to find courage to defend his healthcare reform")

matches = matcher(doc)

doc.ents = tuple(chain(doc.ents, (Span(doc, match[1], match[2], label="OBAMA")for match in matches)))

print(doc.ents)
```

## Remove tag/label from matcher/NER

```Python
matcher.remove("OBAMA")
```

## Visualizing NER

```Python
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")

displacy.serve(nlp("I am flying to Bombay"), style="ent")
```

- `displacy.render(doc, style="ent", jupyter=True)` to render on jupyter notebook.
- By iterating through `doc.sents` we can visualize line by line.
- Using `options` parameter we can customize the rendering. `options={"ents": ["PERSON"]}` will displacy/highlight only the ORG entities.
- We can also assign different colors to each of the label by passing the `options={"colors": {"ORG": "green"}}`

---

## References

- [NER using spacy](https://towardsdatascience.com/named-entity-recognition-ner-using-spacy-nlp-part-4-28da2ece57c6)
