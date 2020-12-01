from meli_sdk import Meli
from mercadolibre.exceptions import TokenExpired
from product_request_model import ProductResponseModel
from access_token_meli import AccessToken
import json


class Product:
    def __init__(self, client_id, client_secret, item_id, site):  
        self.client_id = client_id
        self.client_secret = client_secret
        self.site = site
        self.item_id = item_id
        
        self.meli = Meli(
            client_id = client_id,
            client_secret = client_secret,
            access_token = AccessToken(
                    client_id = client_id,
                    client_secret = client_secret,
                    site=site).get_token("access_token"))


    # Get product from MercadoLibre
    def get_product(self):
        try:
            response = self.meli.get(("items/{x}?include_attributes=all").format(x = self.item_id))
            result = ProductResponseModel(response.text)
            return result
        except TokenExpired:
            print("Your access key has expired. Generating a new one...")
            return AccessToken(self.client_id, self.client_secret, self.site).get_access_token()
        
    # Update product price from MercadoLibre
    def update_product_price(self, price):
        body = {"price":price}
        try:
            response = self.meli.put(("/items/{x}").format(x = self.item_id), body, {'access_token':self.meli.access_token})
            if response.status_code == 401:
                print("Invalid token! Unable to change price.")
            return response.ok
        except TokenExpired:
            print("Your access key has expired. Generating a new one...")
            return AccessToken(self.client_id, self.client_secret, self.site).get_access_token()
