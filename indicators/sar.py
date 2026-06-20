from indicators.base_indicator import BaseIndicator


class ParabolicSAR(BaseIndicator):

    def __init__(self,
                 af=0.02,
                 max_af=0.20):

        self.af = af
        self.max_af = max_af

    def calculate(self, data):

        # Placeholder implementation.
        # Will replace with a full Wilder implementation later.
        return data["low"].rolling(2).min()