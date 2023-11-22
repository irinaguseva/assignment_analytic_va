import json

def print_json(json_file):
    with open(json_file) as f:
        data = json.load(f)

    def print_data(data, indent=0):
        for key, value in data.items():
            print("\t" * indent + str(key) + " - " + str(value))
            if isinstance(value, dict):
                print_data(value, indent+1)
    print_data(data)

print_json("example.json")
