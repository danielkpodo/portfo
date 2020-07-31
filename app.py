from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/works")
def works():
    return render_template("works.html")


def write_to_csv(data):
    with open("db.csv", mode="a", newline='') as file_object:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit-form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
    else:
        return "Something went wrong, try again!"


if __name__ == "__main__":
    app.run(debug=True)
