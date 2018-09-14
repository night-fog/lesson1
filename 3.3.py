import requests

url = 'https://ucbe06a8b78ee92741799a07f648.dl.dropboxusercontent.com/cd/0/get/AQfvESz9dyfog_4oPM3q1TMN-ET3jcOOYyl1pxC31pZGw8flKehw0moCFK7RSRMyXcBuhVhBm7VnnTmKSZ9ub7LTyLJonsX6NBhuG_RxfRD12P13-UlqabW3sraCNa1--NuLEipOa0GL-KAmeNbcQlxZv-xis0AB5dMILUFGyfAXmDLAK61Xfw1KKBxcZYFrm2-xJj0B9qO6epPPjviWji4h/file?_download_id=962436990263194490313827075275695354997815956691617032407422686&_notify_domain=www.dropbox.com&dl=1'
downloaded_filename = 'data.txt'
with open(downloaded_filename, 'wb') as f:
    resp = requests.get(url, verify=False)
    f.write(resp.content)

with open(downloaded_filename, 'r', encoding='utf-8') as f:
    print(f.read())
