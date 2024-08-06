from __future__ import annotations
from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: dict,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.shop_trips = {}

    def go_to_the_shop(self, shops: list[Shop]) -> Shop:
        self.amount_of_money()
        for shop in shops:
            self.get_shop_trip_cost(shop)

        shop = self.drive_to_beneficial_shop()
        return shop

    def drive_home(self) -> None:
        self.money -= (min(self.shop_trips))
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def amount_of_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def drive_to_beneficial_shop(self) -> Shop | None:
        if min(self.shop_trips) > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return None

        cheapest_shop = self.shop_trips[min(self.shop_trips)]
        print(f"{self.name} rides to {cheapest_shop.name}\n")
        return cheapest_shop

    def get_shop_trip_cost(self, shop: Shop) -> None:
        distance_price = self.get_distance_price(shop.location)
        products_price = self.get_product_price(shop.products)
        cost_of_trip = round(distance_price + products_price, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {cost_of_trip}")
        self.shop_trips[cost_of_trip] = shop

    def get_distance_price(self, shop_location: dict) -> float:
        return (
            self.get_distance(shop_location) * 2
            * Car.fuel_price * (self.car.fuel_consumption / 100)
        )

    def get_distance(self, shop_location: dict) -> float:
        """Formula for calculating distance between 2 points:
        sqrt((x2 - x1)^2 + (y2 - y1)^2)"""
        return sqrt(
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        )

    def get_product_price(self, shop_products: dict) -> float:
        return sum(
            self.product_cart[item] * price
            for item, price in shop_products.items()
        )

    @classmethod
    def get_customer_from_dict(cls, custom: dict) -> Customer:
        return cls(
            custom["name"],
            custom["product_cart"],
            custom["location"],
            custom["money"],
            Car(**custom["car"])
        )

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Product cart: {self.product_cart}\n"
            f"Location: {self.location}\n"
            f"Money: {self.money}\n"
            f"Car: {self.car}\n"
        )
