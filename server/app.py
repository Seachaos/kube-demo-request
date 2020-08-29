import uuid as uuid_lib
import os
import requests
from flask import Flask, request, escape

SERVER_ID = uuid_lib.uuid4().hex[4:10].upper()
print('SERVER ID:', SERVER_ID)

app = Flask(__name__)

@app.route('/info')
def api_get_info():
    """
    print server info
    """
    content = get_server_info()
    return content

@app.route('/')
def api_get_index():
    """
    fetch page info from backend_server
    """
    content = get_server_info()
    content += do_request(os.environ.get('backend_server', None))
    return content

@app.route('/request')
def api_request_with_arg():
    url = request.values.get('url', None)
    content = get_server_info()
    content += do_request(url)
    return content

def get_server_info():
    content = 'You visit SERVER ID: {}'.format(SERVER_ID) + '<br />'
    content += 'Service name:' + os.environ.get('service_name', 'undefined') + '<br />'
    content += '<hr />'
    return content

def do_request(url):
    if not url:
        return 'No request url<br />'
    if 'http' not in url:
        url = 'http://' + url

    req = requests.get(url)
    return escape(req.text)

