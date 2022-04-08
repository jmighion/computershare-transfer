# computershare-transfer
Transfer ESPP shares from Computershare to another brokerage

---

### Dependencies:
* selenium
* webdriver-manager
* Chrome for the webdriver
* python-dotenv

---

### Installation/Setup:
* Install dependencies using `pip install -r requirements.txt`
* Install Chrome

#### Variables:
These are environment variables:

* `USERNAME` : Computershare username
* `PASSWORD` : Computershare password
* `COMPANY_NAME` : Company name
* `DTC` : DTC for brokerage
* `ACCOUNT_NUMBER` : Account number for brokerage

You can define using whatever method works best for you (`export` in `.bash_profile`, define in Python console, or just define in the script), or you can create a .env file in the following format:
```
# .env file
USERNAME=username1
PASSWORD=password
COMPANY_NAME=company
DTC=0000
ACCOUNT_NUMBER=X12345678
```
---

### Usage:

In terminal, run `python transfer.py`. Selenium will open a new Chrome window and automate the transfer of all whole shares to your chosen brokerage.

# Warning

This is incomplete and still needs cleanup. If it works, this will transfer all whole shares to your chosen brokerage.

Use at your own risk.
