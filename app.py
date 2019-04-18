from marbles import Server

def home_page(params):
    response = "<html><body><h1>Whazzzapp!</h1></body></html>"
    return response

app = Server()
app.route('/', home_page)
app.start('localhost', 8000)
