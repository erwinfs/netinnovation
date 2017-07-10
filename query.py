import sys
import os
import json
import pystache
from watson_developer_cloud import DiscoveryV1

DISCOVERY_USERNAME="ddde726c-7f0c-488b-861c-dd845aa1c3f1"
DISCOVERY_PASSWORD="16DtSO03WCoD"

ENVIRONMENT_ID="7c98c384-8455-4aab-b54f-bb91065ca390"
COLLECTION_ID="74f48674-41b2-47c3-b041-df802dd451dd"

discovery = DiscoveryV1(
  username=DISCOVERY_USERNAME,
  password=DISCOVERY_PASSWORD,
  version="2017-06-25"
)

searchStr = 'Recloser'
searchFilter = ''

#searchStr = input('Enter Search ')
#searchFilter = input('Enter Filter ')

qopts = {'natural_language_query': searchStr, 'filter': searchFilter, 'passages': 'true', 'count':'1'}
qr = discovery.query(ENVIRONMENT_ID, COLLECTION_ID, qopts)

print ('No of results:' + str(qr['matching_results']))
i = 1
for res in qr['results']:
    print('Result: ' + str(i))
    print('Title: ' + res['extracted_metadata']['title'])
    print('Fine name: ' + res['extracted_metadata']['filename'])
    print('Score: ' +  str(res['score']))
    i += 1
    print ('\n------\n')
print (json.dumps(qr,  sort_keys=True, indent=2, separators=(',', ': ')))
sel = 0
# while sel > -1:
#     sel = int(input('Select result to see more information (0 to exit) '))
#     sel -= 1
#
#     res = qr['results'][sel]
#     print('\nConcepts / relevance')
#     for conc in res['enriched_text']['concepts']:
#         print(conc['text'] + ' / ' + str(conc['relevance']))
#
#     print('\nEntities / relevance')
#     for ent in res['enriched_text']['entities']:
#         print(ent['text'] +
#               ' / ' + str(ent['relevance']) )
#
#     print('\nTaxonomy / score')
#     for tax in res['enriched_text']['taxonomy']:
#         print(tax['label'] + ' / ' + str(tax['score']))




#print(json.dumps(my_query), 'Matching number of results: {{matching_results}}')
