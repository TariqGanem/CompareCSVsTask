import json
import pandas as pd
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except pd.errors.ParserError:
        raise ValueError(f"Error parsing CSV file '{file_path}'.")
    except Exception as ex:
        raise Exception(f"Error reading CSV file '{file_path}': {str(ex)}")


def compare_csv_files(file_path1, file_path2):
    try:
        df1 = read_csv_file(file_path1)
        df2 = read_csv_file(file_path2)
        first_file_ids = set(df1['ID'])
        second_file_ids = set(df2['ID'])

        added_ids = list(first_file_ids - second_file_ids)
        deleted_ids = list(second_file_ids - first_file_ids)
        changed_ids = []
        for id_number in first_file_ids & second_file_ids:
            if df1[df1["ID"] == id_number].values.tolist() != df2[df2["ID"] == id_number].values.tolist():
                changed_ids.append(id_number)

        result = {
            'added': added_ids,
            'deleted': deleted_ids,
            'changed': changed_ids
        }
        return json.dumps(result)
    except Exception as ex:
        return str(ex), 500


class CompareCSVs(Resource):
    def get(self, file_path1, file_path2):
        return compare_csv_files(file_path1, file_path2)


api.add_resource(CompareCSVs, "/<string:file_path1>/<string:file_path2>")

if __name__ == '__main__':
    app.run(debug=True)
