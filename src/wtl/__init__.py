import yaml
import os
import os.path
import requests

def load_config(config_prefix="config", config_dir=None):
    if config_dir == None:
        config_dir = os.getcwd()

    if config_dir.endswith("/"):
        config_dir = "{}/".format(config_dir)

    file_name = "{}{}.yaml".format(
        config_dir, config_prefix).replace("//", "/")
    file_name_default = "{}{}-default.yaml".format(
        config_dir, config_prefix).replace("//", "/")

    file_name_used = None
    if os.path.isfile(file_name):
        file_name_used = file_name
    elif os.path.isfile(file_name_default):
        file_name_used = file_name_default

    if file_name_used != None:
        with open(file_name_used, 'r') as stream:
            return yaml.load(stream, Loader=yaml.Loader)
    return None


def send_notify(data, notify_type, config):
    if not isinstance(config,dict):
        raise ValueError('config must be a dict')
    for f in [
        'protocol',
        'hostname',
        'port',
        'token',
        'service',
    ]:
        if f not in config or config[f] == None:
            raise ValueError('Missing {} value'.format(f))
    for f in [
        'protocol',
        'hostname',
        'token',
        'service',
    ]:
        if not isinstance(config[f],str):
            raise ValueError('{} must be a str'.format(f))
    for f in [
        'port',
    ]:
        if not isinstance(config[f],int):
            raise ValueError('{} must be a str'.format(f))

    protocol = config['protocol']
    hostname = config['hostname']
    port = config['port']
    token = config['token']
    url = '{}://{}:{}/api/sendNotify'.format(protocol, hostname, port)
    data_to_send = {}
    data_to_send["service"] = config['service']
    data_to_send["type"] = notify_type
    data_to_send["token"] = token
    data_to_send["payload"] = data
    response = requests.post(url, json=data_to_send)
    return response.json()
