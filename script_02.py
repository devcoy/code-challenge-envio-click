import json

class Package:
    packages = []
    criteria = []

    def __init__(self, file_path, criteria):
        with open(file_path, 'r') as input_file:
            self.packages = json.load(input_file)
        input_file.close()
        self.criteria = criteria


file_path = 'input_02.json'
# criteria = [
#     ('weight', '=', 3)
# ]

criteria = [
    ('width', '>=', 2),
    ('length', '<=', 9),
]

package = Package(file_path, criteria)
