class SignalResult:

    def __init__(
        self,
        signal,
        price,
        stop_loss=None,
        reason=""
    ):

        self.signal = signal

        self.price = price

        self.stop_loss = stop_loss

        self.reason = reason

    def __str__(self):

        return (
            f"Signal={self.signal}, "
            f"Price={self.price}, "
            f"SL={self.stop_loss}, "
            f"Reason={self.reason}"
        )