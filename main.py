import argparse
import logging
import logging.handlers
import yaml
from scanner.network_scanner import scan_network_for_smb_shares
from smb.credential_checker import connect_and_check_credentials

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/smb_cred_scan.log'),
            logging.StreamHandler()
        ]
    )

def load_configuration():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def main():
    setup_logging()
    config = load_configuration()

    parser = argparse.ArgumentParser(description="SMB Credential Scanner")
    parser.add_argument("--target-ip", required=True, help="Target IP address or range (e.g., 192.168.1.0/24)")
    parser.add_argument("--smb-share", help="Manually specified SMB share (e.g., \\\\target_machine\\share)")

    args = parser.parse_args()

    target_ip = args.target_ip
    smb_share = args.smb_share

    smb_hosts = scan_network_for_smb_shares(target_ip, config)

    if smb_share:
        connect_and_check_credentials(smb_share, config)
    elif smb_hosts:
        print("Discovered SMB Shares:")
        for idx, host in enumerate(smb_hosts, start=1):
            print(f"{idx}. {host}")
        try:
            choice = int(input("Select an SMB share (1, 2, ...): "))
            if 1 <= choice <= len(smb_hosts):
                selected_share = smb_hosts[choice - 1]
                connect_and_check_credentials(selected_share, config)
            else:
                print("Invalid choice. Exiting.")
        except ValueError:
            print("Invalid input. Exiting.")
    else:
        print("No open SMB shares found in the target network.")

if __name__ == "__main__":
    main()
