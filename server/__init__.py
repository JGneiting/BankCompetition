from flask import Flask

app = Flask("BANK Server")

import server.Routes as routes

if __name__ == "__main__":
    app.run(debug=True)
