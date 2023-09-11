#json-to-toml.py
import toml

output_file = ".streamlit/secrets.toml"

with open(".streamlit\\futanalitica-firebase-adminsdk-iqmto-e5cb044b9c.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)