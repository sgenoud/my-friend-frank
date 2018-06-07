from bloop import BaseModel, Column, String, Integer, Engine

from bloop.exceptions import ConstraintViolation


class NumberStore(BaseModel):
    key = Column(String, hash_key=True)
    value = Column(Integer)


engine = Engine(table_name_template="my-memory-{table_name}")
engine.bind(NumberStore)


def get(key):
    try:
        return engine.query(NumberStore, key=NumberStore.key == key).one().value
    except ConstraintViolation:
        return None


def set(key, value):
    update = NumberStore(key=key, value=value)
    engine.save(update)
