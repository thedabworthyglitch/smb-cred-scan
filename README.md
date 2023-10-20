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

#Configuration (config.yaml): Ensure that your config.yaml file is properly configured with your desired parameters, such as the throttle delay, maximum file size, maximum directory depth, and allowed file types.

#Sample config.yaml:
throttle_delay: 2  # Delay in seconds between connecting to shares
max_file_size: 1000000  # Maximum file size in bytes (1 MB)
max_directory_depth: 5  # Maximum directory depth to search
allowed_file_types:
  - .txt
  - .ini
  - .cfg
  - .config
  - .xml

#Running the Scanner: Open a command prompt or terminal and navigate to the directory containing your project files. You can run the main.py script to start scanning for SMB shares.
python main.py --target-ip 192.168.1.0/24

#Selecting an SMB Share: The script will discover SMB shares and display them. You can select an SMB share to scan for hard-coded credentials.
#Sample user interaction:
Discovered SMB Shares:
1. \\192.168.1.100\share1
2. \\192.168.1.101\share2
Select an SMB share (1, 2, ...): 1


#Scanning for Credentials: The script will then scan the selected SMB share for hard-coded credentials. If it finds any, it will log the potential credentials.
#Sample output:
2023-10-20 15:30:45 - WARNING - Found potential credentials in \\192.168.1.100\share1\file.txt:
2023-10-20 15:30:45 - WARNING - Username: myusername
2023-10-20 15:30:45 - WARNING - Password: mypassword

#Viewing Logs: The logs are saved in a file called smb_cred_scan.log and are also displayed in the terminal. You can review the log file for any potential credentials found.
```

## Required Libraries

smbprotocol, regex, argeparser, pyyaml
You can install these libraries using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

## Contribution

Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Your contributions are highly appreciated.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you respect the license terms.
