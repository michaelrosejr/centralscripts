import requests, json
# import pyarubacentral


#
# You must set the access_token before using this script
# or use the pyarubacentral module
#

# access_token = ""

# Set the group you want to move the device into
groupname = "default"

# Set the serial number for the device you want to move
serialnum = "DeviceSerialNumber"


# US-2 URL
URL = "https://apigw-prod2.central.arubanetworks.com/configuration/v1/devices/move"
moveap = {
    "access_token": access_token,
    "group": groupname,
    "serials": [
        serialnum
    ]
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + access_token,
    }
post = requests.post(URL, headers=headers, data=json.dumps(moveap))
print("Status: {} : {}".format(post.status_code, post.text))
