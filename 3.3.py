import requests


url = 'https://uca106c7fd5cbfd84abd67308ea4.dl.dropboxusercontent.com/cd/0/get/ARV7bo8-WvQmj87Lg5_IiEfLoAj910OHAwfvPNyPhkpxxhwp01-CyIlPdMWKiVCH1KKizcQJjq6pIBIGh4GkjUGKzVwvovDV_19fYP0dqVy-Zw2JKg1SU2yRWcWVSRyIgCqqidw6Pr9hWHPrc7xEfZkDbYxqe4p3TIZ78n5KX34Ogi9FBRf6FCe7iY9UapQB0ce8bDOg8E5sICwNDyt-mLoe/file?_download_id=8068836041074238965402141927586491266026920338218175555032945953&_notify_domain=www.dropbox.com&dl=1'
downloaded_filename = 'data.txt'
with open(downloaded_filename, 'wb') as f:
    resp = requests.get(url, verify=False)
    f.write(resp.content)

with open(downloaded_filename, 'r', encoding='utf-8') as f:
    print(f.read())
