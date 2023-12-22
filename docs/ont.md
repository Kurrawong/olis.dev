# Olis Virtual Graph Ontology

The Oli<span class="rtl">s</span> Virtual Graph ontology defines only a couple of classes and a few predicates for the representation of chunks of a Knowledge Graph - sub-graphs that make up the whole.

## RDF
The ontology RDF is available [here](assets/olis.ttl){:download="vg.ttl"}.

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