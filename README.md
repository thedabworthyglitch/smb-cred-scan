# SMB Credential Scanner

## Overview

The SMB Credential Scanner is a Python tool designed to scan a network for open SMB shares, connect to them, and check the files and scripts inside for hard-coded credentials. It aims to identify potential security vulnerabilities in your network by detecting sensitive information stored in scripts and configuration files.

## The program can be used for

Security Audits: Identify potential security risks by detecting hard-coded credentials in shared resources.
Penetration Testing: Assess the security of your network by searching for vulnerabilities.

Network Management: Ensure that sensitive information is not exposed in your SMB shares.
Note: Ensure you have proper authorization and adhere to ethical and legal guidelines when using this tool.

## Why It's Important

Storing hard-coded credentials in files or scripts is a common security mistake. Such credentials can be exploited by attackers to gain unauthorized access. This tool helps you proactively identify and rectify these issues, strengthening your network's security posture.

## Sample Usage

```bash
# Clone the repository
git clone https://github.com/thedabworthyglitch/smb-cred-scan.git
cd smb-cred-scan

# Install the required Python libraries
pip install -r requirements.txt

# Run the tool with a target IP range (e.g., 192.168.1.0/24)
python main.py --target-ip 192.168.1.0/24

# The program will scan the network for open SMB shares, list the discovered shares, and prompt you to select one interactively for credential checking.

# Optionally, you can specify an SMB share manually using the --smb-share argument
python main.py --target-ip 192.168.1.0/24 --smb-share '\\target_machine\share'
```

## Required Libraries

The following Python libraries are required for running the SMB Credential Scanner:

smbprotocol: Used for SMB operations, such as connecting to shares and interacting with files.
regex: Used for pattern matching within file contents.
argparse: Used for parsing command-line arguments.
You can install these libraries using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

## Contribution

Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Your contributions are highly appreciated.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you respect the license terms.
