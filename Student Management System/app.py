from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

records = []

@app.route('/clear', methods=['POST'])
def clear_records():
    records.clear()
    return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = int(request.form['roll_no'])
        hindi = int(request.form['hindi'])
        english = int(request.form['english'])
        maths = int(request.form['maths'])
        science = int(request.form['science'])
        social = int(request.form['social'])

        marks = {
            "Hindi": hindi,
            "English": english,
            "Maths": maths,
            "Science": science,
            "Social Studies": social
        }

        total = sum(marks.values())
        percentage = round(total / 5, 2)
        grade = (
            "A+" if percentage >= 90 else
            "A" if percentage >= 80 else
            "B" if percentage >= 70 else
            "C" if percentage >= 60 else
            "D" if percentage >= 50 else
            "Fail"
        )

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        records.append(student)
    return render_template('index.html', records=records)


if __name__ == "__main__":
    app.run(debug=True, port=5000)