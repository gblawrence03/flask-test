from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text_field = request.form['text_field']
    return f"you entered {text_field}"

if __name__ == "__main__":
    app.run(debug=True)