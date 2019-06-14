import requests
import argparse

class Mac_address:
    def __init__(self,mac_address):
        self.api_key=self.get_api_key()+"{}".format("wACx_ta")
        self.api_key=self.api_key[::-1]
        self.address="api.macaddress.io"
        self.api_version="v1"
        self.key1="apiKey"
        self.url = "https://{}/{}?{}={}&output=json&search={}".format(self.address,self.api_version,self.key1,self.api_key,mac_address)
        self.get_mac_address()

    def get_api_key(self):
        key=self.decrypt("6jGBLJdqTxPz3612NUhBQa")
        return key

    def decrypt(self,key):
        return "m4Q{}".format(key)

    def print_company_name(self,data):
        if(data==None):
            print("Invalid address")
        else:
            company=(data['vendorDetails']['companyName'])
            if(company==""):
                print("Invalid Mac address provided")
            else:
                print("Associated company name for given mac_address  :  {}".format(company))
    def get_mac_address(self):
        data = requests.get(self.url)
        if(data.status_code==200):
            self.print_company_name(data.json())
        else:
            print("Unable to connect to api, Please try again later")

def parse_args():
    parser=argparse.ArgumentParser("MAC Address tool for searching company online")
    parser.add_argument("--mac_address",default="test",help="Provide mac address to which this tool is used")
    return parser.parse_args()

if __name__=="__main__":
    args=parse_args()
    mac_address=vars(args)['mac_address']
    address=Mac_address(mac_address)

