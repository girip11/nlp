# Stop words in Spacy

Model's default stop words can be accessed using `nlp.Defaults.stop_words`

```Python
# check is a word is a stop word or not
nlp.vocab["with"].is_stop

# Adding a word as stop word
# Always use lower case
nlp.Defaults.stop_words.add("btw")

nlp.vocab["btw"].is_stop = True

# removing a stop word is removing from the `nlp.Default.stop_words` set
# and setting the is_stop to False on the `nlp.vocab`
```

---

## References

- [Processing stop words](https://ashutoshtripathi.com/2020/04/06/guide-to-tokenization-lemmatization-stop-words-and-phrase-matching-using-spacy/)
