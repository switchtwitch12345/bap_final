from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_sneaker")
def add_sneaker():
    return render_template("add_sneaker.html")

@app.route("/saverecord", methods=["POST", "GET"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            brand = request.form["brand"]
            model = request.form["model"]
            size = request.form["size"]
            gender = request.form["gender"]
            colour = request.form["colour"]
            price = request.form["price"]
            with sqlite3.connect("sneaker_details.db") as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT into sneaker_Info (brand, model, size, gender, colour, price) values (?,?,?,?,?,?)", (brand, model, size, gender, colour, price))
                connection.commit()
                msg = "Sneaker details successfully Added"
        except Exception as e:
            print("ERROR: {}".format(e))
            msg = "We can not add Sneaker details to the database"
    return render_template("success_record.html", msg=msg)

@app.route("/delete_sneaker")
def delete_sneaker():
    return render_template("delete_sneaker.html")

@app.route("/sneaker_info")
def sneaker_info():
    connection = sqlite3.connect("sneaker_details.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from sneaker_Info")
    rows = cursor.fetchall()
    return render_template("sneaker_info.html", rows=rows)

@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("sneaker_details.db") as connection:
        cursor = connection.cursor()
        cursor.execute("select * from sneaker_Info where id=?", (id,))
        rows = cursor.fetchall()
        if not rows == []:
            cursor.execute("delete from sneaker_Info where id = ?", (id,))
            msg = "Sneaker detail successfully deleted"
        else:
            msg = "Can't be deleted"
    return render_template("delete_record.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True, port=9001)
