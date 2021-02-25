#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask_mysqldb import MySQL
from flask import request
 
mysql = MySQL()
app  = Flask(__name__)
 
#MySQL configuration
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = 'user123'
app.config['MYSQL_DB'] = 'db_name'
app.config['MYSQL_HOST']  ='localhost'
mysql.init_app(app)


@app.route("/", methods=['GET'])
def  hello_world():
    return "hello world"
 

@app.route("/api/Book", methods=['GET'])
def return_all():
    conn = mysql.connect
    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM Book")
    rows = cursor.fetchall()
 
    return jsonify({'rows': rows})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    