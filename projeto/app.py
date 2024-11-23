from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']
        return redirect(url_for('confirmation', message=message))
    return render_template('contato.html')

@app.route('/confirmation')
def confirmation():
    message = request.args.get('message')
    return render_template('confirmação.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)