import requests
import asyncio
from bs4 import BeautifulSoup as bs

import models.company

async def getScrapingResult(type):
    page = requests.get('https://globalbrains.com/en/portfolio')
    soup = bs(page.text, 'html.parser')

    collection = soup.find_all(id='portfolio-{}'.format(type))[0]
    companyDataList = collection.find_all("li")

    companies = []

    for companyData in companyDataList:
        name = companyData.find('img')['alt']
        region = companyData['data-region']
        status = companyData['data-status']

        company = models.company.Company(name, region, status, type)
        companies.append(company)

    return companies