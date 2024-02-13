from flask import Flask, render_template
import requests

app = Flask(__name__)

# Set the URL for the ormuco-backend service. Adjust this accordingly.
BACKEND_URL = "http://localhost:45471/docs"


@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL)
        backend_data = response.text
    except requests.RequestException:
        backend_data = "Unable to connect to backend service."

    return render_template('index.html', data=backend_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
