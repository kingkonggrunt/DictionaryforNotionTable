import os

from dotenv import load_dotenv

load_dotenv()

class NotionAPI:
    """Parent Class for other Notion object class (eg. NotionDatabase)

    NotionAPI will read the user's API token from a "SECRET_TOKEN" environmetal variable (which can)
    be supplied in a .env file
    """

    notion_version = '2022-06-28'

    def create_header(self) -> dict:
        """Create headers for Notion API calls

        :return dict: headers
        """
        return {
            'Authorization': f"Bearer {os.environ.get('SECRET_TOKEN')}",
            'Content-Type': 'application/json',
            'Notion-Version': self.notion_version,
        }

    def __repr__(self) -> str:
        return "NotionAPI()"
