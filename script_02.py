import json

class Package:
    packages = []
    criteria = []
    condition_property_name = ''
    condition_assignment_operator = ''
    condition_value = 0
    packages_by_criteria = []

    def __init__(self, file_path, criteria):
        with open(file_path, 'r') as input_file:
            self.packages = json.load(input_file)
        input_file.close()
        self.criteria = criteria

    def set_condition(self, condition):
        self.condition_property_name = condition[0];
        self.condition_assignment_operator = condition[1]
        self.condition_value = condition[2]

    def get_packages_by_condition(self):
        for package in self.packages:
            for condition in self.criteria:
                self.set_condition(condition)

    def get_packages_ordered(self):
        self.get_packages_by_condition()
        print(self.packages_by_criteria)
        return []


file_path = 'input_02.json'
# criteria = [
#     ('weight', '=', 3)
# ]

criteria = [
    ('width', '>=', 2),
    ('length', '<=', 9),
]

package = Package(file_path, criteria)
packages_ordered = package.get_packages_ordered()
