# pylint: disable=no-member
import os

import requests
from dotenv import load_dotenv
from pprint import pprint

from src.dictionary import Dictionary
from src.dictionary.interface import WordNotFoundError
from src.notion import NotionDatabase, NotionPage



load_dotenv()  # take environment variables from a .env file. see https://pypi.org/project/python-dotenv/


headers = {
        'Authorization': f"Bearer {os.environ.get('SECRET_TOKEN')}",
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28',
}

db_url = f"https://api.notion.com/v1/databases/{os.environ.get('DB_URL')}"
db_query = f"https://api.notion.com/v1/databases/{os.environ.get('DB_URL')}/query"

query = {
    "filter": {
        "and" : [
            {
                "property": "Definitions",
                "rich_text": {
                    "is_empty": True
                }
            },
            {
                "property": "Name",
                "rich_text": {
                    "contains": "Test"
                }
            }
        ]
    }
}

def retrieve_database(url, headers=None) -> requests.Response:
    route = f"https://api.notion.com/v1/databases/{url}"
    return requests.get(route, headers=headers)

def query_database(url, headers=None, query_filter=None,) -> requests.Response:
    route = f"https://api.notion.com/v1/databases/{url}/query"
    if query_filter:
        return requests.post(route, headers=headers, json=query_filter)
    else:
        return requests.post(route, headers=headers, json={})
    
def retrieve_row_ids_in_database(url, headers=None, query_filter=None) -> list:
    database = query_database(url, headers=headers, query_filter=query_filter)
    
    # rows in the database are listed under the results key
    # print(database.json()['results'])
    return [row['id'] for row in database.json()['results']]

# def retrieve_page_id(url, header)

def retrieve_page_by_id(id, headers=headers) -> requests.Response:
    route = f"https://api.notion.com/v1/pages/{id}"
    
    return requests.get(route, headers=headers)


def retrieve_page_property_id_by_name(id, name=None, headers=headers) -> str:
    if name is None:
        raise ValueError("No name specified")
    
    response = retrieve_page_by_id(id, headers=headers)
    return response.json()['properties'][name]['id']

def retrieve_page_property(page_id, property_id, headers=None) -> requests.Response:
    route = f"https://api.notion.com/v1/pages/{page_id}/properties/{property_id}"
    
    return requests.get(route, headers=headers)


def update_page_property(page_id, headers=headers, patch: dict=None):
    route = f"https://api.notion.com/v1/pages/{page_id}"
    
    return requests.patch(route, headers=headers, json=patch)

# have a function that retreives a page property if either an id or a name is given


def update_definition_property(page_id, definition, headers=headers):
    patch = {
        "properties": {
            "Definitions" : {
                'rich_text' : [
                    {
                        "type": "text",
                        "text": {
                            'content': definition
                        }
                    }    
                ]
            }
        }
    }
    
    return update_page_property(page_id, patch=patch, headers=headers)



def define_word(word) -> requests.Response:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    return requests.get(url)

def main():

    query = {
        "filter": {
            "and" : [
                {
                    "property": "Definitions",
                    "rich_text": {
                        "is_empty": True
                    }
                },
                # {
                #     "property": "Name",
                #     "rich_text": {
                #         "contains": "Test"
                #     }
                # }
            ]
        }
    }


    db = NotionDatabase(os.environ.get('DB_ID'))

    db_query = db.query(returns='page', query_filter=query)
    
    for page in db_query:
        word = page.get_page_property('Name')['results'][0]['title']['plain_text']
   
        try:
            definition = Dictionary(word)
        except WordNotFoundError as exc:
            continue
        page.set_page_property('Definitions', page.rich_text(str(definition.meanings)))


if __name__ == "__main__":
    main()
    
    # definition = Dictionary('Profligate')
    
    # print(definition.parts_of_speech)
    # print(definition.noun)
    # print(definition.verb.synonyms)
    
    # Get id for each page with an empty definition
    # Get the id for the definitions property
        # Value of text is inside [results][0][rich_text][plain_text]
        # value of hyperlink is inside [results][0][rich_text][text][link]