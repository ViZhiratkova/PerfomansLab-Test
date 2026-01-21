import json
import sys

def make_a_report(tests, values_dict):
    for item in tests:
        if 'id' in item and item['id'] in values_dict:
            item['value'] = values_dict[item['id']]
        if 'values' in item:
            make_a_report(item['values'], values_dict)

def main():
    values = sys.argv[1]
    tests = sys.argv[2]
    report = sys.argv[3]
    with open(tests) as file:
        data = json.load(file)
        tests_data = data['tests']

    with open(values) as file:
        values_data = json.load(file)

    values_dict = {}
    for item in values_data['values']:
        values_dict[item['id']] = item['value']

    make_a_report(tests_data, values_dict)

    with open(report, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    main()