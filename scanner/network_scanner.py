from smbprotocol.smb import SMB
import logging
import time
import yaml

def load_configuration():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def scan_network_for_smb_shares(target_ip, config):
    smb_hosts = []

    try:
        # Splitting the target IP into network and mask (e.g., "192.168.1.0/24")
        network, mask = target_ip.split('/')
        mask = int(mask)

        # Checking if mask is valid (0 <= mask <= 32)
        if 0 <= mask <= 32:
            for i in range(2 ** (32 - mask)):
                target_ip = f"{network}/{i}"
                try:
                    with SMB(target_ip, 'username', 'password') as smb:
                        # Successfully connected to an SMB share
                        logging.info(f"Connected to SMB share at {target_ip}")
                except Exception as e:
                    logging.warning(f"Failed to connect to {target_ip}: {e} (not an SMB share or access denied)")
                    continue
                time.sleep(config['throttle_delay'])
        else:
            logging.error("Invalid subnet mask. Please specify a valid mask (0 <= mask <= 32).")
    except Exception as e:
        logging.error(f"Error while scanning the network: {e}")

    return smb_hosts

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
