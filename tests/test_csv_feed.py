from pathlib import Path

from data.csv_feed import CSVFeed


def test_csv_feed_class_exists():
    assert CSVFeed is not None


def test_csv_feed_requires_existing_file():
    feed = CSVFeed("does_not_exist.csv")

    try:
        feed.load()
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass

def test_csv_feed_loads_dataframe():
    csv_path = Path("tests/data/sample.csv")

    feed = CSVFeed(csv_path)

    df = feed.load()

    assert len(df) == 3

    assert list(df.columns) == [
        "datetime",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]  