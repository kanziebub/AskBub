import os
import csv

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser, MultifieldParser, OrGroup

from ir_utils import read_csv, index_data, clean_query_string

schema = Schema(
    id=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    text=TEXT(stored=True),
    keywords=TEXT(stored=True)
)

index_dir = "rulebook_index"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)
ix = create_in(index_dir, schema)
data = read_csv("rulebook.csv")
index_data(ix, data)

def search_rules(query_str):
    res_list = []
    query_str = clean_query_string(query_str)
    print(query_str)
    with ix.searcher() as searcher:
        query = MultifieldParser(
                    ["title", "keywords"], 
                    ix.schema,
                    group=OrGroup
                ).parse(query_str)
        results = searcher.search(query, limit=None)
        
        for result in results:
            res_dict = {
                "id": result['id'],
                "title": result['title'],
                "text": result['text'],
                "keywords": result['keywords']
            }
            res_list.append(res_dict)
    return res_list
    
# results = search_rules("who is visca?")
# print("============================================================================")
# for result in results:
#     print(f"ID: {result['id']}, Text: {result['text']}, Keywords: {result['keywords']}")
# print("============================================================================")
