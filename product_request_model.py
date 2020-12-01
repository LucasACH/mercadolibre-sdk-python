from datetime import datetime
import json


class ProductResponseModel:
    id: str
    site_id: str
    title: str
    subtitle: str
    seller_id: int
    category_id: str
    official_store_id: int
    price: int
    base_price: int
    original_price: int
    currency_id: str
    initial_quantity: int
    available_quantity: int
    sold_quantity: int
    buying_mode: str
    listing_type_id: str
    start_time: datetime
    stop_time: datetime
    condition: str
    permalink: str
    thumbnail_id: str
    thumbnail: str
    secure_thumbnail: str
    video_id: str
    accepts_mercadopago: bool
    international_delivery_mode: str
    listing_source: str
    status: str
    warranty: str
    domain_id: str
    automatic_relist: bool
    date_created: datetime
    last_updated: datetime
    health: int
    catalog_listing: bool

    def __init__(self, response):
        self.__dict__ = json.loads(response)



    