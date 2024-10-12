from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_name = None
    result_id = None
    if request.method == 'POST':
        name = request.form.get('name')
        id= request.form.get('id')
        result_name=name
        result_id=id
    return render_template('Lab2.html', result_name=result_name, result_id=result_id)

if __name__ == '__main__':
    app.run(debug=True)