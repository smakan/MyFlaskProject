from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

def send_simple_message(address):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxf1dac46a5a31423e8892e26c35b057e6.mailgun.org/messages",
        auth=("api", "bcbcaafcfa6a47c6e401c7ad08aa199c-acb0b40c-2161098a"),
        data={"from": "Excited User <mailgun@sandboxf1dac46a5a31423e8892e26c35b057e6.mailgun.org>",
              "to": [address],
              "subject": "Subscription successful",
              "text": "Testing some Mailgun awesomness!"})

@app.route("/")
def hello():
    return "Hello World"

# @app.route("/erasmia")
# def helloErasmia():
#     return "Hello Erasmia"


@app.route("/<name>")
def helloStranger(name):
    return render_template("hello.html", name = name.title())
#
# @app.route("/goodmorning")
# def helloStranger(name):
#     return render_template("goodmorning.html", name = name.title())



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    send_simple_message(form_data["email"])
    return "All OK"


app.run(debug=True)
