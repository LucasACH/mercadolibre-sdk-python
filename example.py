from product_meli import Product
from access_token_meli import AccessToken


client_id = "" #[PROVIDE CLIENT_ID]
client_secret = "" #[PROVIDE CLIENT_SECRET]
item_id = "" #[PROVIDE ITEM_ID]
site = "" #[PROVIDE SITE]

# 'MLA': "https://auth.mercadolibre.com.ar",  # Argentina
# 'MLB': "https://auth.mercadolibre.com.br",  # Brasil
# 'MCO': "https://auth.mercadolibre.com.co",  # Colombia
# 'MCR': "https://auth.mercadolibre.com.cr",  # Costa Rica
# 'MEC': "https://auth.mercadolibre.com.ec",  # Ecuador
# 'MLC': "https://auth.mercadolibre.cl",  # Chile
# 'MLM': "https://auth.mercadolibre.com.mx",  # Mexico
# 'MLU': "https://auth.mercadolibre.com.uy",  # Uruguay
# 'MLV': "https://auth.mercadolibre.com.ve",  # Venezuela
# 'MPA': "https://auth.mercadolibre.com.pa",  # Panama
# 'MPE': "https://auth.mercadolibre.com.pe",  # Peru
# 'MPT': "https://auth.mercadolibre.com.pt",  # Prtugal
# 'MRD': "https://auth.mercadolibre.com.do"  # Dominicana


########## GET PRODUCT INFORMATION ##########


product_response = Product(client_id=client_id, client_secret=client_secret, site=site, item_id=item_id).get_product()

# Get product title
print("Title: {title}".format(title=product_response.title))

# Get product original price
print("Original Price: {original_price}".format(original_price=product_response.original_price))

# Get product base price
print("Base Price: {base_price}".format(base_price=product_response.base_price))

# Get seller id
print("Seller ID: {seller_id}".format(seller_id=product_response.seller_id))


########## UPDATE PRODUCT PRICE ##########


price = 0 #[PROVIDE PRICE]

Product(client_id=client_id, client_secret=client_secret, site=site, item_id=item_id).update_product_price(price)


    




