from flask import Flask, render_template
import logging

logging.basicConfig(filename='/data/logs/tools.log', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %X')

app = Flask(__name__)


@app.route('/')
def get_tools():
    logging.info("")
    return render_template('tool.html')


if __name__ == '__main__':
    app.run()
