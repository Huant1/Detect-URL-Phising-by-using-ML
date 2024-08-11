from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form['input_data']
        return render_template('index.html', input_data=input_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
