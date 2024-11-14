import csv
import re

def clean_query_string(query_str):
    cleaned_query = re.sub(r'[^\w\s]', '', query_str)
    return cleaned_query.strip()


def index_data(ix, data):
    writer = ix.writer()
    for entry in data:
        print(f"ID: {entry['id']}, Title: {entry['title']}, Text: {entry['text']}, Keywords: {entry['keywords']}")
        writer.add_document(
            id=str(entry['id']),
            title=entry['title'],
            text=entry['text'],
            keywords=entry['keywords']
        )
    writer.commit()

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            entry = {
                'id': int(row['id']),
                'title': row['title'],
                'text': row['text'],
                'keywords': row['keywords'].split(',')
            }
            data.append(entry)
    return data
