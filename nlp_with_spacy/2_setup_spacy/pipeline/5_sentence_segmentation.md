# Sentence segmentation (Span)

The sentence split is referred to as spans.

```Python
doc = nlp("I am flying to London. I will be flying back to Frisco tomorrow.")

print(doc[5].is_sent_end) # refers to "."

print(doc[6].is_sent_start) # refers to "I" in the second sentence

for sentence in doc.sents:
    print(sentence)
```

---

## References

- [Sentence segmentation](https://ashutoshtripathi.com/2020/04/02/spacy-installation-and-basic-operations-nlp-text-processing-library/)
