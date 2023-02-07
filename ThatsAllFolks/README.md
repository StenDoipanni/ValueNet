

# FOLK ontological module



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
4. Treat those values as frames (as in Fillmore frame semantics), therefore as classes of situations for which it is possible to individuate roles, lexical triggers, and factual entities that, in their semantics, point at a folk value-related occurrence of a certain situation.

While this ontological module does not bear any domain expert authority, its intention is exactly to provide, next to the “official” theoretical ontological transposition, a module that considers also a bottom-up determined folk perspective, and which allows spotting more cultural depending entities. Among gathered folk values, relevant retrievals not considered in BHV and MFT modules, and related to a much more pragmatic dimension, are e.g. `folk:Fitness`: the social importance of being fit; `folk:Punctuality`: social appraisal related to not being late; `folk:Frugality`: moral judgments about bragging about wealthiness; `folk:Wealthiness` itself; `folk:Authenticity`: the idea of being sincere in everyday manifestation and “not interpreting a character”; `folk:Intelligence`: being above average in commonsense intelligence-related tasks; and many others, for a total amount of more than 200 folk values, formalised as frames.


The knowledge graph population process is realised via applying the [QUOKKA](https://github.com/StenDoipanni/QUOKKA) workflow as follows: 


![QUOKKA workflow applied to FOLK repository.](https://github.com/StenDoipanni/ValueNet/blob/main/ThatsAllFolks/quokka_folk.png)


Values are here considered as frames, therefore requiring roles to realize a specific value situation (occurrence of some frame).
Furthermore, value-frames are evoked by entities, e.g. the Figure above shows triggers for the frame `folk:Capable` which is the Folk value referring to commonsense positive evaluation of know-how in some domain.

Entities from well-known semantic web resources, aligned in the [Framester](https://github.com/framester/Framester) hub are gathered via SPARQL queries and declared as value triggers in the FOLK module. <br>
In figure above are shown examples for the `folk:Capable` value frame e.g. the FrameNet frames `fs:Expertise` and `fs:Capability`, or the WordNet synset `wn:skilled-adjective-1`, the VerbNet verb `vb:Excel_74010000` and so on.

The FOLK module is part of the ValueNet ontology, queryable at the [Framester SPARQL endpoint](http://etna.istc.cnr.it/framester2/sparql).


## Explore the Resource via SPARQL query

We provide here some useful query to explore the resource:

*Query 1*
Query to retrieve all the entities triggering some value (from all the theories included in ValueNet) filtered by containing in their URI the string 'expertise'.

```
PREFIX fschema: <https://w3id.org/framester/schema/>
PREFIX vcvf: <http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl#>

SELECT DISTINCT ?entity ?value
WHERE{
  ?entity vcvf:triggers ?value .

FILTER(regex(?entity, "expertise", "i"))
}
```

*Query 2*

Query to retrieve all entities triggering some value from the Folk module and the MFT module filtered by containing the string "fair" (therefore expressing some overlap between commonsense knowledge about values and the MFT theoretical framework focused on morality).

```
PREFIX mft: <https://w3id.org/spice/SON/HaidtValues#>
PREFIX folk: <http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#>
PREFIX vcvf: <http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl#>

SELECT DISTINCT ?entity ?value1  ?value2
WHERE {
?entity vcvf:triggers ?value1, ?value2 .
FILTER(regex(?value1, "https://w3id.org/spice/SON/HaidtValues#"))
FILTER(regex(?value2, "http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl#"))
FILTER(regex(?entity, "fair", "i"))
}

```


## Frame-based Epistemic Stance Detection

Epistemic stance has been defined as: "the combination of attitudes, feelings, judgments, or commitment concerning the propositional content of a message" (Biber and Finegan: 1989).

Exploiting the graph structure it is possible to infer knowledge from the latent moral content of some sentence. Consider a simple sentence like *They are smart and experienced*. Commonsense knowledge suggests us that the expressor of the sentence is stating an opinion about some entity ("they"), and this opinion qualifies the entity with adjectives referring to intelligence and expertise. Consider the Figure below, automatically generated using the FRED tool (ticking the "Align to Framester" option):


![They are smart and experienced]()


The graph of semantic dependencies is automatically generated by the [FRED](http://wit.istc.cnr.it/stlab-tools/fred/demo/?) tool, and then enriched with a value-knowledge layer.
The disambiguation to WordNet synsets `wn:smart-adjective-1` and `wn:experienced-adjective-1` allows the detection of `folk:Intelligence` and `folk:Capable`.
We can hypothesize that, if a cognizer qualifies some entity with adjectives triggering positive values such as "intelligence" and "competence", the cognizer attributes a positive polarity to the qualified entity, and the entity is "euphoric" (good bearer) in relation to the cognizer.



