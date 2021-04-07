# Natural Language Processing (NLP) in Python - From Zero to Hero

## Bag of words

- Text to numerical representation
- Utterance - a sentence.
- From all the utterances, we take all the unique words and replace each word with 0 or 1 if the word is present in the utterance(binary feature). `sklearn.feature_extraction.CountVectorizer`. Thus each sentence is transformed in to a vector with the size of all unique words from all the training sentences.

- In bag of words, we could take unigrams, bigrams, n-grams approach to build the dictionary, that inturn translates to the feature vectors.

## Word vectors

- Word to vector. This captures the semantic meaning of a word in a vector.

- `word2vec` - Within a context window, analyze each token and try to find the relationship among the token, so that in numerical representation, such associated words can be placed close to each other.

- We could use library like **spacy** to convert word to vector. Spacy ships with already trained language models, which we could use to generate the word vectors.

## NLP techniques

- Regexes. [regex cheatsheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)
- Stemming/lemmatization - Stem words - root word of a word. Stemming is rule based. Porter stemming algorithm is commonly used for stemming. Ex: reading - read.
  - Lemmatization more accurate than stemming because stemming is rule based. **NLTK** or **spacy** can be used for getting stem words or lemmas for a given word.
  - Lemmatization uses parts of speech to find the lemma. POS tagging can be done using spacy.
- Stop words removal - Ex: `a`, `an`, `the`.
- Parts Of Speech tagging. **Textblob** is another library that can be used for spell correction and POS tagging and sentiment analysis.
- Spell check and spelling correction
- Sentiment of the sentence

## State of the art models

- Recurrent neural networks. Longer dependencies don't perform well with this architecture. Sequential nature of RNN's, tough to parallelize computation.
- LSTM - type of RNN to handle longer dependencies.
- Attention networks architecture. Learns about each token. can work with longer range dependencies.
- Transformer architectures - GPT - predict/complete phrase, sentence. BERT- bidirectional transformer architecture. **Spacy** can be used to train, transfer learn BERT, XLNET models. **Huggingface/transformers** can be used with tensorflow or pytorch.

---

## References

- [Natural Language Processing - From Zero to Hero](https://www.youtube.com/watch?v=vyOgWhwUmec)
- [Github repo](https://github.com/keithgalli/pycon2020)
