from config.settings import settings

class CapitalManager:


    @staticmethod
    def capital_per_lot():

        return settings.get(
            "capital",
            "capital_per_lot"
        )

    @staticmethod
    def total_capital():

        return settings.get(
            "capital",
            "total_capital"
        )

    @staticmethod
    def max_lots():

        return int(

            CapitalManager.total_capital()

            /

            CapitalManager.capital_per_lot()

        )

    @staticmethod
    def required_capital(lots):

        return (

            lots

            *

            CapitalManager.capital_per_lot()

        )

    @staticmethod
    def can_allocate(lots):

        return (

            CapitalManager.required_capital(
                lots
            )

            <=

            CapitalManager.total_capital()

        )

