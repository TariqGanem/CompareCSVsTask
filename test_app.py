import unittest
from main import app
import config
import json


class TestCompareCSVs(unittest.TestCase):
    client = app.test_client()
    file_path1 = config.INPUT_FILE_PATH_1
    file_path2 = config.INPUT_FILE_PATH_2
    invalid_file = config.INVALID_FILE_PATH
    url = config.BASE_URL

    def test_compare_csv_files(self):
        response = self.client.get(f'{self.url}/{self.file_path1}/{self.file_path2}')
        self.assertEqual(response.status_code, 200)
        expected_result = {
            'added': [1],
            'deleted': [3],
            'changed': [2]
        }
        self.assertEqual(json.dumps(response.json, sort_keys=True), json.dumps(json.dumps(expected_result),
                                                                               sort_keys=True))

    def test_compare_csvs_with_invalid_file(self):
        response = self.client.get(f'{self.url}/{self.file_path1}/{self.invalid_file}')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'"\'ID\'"\n')

    def test_compare_csvs_with_missing_file(self):
        response = self.client.get(f'{self.url}/{self.file_path1}/missing_file.csv')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'"File \'missing_file.csv\' not found."\n')


if __name__ == '__main__':
    unittest.main()
