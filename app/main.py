import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    try:
        with open("app/config.json", "r") as config:
            config_data = json.load(config)
    except FileNotFoundError as e:
        print(e)
        return

    Car.fuel_price = config_data["FUEL_PRICE"]
    customers_dict, shops_dict = config_data["customers"], config_data["shops"]
    customers = [
        Customer.get_customer_from_dict(customer)
        for customer in customers_dict
    ]
    shops = [Shop.get_shop_from_dict(shop) for shop in shops_dict]

    for customer in customers:
        chosen_shop = customer.go_to_the_shop(shops)
        if chosen_shop:
            chosen_shop.serve_customer(customer.name, customer.product_cart)
            customer.drive_home()
