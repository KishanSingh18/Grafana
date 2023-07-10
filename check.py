import random
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


class DataHandler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        

            print("hello")
        


def run_server():
    server_address = ('localhost', 8002)
    httpd = HTTPServer(server_address, DataHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()


def run_serv():
    server_address = ('localhost', 8001)
    httpd = HTTPServer(server_address, DataHandler)
    print('Starting server on port 8001...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    run_serv()
