# ValueNet


Values, as intended in ethics, are part of the broad and challenging area of research about Commonsense Knowledge. The attempt
to untangle the complex structure of relations among human moral and social values requires investigating subjective human perception of the world as well as socio-cultural dynamics. 

We propose **ValueNet**, a modular ontology representing values. 
ValueNet is based on reusable Ontology Design Patterns, it is aligned to the [DOLCE](https://ontopia-lode.agid.gov.it/lode/extract?url=http://ontologydesignpatterns.org/ont/dul/DUL.owl) foundational ontology, and it is a component of the [Framester](https://github.com/framester/Framester) factual-linguistic knowledge graph.



![ValueNet_usage_network](https://user-images.githubusercontent.com/40241049/171409970-2fad99c0-88b6-4c59-8202-e152cf357a4e.png)



## ValueCore
ValueCore module defines a framal structure (Fillmore's Frame Semantics) to represent entities and relations in Value Situations.
The module reuses the [Description&Situation](http://ontologydesignpatterns.org/wiki/Submissions:DescriptionAndSituation) Ontology Design Pattern, considering Value as a dul:Description, satisfied by the occurrence of some Value frame situation specified as follows.


![iswc_valuecore](https://user-images.githubusercontent.com/40241049/171409820-7cf4cb8e-8cc1-4d34-beb7-3f34020b2232.png)



Three main types of vn:ValueSituation, subclasses of dul:Situation, are modeled: 

- **vn:ValueAppraisal** : An agent appraises some entity according to some pivoting Value.

- **vn:ValueRecognition** : An agent recognizes some Value in some context.

- **vn:ValueCommitment** : An agent commits to some Value in some context.



![value_appr_comm_recog](https://user-images.githubusercontent.com/40241049/171410630-97d76958-9892-4436-8003-549e5a994ba6.png)


## MFTriggers
MFTriggers operationalizes Graham and Haidt’s Moral Foundation Theory, providing an explicit semantics to its moral values and violations.contains more than 12000 triples linking moral values to entities from existing lexical and factual web semantics resources, such as FrameNet, VerbNet, WordNet, and DBpedia.


### Explore the MFTriggers Resource

Here some useful queries to explore the resource. <br/>
The queries can be performed on the [Framester endpoint](http://etna.istc.cnr.it/framester2/sparql) <br/>
Enjoy! <br/>

---------------------------------------------------------------------------------------------------------------------------------------------------------------

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

