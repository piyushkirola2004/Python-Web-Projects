from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def load_items():
    items = {}
    try:
        with open("items.txt", "r") as file:
            for i, line in enumerate(file, start=1):
                name, price = line.strip().split(",")
                items[i] = {"name": name, "price": int(price)}
    except FileNotFoundError:
        return {}
    return items

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_items")
def get_items():
    items = load_items()
    return jsonify(items)

@app.route("/generate_bill", methods=["POST"])
def generate_bill():
    data = request.json
    purchases = data.get("purchases", [])
    bill = sum(item["total"] for item in purchases)

    bill_number = 1
    while os.path.exists(f"bill_{bill_number}.txt"):
        bill_number += 1
    bill_filename = f"bill_{bill_number}.txt"

    with open(bill_filename, "w") as bill_file:
        bill_file.write("======= Piyush Store Bill =======\n")
        for item in purchases:
            bill_file.write(f"{item['name']} x {item['qty']} = {item['total']} Rs\n")
        bill_file.write("-------------------------------\n")
        bill_file.write(f"Total Bill: {bill} Rs\n")
        bill_file.write("Thank You for Shopping!\n")
        bill_file.write("===============================\n")

    return jsonify({"bill": bill, "filename": bill_filename})

if __name__ == "__main__":
    app.run(debug=True, port = 5001)