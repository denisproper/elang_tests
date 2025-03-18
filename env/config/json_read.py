import os
import json

current_dir = os.path.dirname(__file__)  
config_path = os.path.join(current_dir, 'config.json')  

with open(config_path, 'r') as file:
    config = json.load(file)


link = config['link']
link_for_settings = config["link_for_settings"]
link_for_privacy_policy = config["link_for_privacy_policy"]
link_for_vocabulary = config["link_for_vocabulary"]
link_for_support = config["link_for_support"]
