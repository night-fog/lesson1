import json
import requests
import magic
import os
import zipfile
import ntpath
import os
import base64


#https://data.mos.ru/opendata/7704111479-svedeniya-o-naibolee-populyarnyh-jenskih-imenah-sredi-novorojdennyh?year=2016
URL = 'https://op.mos.ru/EHDWSREST/catalog/export/get?id=327173'
YEAR = '2016'


def download_file(url: str, result_path: str):
    try:
        r = requests.get(url, stream=True)
    except ConnectionError:
        return None
    with open(result_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return result_path


def guess_file_type(result_path: str):
    return magic.from_file(result_path, mime=True)


def unpack_zip(filepath: str, create_folder: bool=False):
    result_path = os.path.dirname(filepath)
    if create_folder:
        result_path = os.path.join(result_path,
                                   f'{ntpath.basename(filepath)}_dir')
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(result_path)
    return result_path


def extract_zip_and_get_filepath_list(zipfile_path: str):
    path = unpack_zip(zipfile_path, create_folder=True)
    file_list = list()
    for file in os.listdir(path):
        file_list.append(os.path.join(path, file))
    return file_list


def opendata_url2json(url, tmp_filename):
    if download_file(url, tmp_filename) is None:
        return False
    mime_type = guess_file_type(tmp_filename)
    if 'application/zip' == mime_type:
        files = extract_zip_and_get_filepath_list(tmp_filename)
        if len(files) <= 0:
            return False
        with open(files[0], encoding='windows-1251') as f:
            return json.load(f)
    else:
        return False


def opendata2html(json_data: dict, year: int):
    html = '<table>'
    html += '<tr><th>Имя мурысика</th></tr>'
    for item in json_data:
        if item.get('Year') == YEAR:
            html += '<tr><tr>{}</tr></tr>'.format(item.get('Name', None).strip())
    html += '</table>'
    return html


def get_newbie_names(url, file_path, year):
    json_data = opendata_url2json(url, file_path)
    if json_data is False:
        return False
    return opendata2html(json_data, year)

if __name__ == '__main__':
    print(get_newbie_names(URL, f'{os.path.dirname(__file__)}/tmp_data/homework_http.file', 2016))