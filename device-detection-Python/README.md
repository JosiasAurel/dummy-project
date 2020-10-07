
# Detect device type in web app

### Dependencies
 - Flask
 - device-detector

## Explanation
 When a browser sends a request of any type to a server, it sends it along with some headers which include a header called ```User-Agent```. This header contains info about the device which sent the request and the browser used, device OS version and more.
 Here we are using flask to create a basic server to test that. we will use flask request object to access the headers and the User-Agent part of it as such 
 ```python 
 request.headers["User-Agent"] 
 ```
 
 We can then use device detector to detzct the device type.
 
 ## Install
 
 ```bash 
 pip install -r requirements.txt 
 ```