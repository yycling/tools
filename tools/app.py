from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_tools():
    return render_template('./tool.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
