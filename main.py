import csv
import requests          
import json              
from pprint import pprint
from ytd import download_video

key = ''
if not key:
    from settings import trello_key 
    key = trello_key

token = ''
if not token:
    from settings import trello_token 
    token = trello_token

list_id = ''
if not list_id:
    from settings import trello_list_id 
    list_id = trello_list_id

# fields = u'id,name,desc'


base = 'https://api.trello.com/1/'
params_fields_key_and_token = '?fields=id,name,desc&key=' + key + '&token=' + token 
list_url = base + 'lists/' + list_id + '/cards' + params_fields_key_and_token
# params_key_and_token = {'fields':fields,'key':key,'token':token}
response = requests.get(list_url)

print(response.url)
#pprint(response.json())
print('API response code: ', response.status_code)
response_array_of_dict = response.json()
# for card in response_array_of_dict:
#     print(card['id'] + '\t' + card['name'])


new_ids = list(card['id'] for card in response_array_of_dict)

with open('youtube-dl_downloads.json') as json_data:
    d = json.load(json_data)
    #print(d)
    old_ids = list(card['id'] for card in d)
    #print(old_ids)

download_count = 0
for i in new_ids:
    if i not in old_ids:
        #print(str(i) + " \t NOT there")
        for card in response_array_of_dict:
            if(card['id'] == i):
                download_count += 1
                print('\n Downloading...' + '\t' + card['desc'])
                link = [card['desc']]
                download_video(link)

# TODO: Add exceptions and a directory to download the files
if download_count == 0:
    print('\nNo new videos to download')

with open('youtube-dl_downloads.json', 'w') as outf: 
    json.dump(response_array_of_dict, outf)
print('\n --- local list updated --- \n')

