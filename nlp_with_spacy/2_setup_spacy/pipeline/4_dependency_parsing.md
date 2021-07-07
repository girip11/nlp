# Syntactic Dependency parsing

- Process of extracting the dependencies of a sentence to represent its grammatical structure.

> The verb is usually the head of the sentence(ROOT). All other words are linked to the headword.

```Python
doc = nlp("I am flying to London")

for token in doc:
    print(f"{token.text}, {token.dep_}, {spacy.explain(token.dep_)}")
```

- Dependency parsing represents the words in the document as a directed graph.
- Word becomes the node and the edges provides the relationship between the nodes.

Visualizing dependency parsing

```Python
from spacy import displacy

doc = nlp("I am flying to London")

displacy.serve(doc, style="dep", options={"distance": 90})
```

![Dependency parsing graph visualized using displacy](assets/dependency_parsing_graph.png)
