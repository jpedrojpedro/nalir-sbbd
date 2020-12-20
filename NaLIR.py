# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: NaLIR-SBBD
#     language: python
#     name: nalir-sbbd
# ---

from nalir import *

config_json_text = '''{
    "connection":{
        "host": "localhost",
        "password":"desenvolvimento123",
        "user":"nalir",
        "database":"mas"
    },
    "loggingMode": "ERROR",
    "zfiles_path":"/home/novello/nalir-sbbd/zfiles",
    "jars_path":"/home/novello/nalir-sbbd/jars/new_jars"
}
'''
config = ConfigHandler(reset=True,config_json_text=config_json_text)

rdbms = RDBMS(config)

query_line='return me the keyword, which have been contained by the most publications in VLDB conference.'
query = Query(query_line,rdbms.schema_graph)

# ## Stanford Dependency Parser

StanfordParser(query,config)
query.parse_tree

# **Important Note**: The graph vizualitation requires the program [Graphviz](https://graphviz.org/) (alongside with the graphviz python package) to be installed.

query.parse_tree.show()

# ## Node Mapper
import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('punkt')
NodeMapper.phrase_process(query,rdbms,config)

query.parse_tree.show()

# ##  Entity Resolution

# The entity pairs denote that two nodes represente the same entity.

entity_resolute(query)
query.entities

# ## Tree Structure Adjustor

TreeStructureAdjustor.tree_structure_adjust(query,rdbms)
query.query_tree.show()

# ## Explainer

explain(query)
query.query_tree.show()

# ## SQL Translator

# **Important Node**: The error message is resultant of line 191 of file data_structure/block.py

translate(query, rdbms)
print('query: ', query.translated_sql)
