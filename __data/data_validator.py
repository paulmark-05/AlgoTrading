class DataValidator:

    REQUIRED_COLUMNS = [
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    @classmethod
    def validate(cls, df):

        for column in cls.REQUIRED_COLUMNS:

            if column not in df.columns:

                raise ValueError(
                    f"Missing Column: {column}"
                )

        return True