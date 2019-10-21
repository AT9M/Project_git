import sys
file_to_write ='''import requests
from twilio.rest import Client

account_sid ="AC6a6f62dbaf928dab9d849e25d1412efb" # Put your Twilio account SID here

auth_token ="25380b677c458cbfca4abc0eea9bdce0" # Put your auth token here


Number_list = ["+33617966728","+33609062820"]
def display_position():
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    
    a=("latitude "+geo_data['latitude'],"longitude "+geo_data['longitude'],geo_data['city'],geo_data['region'],geo_data['country'])
   
    str =  ' \n--   '.join(a) 
    return str

if __name__ == '__main__':
    
    client = Client(account_sid, auth_token)
    for i in Number_list:
       
       
        message = client.api.account.messages.create(

        to=str(i), # Put your cellphone number here

        from_="+447588675953", # Put your Twilio number here

        body="\n\nJacket alert system press \n SEND EMERGENCY COORDONATE : \n--   "+display_position())

'''
# define the name of the output file
filename = "geolocation2.py"

# preserve the stdout channel
original = sys.stdout

# define content
filecontent = [file_to_write]

with open(filename, 'w') as filehandle:
    # set the new output channel
    sys.stdout = filehandle
     
    for line in filecontent:
        print(line)
     
    # restore the old output channel
    sys.stdout = original