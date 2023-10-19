import subprocess
import re

def scan_network_for_smb_shares(target_ip):
    try:
        result = subprocess.check_output(['nmap', '-p', '139,445', target_ip], universal_newlines=True)
        smb_hosts = re.findall(r'Nmap scan report for (.*?)\s', result)
        return smb_hosts
    except Exception as e:
        print(f"An error occurred while scanning the network: {e}")
        return []

