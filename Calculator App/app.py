from flask import Flask, render_template, request
import numpy as np
from statistics import mean, median, mode, stdev

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        operation = request.form["operation"]
        numbers = request.form.getlist("numbers")
        try:
            nums = [float(x) for x in numbers if x.strip() != ""]
            if operation == "add":
                result = sum(nums)
            elif operation == "subtract":
                result = nums[0] - nums[1]
            elif operation == "multiply":
                result = np.prod(nums)
            elif operation == "divide":
                result = nums[0] / nums[1]
            elif operation == "mean":
                result = mean(nums)
            elif operation == "median":
                result = median(nums)
            elif operation == "mode":
                result = mode(nums)
            elif operation == "std":
                result = round(stdev(nums), 3)
            elif operation == "quantile":
                q = float(request.form.get("quantile_value", 0.5))
                result = np.quantile(nums, q)
            else:
                result = "Invalid Operation"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, port = 5002)
