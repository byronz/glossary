# Glossary

**Glossary** is a small app to import, edit and output the glossary in a user 
frienly way. The main usage of glossary is to create a full list of 
terms/abbreviation/acrynom used in the PGVV domain.

## Data

The core data structure for glossary is quite straightforward: dictonary or hash
map. However it might happen that a same key here an abbreviation has more than 
one value; e.g. AMD might be a famous silicon company or means Asset Management
Device in CRV. 

## Input

Several glossary sources are available inside the company in CSV files. it 
would be helpful to directly import the glossary from a preformmated file.

- CSV
- JSON
- HTML

## Format

**Glossary** uses [YAML](http://yaml.org/spec/1.2/spec.html) to store the data 
structure (dictionary or hash map). Yaml is very easy to edit with any text 
editor. 

    MAOV: model as orcale verifier
    TTM: telemetry model

## Edit

1. Text Editor is the most evident way to modify the YAML source

## Merge

The glossary file is shared across several teams and the amount of 
terms increase smoothly. It is essential to provide the merge ability
which can merge several slightly different data with various format,
typically CSV, JSON, YAML.

## Output

**Glossary** parses the yaml file and translates it into:

- [markdown](http://daringfireball.net/projects/markdown/syntax)
- [reStructuredText](http://docutils.sourceforge.net/rst.html) 

A good number of tools are available to transfer from .md or .rst into HTML, 
PDF or Word documents. 

### HTML

HTML is the best choice for output with a customized CSS as style control. It
includes the inline link and cross link to jump, the modern web browser are 
good in search with enhanced user interactivities. 

`%> pandoc -s -c %css GLOSSARY.md -o Glossary.html`

### CSV 

CSV is simple and can be easily imported by Excel.

## Consideration

1. The framework can be easily extended for other documentation purpose. 
2. Web service with DB would be needed to have more interaction among different
teams and users. 


