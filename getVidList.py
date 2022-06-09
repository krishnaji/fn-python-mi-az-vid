
from azure.identity import  ManagedIdentityCredential,DefaultAzureCredential
import requests

# If running from Azure ( Functions or App Service) Uncomment Below

# managed_identity = ManagedIdentityCredential(client_id='<user-assinged-idenity')

# If running From VS CODE, Login to Azure and uncomment below
managed_identity = DefaultAzureCredential()

token = managed_identity.get_token('https://management.azure.com/.default').token

headers = {
    'Authorization': 'Bearer ' + token
}

body = { 
    "permissionType": "Reader",
    "scope" : "Account"
}


getVidToken = requests.post('https://management.azure.com/subscriptions/<subscription-id>/resourceGroups/<rg-name>/providers/Microsoft.VideoIndexer/accounts/<accountname>/generateAccessToken?api-version=2022-04-13-preview',headers=headers,json=body).json()['accessToken']

print(getVidToken)

param = {'accessToken': getVidToken}

getVidList = requests.get('https://api.videoindexer.ai/eastus2/Accounts/<account-id>/Videos?',params=param)

print(getVidList.json()['results'])
