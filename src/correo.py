import json

with open("config/config.json", "r") as config_file:
    config = json.load(config_file)

email=config["EMAIL"]
password=config["PASSWORD"]
asunto="Nuevo Video para descargar!!!"