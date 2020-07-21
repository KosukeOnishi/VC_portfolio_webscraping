import csv
import argparse
import asyncio
import sys
import time

import scraping
import crunchbase_api_client as client

parser = argparse.ArgumentParser()
parser.add_argument('arg1', help='company type', type=str)

args = parser.parse_args()

types = ["all", "commerce", "technologies", "game", "media", "education", "cloud", "ad", "iot", "fintech", "other"]
if not args.arg1 in types:
    # If type is not validate -> exit this program
    print("Error!")
    print("Argument should be... all | commerce | technologies | game | media | education | cloud | ad | iot | fintech | other")
    sys.exit()

if __name__=='__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    companies = []
    if not args.arg1 == "all":
        scrapingResult = loop.run_until_complete(scraping.getScrapingResult(args.arg1))
        companies = client.getODMs(scrapingResult)
    else:
        types.pop(0)
        for type in types:
            scrapingResult = loop.run_until_complete(scraping.getScrapingResult(type))
            companies += client.getODMs(scrapingResult)

    label = [
        'name', 'region', 'status', 'type', 'detailed_data',
        'short_description', 'homepage_url', 'profile_image_url', 'city'
    ]
    file = open('./results/{}_result.csv'.format(args.arg1), 'w')
    w = csv.writer(file)
    w.writerow(label)
    w.writerows(map(lambda x: x.getData(), companies))
    file.close()

    end = time.time()
    duration = end - start
    print("execution time: {:.1f} seconds".format(duration))
