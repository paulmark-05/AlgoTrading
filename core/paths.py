from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset folders
DATASETS_DIR = PROJECT_ROOT / "datasets"

RAW_DATA_DIR = DATASETS_DIR / "raw"
PROCESSED_DATA_DIR = DATASETS_DIR / "processed"
LIVE_DATA_DIR = DATASETS_DIR / "live"

# Instruments
NIFTY_RAW_DIR = RAW_DATA_DIR / "nifty"
NIFTY_PROCESSED_DIR = PROCESSED_DATA_DIR / "nifty"

# Files
RAW_NIFTY_DATA = NIFTY_RAW_DIR / "NIFTY_50_minute.csv"
PROCESSED_NIFTY_5M = NIFTY_PROCESSED_DIR / "NIFTY_5M.parquet"