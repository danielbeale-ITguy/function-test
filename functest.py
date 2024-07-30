import azure.functions as func

import logging

from azure.cosmos import exceptions, CosmosClient, partition_key

  

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

  
  

def testingfun(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

  

    URL = 'https://danscosmosdb.documents.azure.com:443/'

    KEY = ''

  

    client = CosmosClient(URL, credential=KEY)

    DATABASE_NAME = 'ResumeCounterBase'

    database = client.get_database_client(DATABASE_NAME)

    CONTAINER_NAME = 'CounterContainer'

    container = database.get_container_client(CONTAINER_NAME)

    ITEM_ID = 'item2'

    item = container.read_item(ITEM_ID,partition_key='newpart')

    item['count'] += 1

    container.replace_item(ITEM_ID, item)
