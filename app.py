from flask import Flask, render_template, request
import logging

logging.basicConfig(filename='/data/logs/tools.log', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %X')

app = Flask(__name__)


@app.route('/')
def get_tools():
    # 记录来访问的ip
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        logging.info(request.environ['REMOTE_ADDR'])
    else:
        logging.info(request.environ['HTTP_X_FORWARDED_FOR'])
    return render_template('tool.html')


if __name__ == '__main__':
    app.run()
