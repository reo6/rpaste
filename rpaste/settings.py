from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / "db.json"
ID_LENGTH = 3
DATE_FORMAT = r"%Y-%m-%d %H:%M"
