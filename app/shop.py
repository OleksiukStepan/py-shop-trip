from __future__ import annotations
import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: dict,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve_customer(self, cust_name: str, cust_products: dict) -> None:
        self.print_date()
        print(f"Thanks, {cust_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for item in cust_products:
            prod_price = cust_products[item] * self.products[item]
            if prod_price == int(prod_price):
                prod_price = int(prod_price)

            print(f"{cust_products[item]} {item}s for {prod_price} dollars")
            total_cost += prod_price

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    @staticmethod
    def print_date() -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))

    @classmethod
    def get_shop_from_dict(cls, shop_dict: dict) -> Shop:
        return cls(
            shop_dict["name"],
            shop_dict["location"],
            shop_dict["products"]
        )

    def __str__(self) -> str:
        return (
            f"Shop name: {self.name}\n"
            f"Shop location: {self.location}\n"
            f"Shop products: {self.products}\n"
        )
