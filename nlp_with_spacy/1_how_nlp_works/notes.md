# How NLP works?

NLP is a subfield of AI that analyzes and process the human natural language data.

Computers operate on numerical data. So for computers to understand the natural language, we need to map natural language text to numbers.

## Word embedding

- Word embedding maps a word to a vector of real numbers.
- Words with similar meaning lie close to each other in the vector space.
- Textual representation of the word vector space starts with most common words.
- Graphical representation of the word vector space can be done by performing principal component analysis and reducing the dimensionality to 2 or 3.
- Sentence(list of words) becomes a matrix(list of vectors).
- Operations on matrices can be performed to find semantic similarity between the texts. Ex - Cosine similarity between two corresponding vectors - semantic similarity.

## Machine learning in NLP

- Machine learning models perform tasks like dependency parsing, parts of speech tagging, and Name Entity recognition.
- Model lifecycle consists of development, testing and making predictions.

## Statistical model in NLP

- Statistical model estimates the probability distribution of the linguistic words like words or phrases.

> In probability theory and statistics, a probability distribution for a particular variable is a table of values that maps all of the possible outcomes of that variable to their probabilities of occurrence in an experiment.

-Ex - probability distribution of all possible parts of speech tag a word can take.

Natural language generation - NLG
Natural language understanding - NLU

- Statistical models in Spacy are neural network models.

## Keywords, context and meaning transition

The following helps in identifying intent from a given utterance or a discourse.

- Keywords extraction from the depedency tree.
- Context is important when selecting keywords.
- Meaning transition - extract the intent spread across multiple sentences in a discourse.
