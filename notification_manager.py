from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = "AC0634ba369fb617ac04e195e42c286fef"
        self.auth_token = "2668605a154e538e45e850de8eaa2f30"
        self.client = Client(self.account_sid, self.auth_token)
        self.my_mail = "behealing.therapy@gmail.com"
        self.mail_pass = "gumwqwhsthuveqbc"

    def send_msg(self, data: dict):
        if int(data["stop_over"][0]) == 0:
            body = f"Low price alert! Only {data['price']} USD to fly to " \
                   f"{data['city_to']}-{data['fly_to']}, from {data['date_from']} " \
                   f"to {data['date_to']}"
        else:
            body = f"Low price alert! Only {data['price']} USD to fly to " \
                   f"{data['city_to']}-{data['fly_to']}, from {data['date_from']} " \
                   f"to {data['date_to']} with {data['stop_over'][0]} stopover in " \
                   f"{data['stop_over'][4:]}."

        message = self.client.messages.create(
            body=body,
            from_="+15863937431",
            to="+51987770717"
        )

        print(message.status)

    def send_email(self, data: dict, to_who):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_mail, password=self.mail_pass)
            if int(data["stop_over"][0]) == 0:
                message = f"Only {data['price']} USD to fly to " \
                       f"{data['city_to']}-{data['fly_to']}, from {data['date_from']} " \
                       f"to {data['date_to']}"
            else:
                message = f"Only {data['price']} USD to fly to " \
                       f"{data['city_to']}-{data['fly_to']}, from {data['date_from']} " \
                       f"to {data['date_to']} with {data['stop_over'][0]} stopover in " \
                       f"{data['stop_over'][4:]}."

            connection.sendmail(
                from_addr=self.my_mail,
                to_addrs=to_who,
                msg=f"Subject:Flights Low Price Alert\n\n{message}\n\nClick here: {data['link']}"
            )
