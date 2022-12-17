# ValueNet


Values, as intended in ethics, are part of the broad and challenging area of research about Commonsense Knowledge. The attempt
to untangle the complex structure of relations among human moral and social values requires investigating subjective human perception of the world as well as socio-cultural dynamics. 

We propose **ValueNet**, a modular ontology representing values. 
ValueNet is based on reusable Ontology Design Patterns, it is aligned to the [DOLCE](https://ontopia-lode.agid.gov.it/lode/extract?url=http://ontologydesignpatterns.org/ont/dul/DUL.owl) foundational ontology, and it is a component of the [Framester](https://github.com/framester/Framester) factual-linguistic knowledge graph.

The current version of ValueNet includes:

[ValueCore](http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl) ``http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl`` <br/>
[BHV](https://w3id.org/spice/SON/SchwartzValues) ``https://w3id.org/spice/SON/SchwartzValues`` <br/>
[BHV Triggers]() <br/>
[MFT](https://w3id.org/spice/SON/HaidtValues) ``https://w3id.org/spice/SON/HaidtValues`` <br/>
[MFTriggers](http://www.ontologydesignpatterns.org/ont/ClosureHaidtValuesFrames.owl) ``http://www.ontologydesignpatterns.org/ont/ClosureHaidtValuesFrames.owl`` <br/>
[FolkValues](http://www.ontologydesignpatterns.org/ont/values/valuemerge_rev.owl) ``http://www.ontologydesignpatterns.org/ont/values/valuemerge_rev.owl`` <br/>
[ThatsAllFolks](http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl) ``http://www.ontologydesignpatterns.org/ont/values/FolkValues.owl`` <br/>

Furthermore, some additional modules are being developed:

[MM](http://www.ontologydesignpatterns.org/ont/values/CurryMoralMolecules.owl) ``http://www.ontologydesignpatterns.org/ont/values/CurryMoralMolecules.owl``


![ValueNet_usage_network](https://user-images.githubusercontent.com/40241049/173843601-772306ea-e2c6-46d5-9ca2-ea5306aca586.png)


## ValueCore
ValueCore module defines a framal structure (Fillmore's Frame Semantics) to represent entities and relations in Value Situations.
The module reuses the [Description&Situation](http://ontologydesignpatterns.org/wiki/Submissions:DescriptionAndSituation) Ontology Design Pattern, considering Value as a dul:Description, satisfied by the occurrence of some Value frame situation specified as follows.


![iswc_valuecore](https://user-images.githubusercontent.com/40241049/171409820-7cf4cb8e-8cc1-4d34-beb7-3f34020b2232.png)



Three main types of vn:ValueSituation, subclasses of dul:Situation, are modeled: 

- **vn:ValueAppraisal** : An agent appraises some entity according to some pivoting Value.

- **vn:ValueRecognition** : An agent recognizes some Value in some context.

- **vn:ValueCommitment** : An agent commits to some Value in some context.



![value_appr_comm_recog](https://user-images.githubusercontent.com/40241049/171410630-97d76958-9892-4436-8003-549e5a994ba6.png)


## BHV
BHV is the ontological transposition of the Theory of Basic Human Values by Shalom Schwartz, proposed as a pan-cultural theory in the 1980s. Its main assumption is that human values are organized in a “value wheel”, that is, an ordering structure that organizes values as a circumplex model, dividing them in four quadrants with two opposing axes, and a congruity continuum between adjacent values.


## MFT
MFT is the ontological transposition of the Moral Foundation Theory, that was proposed as a cultural-independent theory of moral and social values, inspired by Schweder’s et al. work on universal human ethics and tightly related to the investigation of moral emotions, with a particular focus on behavioural neuro-cognitivism. Its agnostic point of view towards cultural dependencies is realized via its dyadic oppositional structure.


## MFTriggers
MFTriggers operationalizes Graham and Haidt’s Moral Foundation Theory, providing an explicit semantics to its moral values and violations.contains more than 12000 triples linking moral values to entities from existing lexical and factual web semantics resources, such as FrameNet, VerbNet, WordNet, and DBpedia.

## MM
MM is the ontological transposition of Curry's Moral Molecules theory, considering values as "cooperation strategies". It is still under development.



---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Ontology Prefixes

To explore in detail all the modules we list here some useful prefixes which can be used to query the Framester endpoint.

```
DOLCE foundational ontology
dul : <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl/>
Framester schema
fschema : <https://w3id.org/framester/schema/>
MFT module
mft : <https://w3id.org/spice/SON/HaidtValues#>
BHV module
bhv : <https://w3id.org/spice/SON/SchwartzValues#>
ValueCore module
vc : <http://www.ontologydesignpatterns.org/ont/values/valuecore.owl#>
```

### Explore the MFTriggers Resource

Here some useful queries to explore the resource. <br/>
The queries can be performed on the [Framester endpoint](http://etna.istc.cnr.it/framester2/sparql) <br/>
Enjoy! <br/>



Query to find all value triggers starting from a lexical variable, e.g. "war", retrieving in addition all the Moral Foundations triggered, and their opposite value in the dyad.

```

PREFIX vcvf: <http://www.ontologydesignpatterns.org/ont/values/valuecore_with_value_frames.owl#>
PREFIX haidt: <https://w3id.org/spice/SON/HaidtValues#>

SELECT ?s ?o ?o2
WHERE
 { ?s vcvf:triggers ?o . ?o vcvf:oppositeTo ?o2 . 
FILTER(regex(?s, "war", "i"))
}
LIMIT 10

```


### BHV Competency Questions


1. Is the entity x an instance of some value, according to BHV theory?
2. What values have as focus some ```bhv:SocialFocus``` or ```bhv:PersonalFocus```?
3. What is the ```bhv:opposingFocus``` of some value?
4. What is the attitude of some value?
5. What is the value motivation for some value?


The above mentioned CQs are satisfied by a scenario in ttl format available [here](https://github.com/spice-h2020/SON/blob/main/SchwartzValues/Schwartz_scenario.ttl).


### MFT Competency Questions

1. Is the entity x an instance of some value, according to MFT theory?
2. What is the value ```mft:opposedTo``` some entity x?


The above mentioned CQs are satisfied by a scenario in ttl format available [here](https://github.com/spice-h2020/SON/blob/main/HaidtValues/haidt_scenario.ttl)







