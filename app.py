from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/list')
def index_list_all():
    return ""

if __name__ == '__main__':
    app.run()
