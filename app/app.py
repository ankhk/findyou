# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from extractor import *
from sqldb import *

app = Flask(__name__, static_url_path='/static')
extr = Extractor()
db = DBworker(app)


@app.route('/', methods=['post', 'get'])
def url_page():
    result = ''
    url = None
    if request.method == 'POST':
        url = request.form.get('url')  # запрос к данным формы
    if url:
        result = extr.get_from_url(url)
        db.save_to_db(result, url)
    return render_template('url.html', result=result,
                           url=url)


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




