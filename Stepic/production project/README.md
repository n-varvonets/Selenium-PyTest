# Selenium-PyTest

For running project for review you need:

1) Go to necessary directory with next cmd(if it necessary):
- **cd Stepic/production project**

2) Сonfigure your web driver in **conftest.py** (by default there is my own directory to driver in 22 line - you will be have a different value)


3) Install packages of the environment:
- **pip install -r \path\to\requirements.txt**

4) Execute cmd for running tests:
- **pytest -v --tb=line --language=en -m need_review** -  for review marked tests