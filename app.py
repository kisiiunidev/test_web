# import zipfile

# a = zipfile.is_zipfile("app1.zip")
# print(a)

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return "File server is running"

@app.route("/download/cpp.zip")
def download():
    return send_from_directory(
        "files",
        "app1.zip",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)