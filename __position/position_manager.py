class PositionManager:

    def __init__(self):

        self.active_position = None

    def has_position(self):

        return self.active_position is not None

    def open_position(
        self,
        signal,
        entry_price,
        stop_loss,
        target_price,
        timestamp
    ):

        if self.has_position():

            return False

        self.active_position = {

            "signal": signal,

            "entry_price": entry_price,

            "stop_loss": stop_loss,

            "target_price": target_price,

            "entry_time": timestamp,

            "status": "OPEN"
        }

        return True

    def close_position(self):

        if self.active_position:

            self.active_position["status"] = "CLOSED"

        self.active_position = None

    def get_position(self):

        return self.active_position