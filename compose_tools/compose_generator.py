import yaml

# Define the base structure of your docker-compose.yml
compose_dict = {
    'version': '3.8',
    'services': {}
}

def represent_list_in_flow_style(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)

yaml.add_representer(list, represent_list_in_flow_style, Dumper=yaml.SafeDumper)


with open('docker-compose.yml', 'w') as file:
    for i in range(2):
        service_name = f'hello{i+1}'
        compose_dict['services'][service_name] = {
            'build': '.',
            'image': 'hello:latest',
            'volumes': ['./hello:/usr/src/app/hello'],
            'command': ["python", "./main.py", "-r", str(i+3)]
        }
    yaml.dump(compose_dict, file, Dumper=yaml.SafeDumper, default_flow_style=False, sort_keys=False)