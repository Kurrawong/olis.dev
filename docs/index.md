# Intro to Olis

Oli<span class="rtl">s</span> is a graph management application. Its job is to help administrators of [Knowledge Graphs](https://en.wikipedia.org/wiki/Knowledge_graph) manage them as a series of sub-graphs.

## Opposite of Silo

Oli<span class="rtl">s</span>, "Silo", reversed!, is the _opposite_ of a Data Silo as there are as few barriers as possible to getting data in and out, and even moving away from an Oli<span class="rtl">s</span>-managed dataset.

Oli<span class="rtl">s</span> does things to ensure you are completely in control of your data and not locked in my it:

* **Contains Schema in the data**
    * Oli<span class="rtl">s</span> manages data that contains its schemas within it, not somewhere else that can only be accessed through special tools
    * Administrative & configuration data used by Oli<span class="rtl">s</span> is _just more data_ in the same dataset and is accessible in the same way 
* **Strongly defined**
    * All the parts of data managed by Oli<span class="rtl">s</span> - objects, their relations, class definitions - are defined in an open standards way, so no data elements have meaning or roles that are implicit or hidden and that can be misunderstood  
* **Uses Standardised IO protocols**
    * _All_ data within an Oli<span class="rtl">s</span>-managed dataset can be accessed via the [SPARQL](http://www.w3.org/TR/sparql11-overview/) series of data standards, which includes not only a query language but protocols for lodging queries, receiving responses and dumping all data
    
## How it works

Data in a Knowledge Graph can be segmented into sub-graphs in a manner similar to the way in which _schemas_ in some relational database systems can segment data. Multiple graphs can then be used together to form the total Knowledge Graph but managed separately, if required.

Oli<span class="rtl">s</span> provides a model and an API for managing Knowledge Graph sub-graphs. The Oli<span class="rtl">s</span> data model defines:

* Real Graphs
    * Knowledge Graph sub-graphs that contain data
* Virtual Graphs
    * Knowledge Graph sub-graphs that are aliases for other Real and Virtual graphs and contain none of their own data

Using the Oli<span class="rtl">s</span> API, you can make Virtual Graphs for complex datasets that consist of potentially very many Real Graphs and other Virtual Graphs that segment the dataset's data by time or some other dimension.

!!! note "Example"
    A data stream supplies new data to a Knowledge Graph every day.

    Oli<span class="rtl">s</span> can be used to define a Virtual Graph for that stream and a Real Graph is created for incoming data each week.

    Data reprocessing or reasoning can be performed on weekly Real Graph 'chunks', rather than the whole dataset.

## How I get it

Oli<span class="rtl">s</span> is currently in pre-Alpha testing with a limited number of implementers now (September 2022). Please contact [Kurrawong AI](http://kurrawong.net) if you want in!

## Status

**Date** | **Status**
--- | ---
September 2022 | Pre-Alpha testing
November 2022 | Expected Alpha release

