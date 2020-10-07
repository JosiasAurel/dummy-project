from flask import Flask, request
from device_detector import DeviceDetector, SoftwareDetector

app = Flask(__name__)

@app.route("/")
def index():
    ua_string = request.headers["User-Agent"]
    device = SoftwareDetector(ua_string).parse()
    print(f"Client Name : {device.client_name()}")
    print(f"Client Type : {device.client_type()}")
    print(f"Client Version : {device.client_version()}")
    print(f"OS : {device.os_name()}")
    print(f"OS Version : {device.os_version()}")
    print(f"Engine : {device.engine()}")
    
    return "Detect User-Agent in python"

if __name__ == "__main__":
   app.run(debug=True)
