# pylint: disable=no-member
import os
import logging
from time import sleep
from datetime import datetime

import requests
from dotenv import load_dotenv
from pprint import pprint

from src.dictionary import Dictionary
from src.dictionary.interface import WordNotFoundError
from src.notion import NotionDatabase, NotionPage
from src.loggers import handlers
from src.flask_server import flask_server



load_dotenv()  # take environment variables from a .env file. see https://pypi.org/project/python-dotenv/

def append_to_file(filename, contents):
    with open(filename, 'a') as f:
        f.write(f"{contents}\n")


def main():
    
    # create loggers
    log_error = logging.getLogger(f"{__name__}: errors")
    log_error.addHandler(handlers.streaming())
    log_error.addHandler(handlers.error_handler())
    
    log_not_found = logging.getLogger(f"{__name__}: not found")
    log_not_found.addHandler(handlers.streaming())
    log_not_found.addHandler(handlers.definition_not_found())
    

    # Run a web server to keep the replit repo alive with UpTimeRobot pings
    flask_server.keep_alive()
    
    
    # Create a connection to the Notion Database 
    db = NotionDatabase(os.environ.get('DB_ID'))
    if repr(db) == "NotionDatabase(None)":
        log_error.critical("Environmental variable -> 'DB_ID' not found")
    
    # Query for rows with empty definitions
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
    while True:
        db_query = db.query(returns='page', query_filter=query)
        
        # Iterate through each page (word) and fill in it's definition
        for page in db_query:
            
            # Find the page's word
            word = page.get_page_property('Name')['results'][0]['title']['plain_text']
    
            # Attempt to find it's definition, and add it to the page
            try:
                definition = Dictionary(word)
            except WordNotFoundError as exc:
                log_not_found.warning(f"{word} -> not found", exc_info=True)
                append_to_file(".logs/word.log", f"{datetime.now()}: {word} -> not found")
                continue
        
            append_to_file(".logs/word.log", f"{datetime.now()}: {word} -> found")
            page.set_page_property('Definitions', page.rich_text(str(definition.meanings)))
            
        # sleep for 15 minutes
        sleep(60*15)


if __name__ == "__main__":
    main()
