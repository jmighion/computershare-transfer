# computershare-transfer
Transfer or sell all ESPP shares from Computershare to another brokerage.

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
These are environment variables for a transfer:

* `USERNAME` : Computershare username
* `PASSWORD` : Computershare password
* `COMPANY_NAME` : Company name
* `DTC` : DTC for brokerage
* `ACCOUNT_NUMBER` : Account number for brokerage

`DTC` and `ACCOUNT_NUMBER` are not needed for selling.

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

### Usage

#### Transfer

In a terminal, run `python transfer.py`.
Selenium will open a headless Chrome window (aka you won't see anything) and automate the transfer of all whole shares to your chosen brokerage.

#### Sell

An electronic payment needs to be setup for a sale to avoid fees and charges.

In a terminal, run `python sell.py`.
Selenium will open a headless Chrome window (aka you won't see anything) and automate the sale of all shares to the first electronic payment option.

Multiple electronic payment options have not been tested.

# Warning

This will transfer all whole shares to your chosen brokerage or sell all shares to the first electronic payment option.

Use at your own risk.
