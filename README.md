# Glossary

**Glossary** is a small application to help organizing your glossary in a 
convenient way. As a new hire in the medical device industry, the first tough 
challenge is the endless terminology list which sometimes is hard to memorize 
in a short time. This small gadget would help on merging diffrent glossary list
from various sources (excel, doc, csv), manage the conflict of keys(termination), 
and transfer the consolidated data into a nice document.

## Data

The core data structure for glossary is quite straightforward: dictonary or hash
map. However it might happen that a same key here an abbreviation has more than 
one value; e.g. AMD might be a famous silicon company or means Asset Management
Device in CRV. 

## Input

Several glossary sources are available inside the company in CSV files. it would 
be helpful to directly import the glossary from a preformmated file.

- CSV
- JSON
- YAML

## Data Storage

**Glossary** uses [YAML](http://yaml.org/spec/1.2/spec.html) to store the data 
structure (dictionary or hash map). Yaml is very easy to edit with any text 
editor; it is also easy to transfer to JSON, CSV or other data format. 

    MAOV:
    - Model As Orcale Verifier

    TTM: 
    - Telemetry Model

## Edit

1. Text Editor is the most evident way to modify the YAML source

note:
    *the first step has no consideration to design any GUI to edit the glossary.* 

## Merge

The glossary file is shared across several teams and the amount of 
terms increase smoothly. It is essential to provide the merge ability
which can merge several slightly different data with various format,
typically CSV, JSON, YAML.

## Output

- [markdown](http://daringfireball.net/projects/markdown/syntax)
- [reStructuredText](http://docutils.sourceforge.net/rst.html) 
- [JSON](http://www.json.org/)
- [YAML](http://www.yaml.org/spec/1.2/spec.html)
- CSV

A good number of tools are available to transfer from .md or .rst into HTML, 
PDF or Word documents. 

### HTML

`%> pandoc -s -c %css GLOSSARY.md -o Glossary.html`

## Consideration

1. The framework can be easily extended for other documentation purpose. 
2. Web service with DB would be needed to have more interaction among different
teams and users. 
