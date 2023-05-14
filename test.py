import requests
import config

if __name__ == '__main__':
    file_path1 = config.INPUT_FILE_PATH_1
    file_path2 = config.INPUT_FILE_PATH_2
    BASE_URL = config.BASE_URL
    response = requests.get(BASE_URL + "/" + file_path1 + "/" + file_path2)
    print(response.json())
