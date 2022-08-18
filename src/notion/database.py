from typing import Union, Iterable

import requests

from .api import NotionAPI
from .page import NotionPage


class NotionDatabase(NotionAPI):
    """An objective representation of a Notion Database

    Currently, you can only query the database to return page results. Query requires knowledge in 
    building query filters (https://developers.notion.com/reference/post-database-query-filter)
    """
    def __init__(self, db):
        """
        :param string db: ID of the Notion Database.
        ID of a database is found in the share url:
        https://wwww.notion.so/<exampleworkspace>/<ID>?v=...
        """ # TODO later accept database id or notion url

        self.db_url = db
        self.db = self.db_url


    @property
    def db(self) -> requests.Response.json:
        # The notion database
        return self._db

    @db.setter
    def db(self, url):
        route = f"https://api.notion.com/v1/databases/{url}"
        self._db = requests.get(route, headers=self.create_header()).json()

    def query(self, query_filter: dict=None, returns: str='json') -> Union[requests.Response.json, Iterable[NotionPage]]:
        """Query the database.

        Returns a json response or a list of NotionPage objects for each NotionPage in the query
        result.

        See NotionPage docstring for usage of NotionPage objects (a row in a Notion table)

        :param dict query_filter: Refer to https://developers.notion.com/reference/post-database-query-filter, defaults to None
        :param str returns: output of query ('json', 'page'), defaults to 'json'
        :return Union[requests.Response.json, Iterable[NotionPage]]: json response or [NotionPage...]
        """
        route = f"https://api.notion.com/v1/databases/{self.db_url}/query"

        if query_filter is None:
            query_filter = {}

        response = requests.post(route, headers=self.create_header(), json=query_filter)

        if returns == 'json':
            return response.json()
        elif returns == 'page':
            return [NotionPage(page['id']) for page in response.json()['results']]

    def __repr__(self) -> str:
        return f"NotionDatabase({self.db_url})"
