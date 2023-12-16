import unittest
import os

from flask import Flask, render_template, redirect, url_for
import pyodbc

app = Flask(__name__)

# دسته‌ای از لینک‌ها و نام تست‌ها
links = {
    'Login': '/login',
    'TestAll': '/testall',
    'About': '/about',

}

# دسته‌ای از توضیحات متناظر با هر لینک
descriptions = {
    'Login': '/login////////////',
    'TestAll': '/register///////////',
    'About': '/about///////////',
    # توضیحات مربوط به سایر لینک‌ها
}


commandBase = 'python'
login_test_path = './Test/Login.py'
testall_path = './test.py'
# تنظیمات اتصال به دیتابیس
db_connection_string = 'DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password'

try:
    cnxn = pyodbc.connect(db_connection_string)
    cursor = cnxn.cursor()
    connected_to_database = True
except pyodbc.Error as e:
    error_message = str(e)
    connected_to_database = False


@app.route('/')
def home():
    return render_template('buttons.html', links=links, descriptions=descriptions)


@app.route('/display_data')
def display_data(error_message=".اتصال به دیتابیس انجام نشد"):
    if not connected_to_database:
        return render_template('error.html', error_message=error_message)

    try:
        # بازیابی داده‌ها از دیتابیس
        query = 'SELECT * FROM your_table'
        cursor.execute(query)
        data = cursor.fetchall()
    except pyodbc.Error as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)

    # بستن اتصال به دیتابیس
    cursor.close()
    cnxn.close()

    return render_template('display_data.html', data=data)


@app.route('/login')
def login():
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(login_test_path), pattern=os.path.basename(login_test_path))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/testall')
def test_all():
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(testall_path), pattern=os.path.basename(testall_path))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
