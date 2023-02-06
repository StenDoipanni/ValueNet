

# FOLK ontological module



The FOLK module is the ontological module in ValueNet for representing social-standard-determined virtues. <br>

The existence of this module is motivated by a factual and pragmatic approach: albeit the huge debate about what and how many moral values are there, people still have commonsense knowledge about behaviors that shape everyday social interaction.
In everyday life, people can answer questions like “what is that you look for in a good friend?” or “what do you evaluate the most in your search for a soulmate”, etc. <br>

For instance, adopting or not a healthier, low-fat diet may not be considered directly a moral issue (such as trolley dilemmas), but many subcultures focused on the "Sanctity" pole of the Moral Foundations Theory dyad, resonate with the “my body is a temple” metaphor, considering morally inferior not to adopt healthy habits. <br>

These values are considered "mandatory" in the sense that everyone is expected to respect them, and is expected to be judged if not. <br>
People who fail or refuse to do so are subject to social criticism or punishment. <br>



Ultimately, in the ValueNet ontology network BHV module (based on Basic Human Values theory) aims at covering individual and cultural values, MFT (based on Moral Foundations Theory) is focused on the moral judgment aspect of values, and the FOLK module deals with this aspect of “social expectation”.

Therefore, to investigate culturally relative morality, we tried to reverse engineer this big substratum of commonsense knowledge.

The generation of the Folk value module, and its operationalisation with a bottom-up approach, is done by following these three steps:
1. Scrape the web for extended lists of what people consider values. Note that this could be any kind of list, from online life coach guidelines to live a better life, to unoffcial repositories of cultural values, that we named “folk values”;
2. Model them in a dedicated ontological module;
3. Establish a taxonomy among them, and filter the granularity of detail, namely, remove duplicates with different names (e.g. “Victory” and “Winning”) which were pointing at a very similar portion of reality.
4. Treat those values as frames, therefore as classes of situations for which it is possible to individuate roles, lexical triggers, and factual entities that, in their semantics, point at a folk value-related occurrence of a certain situation.

While this ontological module does not bear any domain expert authority, its intention is exactly to provide, next to the “official” theoretical ontological transposition, a module that considers also a bottom-up determined folk perspective, and which allows spotting more cultural depending entities. Among gathered folk values, relevant retrievals not considered in BHV and MFT modules, and related to a much more pragmatic dimension, are e.g. folk:Fitness: the social importance of being fit; folk:Punctuality: social appraisal related to not being late; folk:Frugality: moral judgments about bragging about wealthiness; folk:Wealthiness itself; folk:Authenticity: the idea of being sincere in everyday manifestation and “not interpreting a character”; folk:Intelligence: being above average in commonsense intelligence-related tasks; and many others, for a total amount of more than 200 folk values, formalised as frames.


The knowledge graph population process is realised via applying again the QUOKKA workflow as in ref.

The FOLK module is part of the ValueNet ontology, queryable here(link).
