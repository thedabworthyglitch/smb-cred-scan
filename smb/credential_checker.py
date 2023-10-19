from smbprotocol.create_contexts import CreateContextName
from smbprotocol.smb2 import SMB2Packet
from smbprotocol.smb3 import SMB2NegotiateResponse, SMB2SessionSetupRequest, \
    SMB2SessionSetupResponse, SMB2TreeConnectRequest, SMB2TreeConnectResponse, SMB2CreateRequest, \
    SMB2CreateResponse, SMB2ReadRequest, SMB2ReadResponse, SMB2QueryInfoRequest, SMB2QueryInfoResponse
import re

def connect_and_check_credentials(share_path):
    try:
        with SMB(share_path, 'username', 'password') as smb:
            files = smb.list()
            for file in files:
                if file.is_directory:
                    connect_and_check_credentials(f"{share_path}/{file.filename}")
                else:
                    with smb.create_file(file.filename, 'r') as f:
                        content = f.read()
                        # Add your credential pattern matching logic here
                        # Example:
                        if re.search(r'username=(.*?)&password=(.*?)', content):
                            print(f"Found potential credentials in {share_path}/{file.filename}")
    except Exception as e:
        print(f"Error while accessing {share_path}: {e}")

