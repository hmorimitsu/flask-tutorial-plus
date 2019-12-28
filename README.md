# Flask Tutorial Plus

This repository contains a modified version of the official [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial).
The code of the tutorial was adapted to take advantage of some common Flask libraries, including:
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/),
- [Flask WTForms](https://flask-wtf.readthedocs.io/),
- [Flask Login](https://flask-login.readthedocs.io/), and
- [Flask Migrate](https://flask-migrate.readthedocs.io/).

The application is still the same as in the original tutorial, and a significant part of the code remains unchanged.
If you are interested in learning more about the code, I recommend you check the original tutorial, which explains everything nicely.

I wrote this code mostly to learn Flask myself, but I decided to make it public in case someone else wanted to see
a relatively simple example of how to employ those Flask libraries in practice (as I did).

I did my best to follow good practices to write the code, but as I am new to Flask, I cannot guarantee everything is implemented in the best way.
I consulted a few other sources to learn about the libraries, and they are listed in the [Acknowledgements](#acknowledgements).

## Requirements

- Python 3
- Flask
- Flask SQLAlchemy
- Flask WTForms
- Flask Login
- Flask Migrate
- Flask Script

It is assumed you already have Python 3 with pip installed (if not, there are many tutorials about it).
You should also be using some type environment, such as [Virtualenv](https://virtualenv.pypa.io/en/latest/) or [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

You can install all other required libraries with the command below:
```bash
pip install flask Flask-SQLAlchemy flask-login Flask-WTF Flask-Migrate Flask-Script
```

Alternatively, if you are using an environment, and you want to install the same versions of the libraries I used when writing this code, first complete the first two steps of the [Usage](#usage) and then run:
```bash
pip install -r requirements.txt
```

## Usage

The instructions below show how to run this code using terminal in a Linux machine. If you are using another OS, you may have to adapt the instructions.

1. Clone this repository:
```bash
git clone https://github.com/hmorimitsu/flask-tutorial-plus.git
```

2. Enter the folder that was created by cloning the repository.
```bash
cd flask-tutorial-plus
```

3. Use Flask Migrate to initialize the sqlite database. If you want to use another database (such as Postgres or MySQL), you will have the edit the `DATABASE_URL` in [config.py](instance/config.py)) before starting this step.
```bash
bash manage_db.sh
```

4. If there were any error during the migration, fix them before proceeding. If there are no errors, then you can start to serve the application by running:
```bash
python app.py
```

1. Again, check for error messages and fix them. If no errors, then open a browser and enter the address informed in the terminal (tipically `http://127.0.0.1:5000/`). If everything goes well, you should see the initial page of the website.

## Acknowledgements

A significant part of the code comes from the official [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial).

Besides, the following websites were used to implement parts related to other Flask libraries:

- [https://hackersandslackers.com/your-first-flask-application](https://hackersandslackers.com/your-first-flask-application)
- [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [https://realpython.com/flask-by-example-part-1-project-setup/](https://realpython.com/flask-by-example-part-1-project-setup/)

## LICENSE

This code is licensed under the [MIT License](LICENSE).
