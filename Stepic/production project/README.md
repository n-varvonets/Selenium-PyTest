# Selenium-PyTest

For running project for review you need:

1) Go to necessary directory with next cmd:
- **cd Stepic/production project**

2) Execute cmd for running tests:
- **pytest -s -v --tb=line test_product_page.py**  - for all tests
- **pytest -v --tb=line --language=en -m need_review** -  for review marked tests
3) Install packages of the environment:
- **pip install -r \path\to\requirements.txt**

4) Сonfigure your web driver in **conftest.py** (by default there is my own directory to driver in 22 line - you will be have a different value)
  