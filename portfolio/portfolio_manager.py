class PortfolioManager:

    def __init__(self):

        self.positions = []

    def add_position(

        self,

        position
    ):

        self.positions.append(
            position
        )

    def get_open_positions(self):

        return [

            p

            for p in self.positions

            if p.status == "OPEN"
        ]

    def close_position(

        self,

        position
    ):

        position.status = "CLOSED"