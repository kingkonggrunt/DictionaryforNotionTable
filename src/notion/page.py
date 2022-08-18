import requests

from .api import NotionAPI

class NotionPage(NotionAPI):
    """An objective representation of a Notion Page.

    A Notion Page from a Database table will contain properties that equal the column names of the
    table the page originates from.
    Otherwise, properties are merely properties of the page.

    """
    def __init__(self, page_id):
        """
        :param _type_ page_id: ID is found in the share url or the NotionPage.
        Refer to NotionDatabase
        """
        self.page_id = page_id
        self.page = self.page_id
        self.properties = self.page

    def set_page_property(self, page_property: str, update: dict) -> requests.Response:
        """Update a page property on a Notion Page
        Refer to https://developers.notion.com/reference/property-value-object on how to create an
        update patch for your property

        :param str page_property: property name or id
        :param dict update: https://developers.notion.com/reference/property-value-object
        :return requests.Response: api response
        """
        route = f"https://api.notion.com/v1/pages/{self.page_id}"

        patch = {"properties": {page_property : update }}

        return requests.patch(route, json=patch, headers=self.create_header())

    def get_page_property(self, page_property) -> requests.Response.json:
        """Get the API response of a page's page property

        :param _type_ page_property: name or id
        :return requests.Response.json: API response for the page
        """
        route = f"https://api.notion.com/v1/pages/{self.page_id}/properties/{page_property}"

        return requests.get(route, headers=self.create_header()).json()

    @property
    def properties(self) -> dict:
        """Return the page properties of the page.
        If the page originates from a Notion Database table, then the page properties are the 
        column names of the table

        :return dict: page property names and id's
        """
        return self._properties

    @properties.setter
    def properties(self, page):
        # self._properties = {name:id['id'] for name, id in page['properties'].items()}
        self._properties = page['properties']

    @property
    def page(self) -> requests.Response.json:
        """API response for the Notion Page

        :return requests.Response.json: api response
        """
        return self._page

    @page.setter
    def page(self, page_id):
        route = f"https://api.notion.com/v1/pages/{page_id}"
        self._page = requests.get(route, headers=self.create_header()).json()

    def __repr__(self) -> str:
        return f"NotionPage('{self.page_id}')"

    @staticmethod
    def get_plain_text(page_property) -> str:
        """Get the plain text of a rich text property

        :param _type_ page_property: name or id
        :return str: plain text of the page property
        """
        # TODO this is hard coded to only work for rich_text property types.
        # write the code to identify the property type to
        # maybe consist placing this in another class
        return page_property['results'][0]['rich_text']['plain_text']

    @staticmethod
    def rich_text(text: str, italic: bool=None, bold: bool=None, color=None) -> dict:
        """Create a rich_text patch for a Notion field

        :param str text: text contents
        :param bool italic: italicise text, defaults to None
        :param bool bold: bold text, defaults to None
        :param _type_ color: color text, defaults to None
        :return dict: update patch to add rich text to Notion
        Example:
        # A current use case is to update a rich_text page property
        page = NotionPage()
        page.set_page_property('Comments', page.rich_text("NICE ONE!!"))
        """

        annotations = {}
        if italic:
            annotations['italic'] = italic
        if bold:
            annotations['bold'] = bold
        if color:
            annotations['color'] = color

        content = {
            "type": "text",
            "text": {
                'content': text
            },
            "annotations": annotations
        }


        return {
            'rich_text' : [content]
        }

    # TODO property value builder/class
    # TODO create a rich text builder to build rich text json patches
    