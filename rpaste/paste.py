from tinydb import TinyDB, Query
import os
import binascii
from datetime import datetime
from .settings import ID_LENGTH, DATE_FORMAT
from dataclasses import dataclass


def generate_unique_id(db: TinyDB):
    ID = Query()
    random_id = binascii.b2a_hex(os.urandom(ID_LENGTH)).decode()

    if len(db.search(ID.id == random_id)) > 0:
        return generate_unique_id(db)

    return random_id


@dataclass
class Paste:
    content: str
    description: str
    id: str
    date: datetime

    @classmethod
    def create(cls, db: TinyDB, content: str, description: str):
        return cls(
            content,
            description,
            generate_unique_id(db),
            datetime.now(),
        )

    @classmethod
    def get(cls, db: TinyDB, id: str):
        """
        Returns a new Paste instance from the given ID and TinyDB database.
        """
        paste = db.get(Query().id == id)
        if paste is not None:
            return cls(
                paste["content"],
                paste["description"],
                paste["id"],
                datetime.strptime(paste["date"], DATE_FORMAT)
            )
        else:
            return None

    def save(self, db: TinyDB):
        if not self.content or not self.description or not self.id or not self.date:
            raise ValueError("Values cannot be empty.")
        db.insert({
            "content": self.content,
            "description": self.description,
            "id": self.id,
            "date": datetime.strftime(self.date, DATE_FORMAT)
        })
