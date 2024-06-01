import server


@server.app.route('/bankcompetition')
def home():
    return "Hello, world!"
