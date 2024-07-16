# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, which will be the WSGI application
app = Flask(__name__)

# Define a route for the root URL ("/") and the "/home" URL
@app.route("/")
@app.route("/home")
def home():
    # Define the function that will be executed when the root URL or "/home" is accessed
    # Return a simple HTML message for the home page
    return "<h1>Welcome to the Home Page</h1>"

# Define a route for the "/welcome/<name>" URL with a dynamic segment
@app.route("/welcome/<name>")
def welcome(name):
    # Define the function that will be executed when the "/welcome/<name>" URL is accessed
    # Return a personalized welcome message
    return f"<h1>Hi {name}, you are welcome to this page</h1>"

# Define a route for the "/addition/<int:num>" URL with a dynamic integer segment
@app.route("/addition/<int:num>")
def addition(num):
    # Define the function that will be executed when the "/addition/<int:num>" URL is accessed
    # Return the result of adding 10 to the input number
    return f"<h2>Input is {num} + 10 = {num + 10}</h2>"

# Define a route for the "/addition_two/<int:num1>/<int:num2>" URL with two dynamic integer segments
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
    # Define the function that will be executed when the "/addition_two/<int:num1>/<int:num2>" URL is accessed
    # Return the result of adding the two input numbers
    return f"<h2>{num1} + {num2} = {num1 + num2}</h2>"

# Define a route for the "/about" URL
@app.route("/about")
def about():
    # Define the function that will be executed when the "/about" URL is accessed
    # Return a simple HTML message for the about page
    return "<h2>Welcome to the About Section</h2>"

# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Run the Flask application in debug mode, which provides helpful error messages and live reloading
    app.run(debug=True)
