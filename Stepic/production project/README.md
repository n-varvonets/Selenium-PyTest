# Selenium-PyTest
By clicking on the link from the Stepic, you can see not a separate project, but just the directory of final project
for review. For running project you need:

1) Go to necessary directory for testing project by next cmd(if you are in project root directory):
- **cd Stepic/production project**

2) Сonfigure your web driver in **conftest.py** (by default there is my own directory to driver in 22 line - you will be have a different value)


3) Install packages of the environment:
- **pip install -r requirements.txt**

4) Execute cmd for running tests:
- **pytest -v --tb=line --language=en -m need_review** -  for review marked tests