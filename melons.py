"""Classes for melon orders."""
from random import randint
import datetime


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Get base price of melon based on Splurge Pricing"""

        base_price = randint(5, 9)
        today = datetime.datetime.now()
        hour = today.hour
        day_of_week = datetime.date.weekday(today)

        if day_of_week in range(0, 5) and hour in range(8, 11):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if "christmas" in self.species.lower():
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        # total = super().get_total()

        # if self.qty < 10:
        #     return total + 3

        # return total

        if self.qty < 10:
            total = super().get_total() + 3
        else:
            total = super().get_total()

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    order_type = "government"
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Mark melon as inspected if passed inspection."""

        if passed is True:
            self.passed_inspection = True


class TooManyMelonsError(ValueError):
    """Raise error when melon quantity is greater than 100."""

    pass