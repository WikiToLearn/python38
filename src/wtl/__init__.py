import yaml
import os
import os.path

def loadConfig(config_prefix="config",config_dir=None):
    if config_dir == None:
        config_dir = os.getcwd()

    if config_dir.endswith("/"):
        config_dir = "{}/".format(config_dir)

    file_name = "{}{}.yaml".format(config_dir,config_prefix).replace("//","/")
    file_name_default = "{}{}-default.yaml".format(config_dir,config_prefix).replace("//","/")

    file_name_used = None
    if os.path.isfile(file_name):
        file_name_used = file_name
    elif os.path.isfile(file_name_default):
        file_name_used = file_name_default

    if file_name_used != None:
        with open(file_name_used, 'r') as stream:
            return yaml.load(stream, Loader=yaml.Loader)
    return None
