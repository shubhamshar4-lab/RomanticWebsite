from os import environ
from RomanticWebsite import app

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(environ.get("PORT", 8080))
    app.run(host=host, port=port)
