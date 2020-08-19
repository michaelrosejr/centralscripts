import requests, json
# import pyarubacentral


#
# You must set the access_token before using this script
# or use the pyarubacentral module
#

access_token = "srGPDPZ2DvDd4PzbxdlAYoYFdRtWB9uz"

# Set the serial number for the device you want to move
# serialnum = "DeviceSerialNumber"
serialnum = "PHK3KPP0ZX"
services = "dm"

def unassign_device(access_token, serialnum, services):
    # US-2 URL
    URL = "https://apigw-prod2.central.arubanetworks.com/licensing/v2/subscriptions/unassign"
    data = {
        "serials":[
            serialnum
            ],
        "services":[
            services
        ]
        }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token,
        }
    post = requests.post(URL, headers=headers, data=json.dumps(data))
    return(post.status_code, post.text)

def list_services(access_token):

    # US-2 URL
    URL = "https://apigw-prod2.central.arubanetworks.com/licensing/v2/subscriptions/stats"
    querystring = {"license_type":"all"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token,
        }
    post = requests.get(URL, headers=headers, params=querystring)
    return(post.status_code, post.text)

if __name__ == "__main__":
    print(unassign_device(access_token, serialnum, services))