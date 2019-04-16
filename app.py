import os

from flask import Flask, render_template, jsonify
import xlrd

app = Flask(__name__)

filename = 'data.xlsx'


def read_file(file):
    type = os.path.splitext(file)[1]
    xy = []
    if type == '.xlsx':
        data = xlrd.open_workbook(filename)
        table = data.sheet_by_index(0)
        for i in range(0, table.ncols):
            temp = {}
            temp[table.col_values(i)[0]] = table.col_values(i)[1:]
            xy.append(temp)
    elif type == 'csv':
        pass
    elif type == 'txt':
        pass
    return xy


@app.route('/get_data')
def get_data():
    xy = read_file(filename)
    return jsonify(xy)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
