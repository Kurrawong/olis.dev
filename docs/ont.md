# Olis Ontology

The Oli<span class="rtl">s</span> ontology is a model of virtual and real RDF Named Graphs and relations between them.

It defines only a couple of classes and a few predicates.

## RDF
The ontology RDF is available [here](assets/olis.ttl){:download="olis.ttl"}.

## Classes

### Named Graph

An RDF Named Graph

### Real Graph

An RDF Named Graph that contains triples

### Virtual Graph

An RDF Named Graph that is an alias for other Named Graphs and does not contain triples

## Predicates

### is alias for

A Virtual Graph is an alias for one ore more other Named Graphs

### name

The name of the item

### description

A description of the item