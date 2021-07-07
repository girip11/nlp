# Part of speech tagging

[Coarse parts of speech tags](https://ashutoshtripathi.com/2020/04/13/parts-of-speech-tagging-and-dependency-parsing-using-spacy-nlp/)include

- Noun (NOUN)
- Propernoun (PROPN)
- Pronoun (PRON)
- Determiner (DET)
- Adjective (ADJ)
- Verb (VERB)
- Adverb (ADV)
- Auxiliary (AUX). Ex: `is`, `will`
- Preposition (adp)
- Punctuation (PUNCT)
- Particle (PART)
- Conjunction (CONJ)
- Coordinating conjunction (CCONJ)
- Subordinating conjunction (SCONJ)
- Interjection (INTJ)
- Symbol (SYM)
- Number (NUM)
- Other (X)
- Space (SPACE)

Coarse parts of speech tags are available through `Token.pos_`, while fine grained parts of speech tags are available through the property `Token.tag_`

[Fine grained parts of speech tags](https://ashutoshtripathi.com/2020/04/13/parts-of-speech-tagging-and-dependency-parsing-using-spacy-nlp/) include

To view description of either fine grained or coarse grained tag, use `spacy.explain(Token.tag_)`

```Python
for token in nlp("I am flying to Bombay"):
    print(f"{token.text}, {token.lemma_}, {token.tag_}, {spacy.explain(token.tag_)}")
```
