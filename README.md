# DictionaryforNotionTable

Read a Notion Database Table contain words and this program will fill in the table with the definition of the words  

Uses the Notion API and freeDictionaryAPI

*Python Version*: 3.9.13

## Setup
1. Follow the instructions at https://developers.notion.com/docs/getting-started to create an integration and share the integration with the Database table
2. Save the secret token of the integration under the environment variable `SECRET_TOKEN`, likewise you can save the secret token in a `.env` file under the variable `SECRET_TOKEN` (this application use `py-dotenv` under the hood)
3. Create a virtual python environment with `python -m venv venv` and `pip install -r requirements.txt` in the activate environment to load the right packages

## Examples