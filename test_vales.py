import sys
import pandas as pd
import json

path_to_requirements = sys.argv[1]

try:
    with open(path_to_requirements) as data_file:
        requirements = json.load(data_file)
        print(requirements)

        transforms = requirements['transforms']
        print(len(transforms.items()))
        if len(transforms.items()) > 0:
            data = pd.read_csv(requirements['table_file_path'], sep=";", names=requirements['headers'],
                               usecols=requirements['headers'],
                               encoding="latin1", dtype=str, skiprows=1)
            for (column, transform_list) in transforms.items():
                for col_transform in transform_list:
                    print('key: ' + column + ' --- ' 'value: ' + str(col_transform))

            data = data.drop(["NOMBRE"], axis=1)
            data.DOCUMENTO = data["DOCUMENTO"].apply(hash)
            data.to_csv(requirements['table_file_path'], index=False, sep=";")
        else:
            print("TRANSFORMATIONS NOT FOUND")
except:
    print("ERRORS DETECTED")
