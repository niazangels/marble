from collections.abc import Iterable
from wsgiref.simple_server import make_server

class Server:

    def __init__(self):
        self.ROUTER = {}
        self.default_response = [b'This route does not exist yet :(']

    def route(self, route, fn):
        self.ROUTER[route] = fn

    def webserver(self, env, start_response):
        
        path_info = env['PATH_INFO']
        query_string = env['QUERY_STRING']
        response = None

        route = self.ROUTER.get(path_info, None)
        
        if route:
            status, headers = '200 OK', []
            route_response = route(query_string)
            if route_response:
                if isinstance(route_response, str):
                    response = [route_response.encode()] 
            else:
                response = self.default_response 
        else:
            status, headers = '404 NOT FOUND', []
            response =  self.default_response #try unicode
        
        start_response(status, headers)
        return response

    def start(self, host, port):
        server = make_server(host, port, self.webserver)
        print(f"Server running on {host}:{port}")
        server = server.serve_forever()
