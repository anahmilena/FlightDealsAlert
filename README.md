# Flight Deals Alert
This Python project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course on Udemy, specifically days 39 and 40. The project is designed to search for cheap flights and send an alert message by email and/or SMS.

## Prerequisites
To run this project you will need Python 3.x installed on your computer. In addition, the following packages are required:

* requests
* twilio
* datetime
* smtplib

## Usage
To use this project, you must have a Twilio account to send SMS alerts. The notification_manager.py file uses the twilio package to send SMS alerts, so you will need to enter your Twilio credentials in this file.

You also need to create a Sheety account to store the data. The data_manager.py file uses the Sheety API to access data stored in Google Sheets.

To run the project, simply execute the main.py file. This will run the flight search and send an alert message by email or SMS if a flight is found at a lower price than the one specified in the Google Sheet.

## Authors
Udemy instructor: Dr. Angela Yu

## License
This project is licensed under the [MIT](/LICENSE) License - see the LICENSE file for details.