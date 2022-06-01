# ValueNet


Values, as intended in ethics, are part of the broad and challenging area of research about Commonsense Knowledge. The attempt
to untangle the complex structure of relations among human moral and social values requires investigating subjective human perception of the world as well as socio-cultural dynamics. 

We propose **ValueNet**, a modular ontology representing values. 
ValueNet is based on reusable Ontology Design Patterns, it is aligned to the [DOLCE](https://ontopia-lode.agid.gov.it/lode/extract?url=http://ontologydesignpatterns.org/ont/dul/DUL.owl) foundational ontology, and it is a component of the [Framester](https://github.com/framester/Framester) factual-linguistic knowledge graph. 

Its **ValueCore** module defines a framal structure to represent entities and relations in Value Situations, and operationalizes Graham and Haidt’s Moral Foundation Theory in a dedicated module (MFTriggers), providing an explicit semantics to its moral values and violations.

**MFTriggers** contains more than 12000 triples linking moral values to entities from existing lexical and factual web semantics resources, such as FrameNet, VerbNet, WordNet, and DBpedia.
