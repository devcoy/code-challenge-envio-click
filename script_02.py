import json

class Package:
    packages = []
    criteria = []
    condition_property_name = ''
    condition_assignment_operator = ''
    condition_value = 0
    package_tmp = {}
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
            self.package_tmp = package;
            for condition in self.criteria:
                self.set_condition(condition)

                if self.condition_assignment_operator == '=':
                    if package[self.condition_property_name] != self.condition_value:
                        if self.packages_by_criteria:
                            self.packages_by_criteria.pop()
                        break

                elif self.condition_assignment_operator == '>':
                    if package[self.condition_property_name] <= self.condition_value:
                        if self.packages_by_criteria:
                            self.packages_by_criteria.pop()
                        break

                elif self.condition_assignment_operator == '>=':
                    if package[self.condition_property_name] < self.condition_value:
                        if self.packages_by_criteria:
                            self.packages_by_criteria.pop()
                        break

                elif self.condition_assignment_operator == '<':
                    if package[self.condition_property_name] >= self.condition_value:
                        if self.packages_by_criteria:
                            self.packages_by_criteria.pop()
                        break

                elif self.condition_assignment_operator == '<=':
                    if package[self.condition_property_name] > self.condition_value:
                        if self.packages_by_criteria:
                            self.packages_by_criteria.pop()
                        break
                if(len(self.packages_by_criteria) == 0):
                    self.packages_by_criteria.append(self.package_tmp)
                else:
                    last_package = self.packages_by_criteria[-1]
                    if(last_package['id'] != self.package_tmp['id']):
                        self.packages_by_criteria.append(self.package_tmp)

    def sort_by_bubble(self):
        items_total = len(self.packages_by_criteria)

        for i in range(items_total):
            for j in range(0, items_total - i - 1):
                if self.packages_by_criteria[j]['priority'] > self.packages_by_criteria[j + 1]['priority']:
                    self.packages_by_criteria[j], self.packages_by_criteria[j + 1] = self.packages_by_criteria[j + 1], self.packages_by_criteria[j]

    def get_distinct_packages(self):
        return [item for item in self.packages + self.packages_by_criteria if item not in self.packages or item not in self.packages_by_criteria]

    def get_packages_ordered(self):
        self.get_packages_by_condition()
        self.sort_by_bubble()
        another_packages = self.get_distinct_packages()
        self.packages_by_criteria.extend(another_packages)
        return self.packages_by_criteria;





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
print(packages_ordered)
