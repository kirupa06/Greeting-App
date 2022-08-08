from flask import Flask, render_template, request, flash, redirect, url_for
import random
r = random.randint(1, 2)

app = Flask(__name__)
app.secret_key = "lol"


@app.route('/hi')
def home():
    flash("What's Ur Name")
    return render_template('index.html')


@app.route('/greet', methods=['POST', 'GET'])
def good():
    if r == 1:
        flash(str(request.form['inp_name']).upper()+"...")
        return render_template('good.html')
    else:
        flash(str(request.form['inp_name']).upper()+"...")
        return render_template('osm.html')


@app.route('/bye', methods=['POST', 'GET'])
def bye():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
