import socket
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status=200)


@app.route("/")
def home_page():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        host_addr=socket.gethostbyname(socket.gethostname()),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
