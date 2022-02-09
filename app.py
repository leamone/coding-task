from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))

def calculate():

    if request.method == "POST":
        calc_input = request.form["calculator_input"]

        input_obj = json.loads(calc_input)
        input_1 = input_obj.get("input1")
        input_2 = input_obj.get("input2")
        operator = input_obj.get("operator")

        result = None
        action = None
        if operator == "+":
            action = "addition"
            result = input_1 + input_2
        elif operator == "-":
            action = "subtraction"
            result = input_1 - input_2
        elif operator == "/":
            action = "division"
            result = input_1 / input_2
        elif operator == "*":
            action = "multiplication"
            result = input_1 * input_2
        calc_output = json.dumps({f"{action}_product": result}, indent=4)
        return render_template("index.html", calculator_output=calc_output)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")