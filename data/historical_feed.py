class HistoricalFeed:

    def __init__(self, df):

        self.df = df

        self.index = 0

    def next_candle(self):

        if self.index >= len(self.df):

            return None

        candle = self.df.iloc[self.index]

        self.index += 1

        return candle