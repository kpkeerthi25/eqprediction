import urllib2
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'time': "",   
                            'latitude': "1",   
                            'longitude': "1",   
                            'place': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/9727256e6d4e43e094182a132ad823bb/services/4e2fc818a51c45d9aec71daef76a5739/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read())) 
import urllib2
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'time': "",   
                            'latitude': "1",   
                            'longitude': "1",   
                            'place': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/9727256e6d4e43e094182a132ad823bb/services/4e2fc818a51c45d9aec71daef76a5739/execute?api-version=2.0&format=swagger'
api_key = 'ykfQyqqy+/saXNHgmJWFNQnofe98cECbHV8pm1J6ZWBmnW4WjzxwTqnunLYJM8ihsmfLAodTstwDyKGdX2JzNw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read())) 
