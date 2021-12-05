from flask import Flask, redirect,url_for

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():  # put application's code here
    return 'Hello to home page!'

@app.route('/catalog')
def catalog_func():
    return 'Hello to catalog page!'

@app.route('/about')
def about_func():
    # todo
    # do something with db
    print('i am in about')
    return redirect('/catalog')

@app.route('/product')
def product_func():
    # todo
    # do something with db
    print('i am in product page')
    return redirect(url_for('catalog_func'))


if __name__ == '__main__':
    app.run(debug=True)
