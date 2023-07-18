Readme for web_flask aka Web Framework for AirBnB

# General

## What is a Web Framework
GeeksforGeeks describes ‘web application frameworks’ or ‘web frameworks’ as “a software framework that is designed to support the development of web applications including web services, web resources and web APIs”. In simple words, web frameworks are a piece of software that offers a way to create and run web applications.
    
## How to build a web framework with Flask
A minimal Flask application looks something like this:

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

1. First we imported the Flask class. An instance of this class will be our WSGI application.

2. Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

3. We then use the route() decorator to tell Flask what URL should trigger our function.

4. The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

## How to define routes in Flask
Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.

Use the route() decorator to bind a function to a URL.

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return 'Hello, World'

You can do more! You can make parts of the URL dynamic and attach multiple rules to a function.
[resource](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing)

## What is a route
A route refers to the mapping between a URL (Uniform Resource Locator) and a specific function or handler that will be executed when that URL is requested by a client. In Flask, you can use the @app.route decorator to associate a URL with a Python function. 
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Welcome to the home page!'

    @app.route('/about')
    def about():
        return 'This is the about page.'

    @app.route('/user/<username>')
    def user_profile(username):
        return f'Profile page of {username}'

    if __name__ == '__main__':
        app.run()
In the context of web development, a route refers to the mapping between a URL (Uniform Resource Locator) and a specific function or handler that will be executed when that URL is requested by a client.

In most web frameworks, including Flask, routes are defined using decorators or similar mechanisms. In Flask, you can use the @app.route decorator to associate a URL with a Python function. Here's an example:

python

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Welcome to the home page!'

    @app.route('/about')
    def about():
        return 'This is the about page.'

    @app.route('/user/<username>')
    def user_profile(username):
        return f'Profile page of {username}'

    if __name__ == '__main__':
        app.run()

In this example, we define three routes:

1. The root URL ```/``` is associated with the home function. When a user visits the root URL, Flask will invoke the home function and return the string 'Welcome to the home page!'.

2. The URL ```/about``` is associated with the about function. When a user visits ```/about```, the about function is called, returning the string 'This is the about page.'.

3. The URL ```/user/<username>``` is a dynamic route, where ```<username>``` acts as a placeholder for a variable value. For example, if a user visits ```/user/johndoe```, Flask will execute the ```user_profile``` function with the value ```johndoe``` as the username parameter.

## How to handle variables in a route
In Flask, you can handle variables in routes by defining dynamic routes using variable placeholders. These placeholders allow you to capture values from the URL and pass them as arguments to your route functions. There are two common ways to define variable placeholders in routes: using the default syntax and specifying data types.
Using Default Syntax:

You can define a variable placeholder in a route by enclosing it within < and > symbols. For example:

    from flask import Flask

    app = Flask(__name__)

    @app.route('/user/<username>')
    def user_profile(username):
        return f'Profile page of {username}'

    if __name__ == '__main__':
        app.run()

In this example, the route /user/<username> defines a dynamic route where the <username> part acts as a variable placeholder. When a user visits a URL like /user/johndoe, Flask captures the value johndoe and passes it as an argument to the user_profile function. Inside the function, you can access this value and use it as needed.

Specifying Data Types:
You can also specify the data type of the variable placeholder in the route definition. Flask supports several built-in data types such as int, float, path, etc. For example:
    from flask import Flask

    app = Flask(__name__)

    @app.route('/user/<int:user_id>')
    def user_profile(user_id):
        return f'Profile page of user with ID {user_id}'

    if __name__ == '__main__':
        app.run()

In this case, the route ```/user/<int:user_id>``` expects the user_id variable to be an integer. If a user visits a URL like ```/user/123```, Flask will convert the captured value ```123``` into an integer and pass it as an argument to the ```user_profile``` function.

By using variable placeholders in routes, you can create flexible and dynamic routes that handle different values and parameters based on the URL. Flask's routing system makes it convenient to capture and utilize these variables within your route functions.

## What is a template
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically.

Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, any anything else.

For a reference to HTML, CSS, and other web APIs, use the MDN Web Docs.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:
    
    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)



Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

Case 1: a module:

    /application.py
    /templates
        /hello.html

Case 2: a package:

    /application
        /__init__.py
        /templates
            /hello.html

## How to create a HTML response in Flask by using a template
## How to create a dynamic template (loops, conditions…)
## How to display in HTML data from a MySQL database
