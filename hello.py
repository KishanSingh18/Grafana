from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import logging
from socketserver import TCPServer 
from prometheus_client import start_http_server, Counter, Summary, Gauge
import random
import time

        
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("jfjlsd")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()    
        content = "Hello, World!"

        # Send the content as the response
        self.wfile.write(content.encode())
        
        
            
        # rr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
             
                
if __name__ == '__main__':
        
# Start up the server to expose the metrics.
    start_http_server(8000)
    my_counter1 = Gauge('my_counter5', 'My counter')
    my_counter1.set(0)
    j=0
    while(True):
            # print(n)
            j+=1
            my_counter1.set(j)
            print(j)
            logging.warning('Watch out!')
            time.sleep(1)
    # # Generate some requests.
    # logging.warning('Watch out!!!!!!')
    # webServer = HTTPServer(('localhost', 8002), MyServer)
    # print("Server started http://%s:%s" % ('localhost', 8002))
    
    
    # webServer.serve_forever()
        
    """Entrypoint for python server"""
    
    
    
        

    # import os
    # from http.server import HTTPServer, CGIHTTPRequestHandler

    # # # Make sure the server is created at current directory
    # # os.chdir('.')

    # # Create server object listening the port 80
    # server_object = HTTPServer(server_address=('', 8001), RequestHandlerClass=CGIHTTPRequestHandler)
    # # Start the web server
    # server_object.serve_forever()



# import random
# import time
# from http.server import BaseHTTPRequestHandler, HTTPServer


# class DataHandler(BaseHTTPRequestHandler):
#     def _set_response(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

#     def do_GET(self):
#         if self.path == '/data':
#             self._set_response()

#             while True:
#                 # Generate random data
#                 temperature = random.uniform(20.0, 30.0)
#                 humidity = random.uniform(40.0, 60.0)
#                 pressure = random.uniform(900.0, 1100.0)

#                 # Construct the response with simulated live data
#                 response = f"Temperature: {temperature} °C, Humidity: {humidity} %, Pressure: {pressure} hPa"
#                 self.wfile.write(response.encode())

#                 # Wait for a certain interval (e.g., 1 second)
#                 time.sleep(1)
#         else:
#             self.send_error(404)


# def run_server():
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, DataHandler)
#     print('Starting server on port 8000...')
#     httpd.serve_forever()


# if __name__ == '__main__':
#     run_server()




# import random
# import time
# from http.server import BaseHTTPRequestHandler, HTTPServer


# class DataHandler(BaseHTTPRequestHandler):
    

#     def do_GET(self):
        

#             while True:
#                 # Generate random data
#                 temperature = random.uniform(20.0, 30.0)
#                 humidity = random.uniform(40.0, 60.0)
#                 pressure = random.uniform(900.0, 1100.0)

#                 # Construct the response with simulated live data
#                 print("helo");

#                 # Wait for a certain interval (e.g., 1 second)
#                 time.sleep(1)
        


# def run_server():
#     server_address = ('localhost', 8002)
#     httpd = HTTPServer(server_address, DataHandler)
#     print('Starting server on port 8000...')
#     httpd.serve_forever()


# if __name__ == '__main__':
#     run_server()