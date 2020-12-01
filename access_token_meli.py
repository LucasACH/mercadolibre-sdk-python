import csv
from mercadolibre.client import Client

class AccessToken:
    def __init__(self, client_id, client_secret, site):  
        self.client_id = client_id
        self.client_secret = client_secret
        self.site = site
        self.client = Client(client_id, client_secret, self.get_token("refresh_token"), site=site)

    # Save token to csv file
    def add_token(self, access_token, refresh_token):
        with open("tokens.csv", "w", newline = "\n") as tokens_database:
            writer = csv.DictWriter(tokens_database, fieldnames = ["token", "id"])
            writer.writerow({"token":"access_token", "id":access_token})
            writer.writerow({"token":"refresh_token", "id":refresh_token})
            ...
        print("Tokens added to database")

    # Get token from csv file
    def get_token(self, token):
        with open("tokens.csv") as tokens_database:
            tokens_database_reader = dict(filter(None, csv.reader(tokens_database)))
            return tokens_database_reader[token]

    # Generate access token
    def get_access_token(self):
        try:
            new_access_token = self.client.refresh_token()
            print("New access token: {access_token}".format(access_token = new_access_token["access_token"]))
            self.add_token(new_access_token["access_token"], new_access_token["refresh_token"])
            print("Access token successfully generated!")
        except KeyError:
            print("Unable to generate token")
            return False