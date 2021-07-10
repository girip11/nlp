# Sentence segmentation (Span)

The sentence split is referred to as spans.

```Python
doc = nlp("I am flying to London. I will be flying back to Frisco tomorrow.")

print(doc[5].is_sent_end) # refers to "."

print(doc[6].is_sent_start) # refers to "I" in the second sentence

for sentence in doc.sents:
    # start and end token indices
    print(type(sentence)) # sentence is an object of Span
    print(sentence.text, sentence.start, sentence.end)
```

- `doc.sents` is a generator.

## Custom sentence segmentation rules

### 1. Using `Language.component` decorator

- Sentence segmentation rules should be set before the creation of the Doc object.
- Segmentation uses dependency parsing and identifying end-of-sentence punctuations.
- Custom sentence segmentation rules have to run before the parser stage.

```Python
from spacy import Language

# Language.factory if we are decorating a class
@Language.component("custom_sentence_split")
def custom_sentence_split(doc):
    for token in doc:
        if token.text == ";":
            # next token is marked as sentence beginning
            doc[token.i+1].is_sent_start = True

    return doc

nlp.add_pipe("custom_sentence_split", before="parser")
print(nlp.pipe_names)

doc = nlp("Management is doing things right; leadership is doing the right things. -Peter Drucker")

for sent in doc.sents:
    print(sent.text)
```

**NOTE**: You cannot alter `Token.is_sent_start` once the document is parsed. Hence the solution is to add the step to the NLP pipeline but executes before **`parser`** stage.

### 2. Using `Sentencizer`

Above sentence split based on different punctuation characters can also be implemented using `Sentencizer`.

From the [spacy documentation](https://spacy.io/api/sentencizer),

> `Sentencizer` lets you implement a simpler, rule-based strategy that doesn’t require a statistical model to be loaded.

```Python
from spacy.pipeline import Sentencizer

config = {"punct_chars": Sentencizer.default_punct_chars + [";"]}

# use the default name which is sentencizer
nlp.add_pipe("sentencizer", config=config)
print(nlp.pipe_names)

doc = nlp("Management is doing things right; leadership is doing the right things. -Peter Drucker")

for sent in doc.sents:
    print(sent.text)
```

## Customizing `Sentencizer`

```Python
from spacy.pipeline import Sentencizer
from spacy import Language


@Language.factory("custom_sentencizer3",
assigns=["token.is_sent_start", "doc.sents"])
def make_custom_sentencizer(
    nlp: Language,
    name: str
):
    return CustomSentencizer(name, punct_chars = Sentencizer.default_punct_chars + [";"])

class CustomSentencizer(Sentencizer):
    def __call__(self, doc):
        for token in doc:
            if token.text == ";":
                # next token is marked as sentence beginning
                doc[token.i+1].is_sent_start = True

        return doc

# We have to use before parser since we are modifying `Token.is_sent_start`
nlp.add_pipe("custom_sentencizer3", before="parser")
print(nlp.pipe_names)

doc = nlp("Management is doing things right; leadership is doing the right things. -Peter Drucker")

for sent in doc.sents:
    print(sent.text)
```

## [`SentenceRecognizer`](https://spacy.io/api/sentencerecognizer)

`SentenceRecognizer` is a **trainable pipeline** component for sentence segmentation.

---

## References

- [Sentence segmentation](https://ashutoshtripathi.com/2020/05/04/how-to-perform-sentence-segmentation-or-sentence-tokenization-using-spacy-nlp-series-part-5/)
