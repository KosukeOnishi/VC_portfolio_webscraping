import requests
import re
import configparser

config = configparser.ConfigParser()
config.read('setting.ini')

def getODMs(companies):
    if len(companies) == 0:
        return

    url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"
    headers = {
        'x-rapidapi-host': config.get('development', 'host'),
        'x-rapidapi-key': config.get('development', 'key')
    }

    sum = len(companies)

    for i, company in enumerate(companies):
        queryText = getQueyText(company.name)
        locationsText = company.region
        # If locations Text is not "japan", it could be like "asia | north-america | europe...", which is not supported on this API.
        if locationsText != "japan":
            locationsText = ""
        querystring = {"query":"{}".format(queryText),"locations":"{}".format(locationsText)}

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json()

        if len(result["data"]["items"]) != 0:
            company.addExtraData(result["data"]["items"][0]["properties"])
        else:
            company.notFound()

        print("fetching data... {0}/{1}".format(i+1, sum))

    return companies

def getQueyText(name):
    queryText = re.sub(r'\s.*$', '', name)
    #remove ","
    queryText = name.split(',')[0]
    return queryText