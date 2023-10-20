import os
import re
import time
import logging
import yaml

def load_configuration():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def connect_and_check_credentials(share_path, config, depth=0):
    try:
        if depth > config['max_directory_depth']:
            return

        # Throttling
        time.sleep(config['throttle_delay'])

        for root, dirs, files in os.walk(share_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                if os.path.getsize(file_path) > config['max_file_size']:
                    logging.warning(f"File size exceeded limit: {file_path}")

                _, file_extension = os.path.splitext(file_path)
                if file_extension not in config['allowed_file_types']:
                    continue

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    # Credential pattern matching logic
                    credential_pattern = re.compile(r'username=(.*?)&password=(.*?)', re.IGNORECASE)
                    matches = credential_pattern.findall(content)

                    if matches:
                        for match in matches:
                            username, password = match
                            logging.warning(f"Found potential credentials in {file_path}:")
                            logging.warning(f"Username: {username}")
                            logging.warning(f"Password: {password}")

    except Exception as e:
        logging.error(f"Error while accessing {share_path}: {e}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/smb_cred_scan.log'),
            logging.StreamHandler()
        ]
    )

    config = load_configuration()
