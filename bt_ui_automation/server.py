import subprocess
import os

from flask import Flask, render_template
app = Flask(__name__)

session = {
    'level_one': {
        'crash_browser': True
    }
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/level_one")
def level_one():

    always_crash = os.environ.get('ALWAYS_CRASH_LEVEL_ONE', False)

    if always_crash or session['level_one']['crash_browser']:
        print('Crashing browser')
        subprocess.run('pkill -f firefox', shell=True)

    session['level_one']['crash_browser'] = not session['level_one']['crash_browser']

    return render_template('level_one.html')


@app.route("/level_two")
def level_two():

    return render_template('level_two.html')


@app.route("/level_three")
def level_three():

    return render_template('level_three.html')
