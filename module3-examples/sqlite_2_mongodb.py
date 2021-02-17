"""MongoDB example using PyMongo"""
from os import getenv
import sqlite3
import pymongo
import queries as q

DBNAME = "test"
extraction_db = "rpg_db.sqlite3"


# SQLite DB
def sl_connection(extraction_db):
    """Connect to SQLite DB"""
    sl_conn = sqlite3.connect(extraction_db)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def execute_query(curs, query):
    return curs.execute(query).fetchall()


# Mongo DB
def mongo_client(password, dbname):
    """
    Using F String Formatting to add in dbname and password
    to generate client object.
    """

    client = pymongo.MongoClient(
        "mongodb+srv://nwdelafu-MacOS:{}@cluster0.dmymp.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client


def show_all(collection):
    all_docs = list(collection.find())
    return all_docs


def doc_creation(collection, curs, characters_list):
    # characters - (id, name, level, exp, hp, strength, intellegince, dexterity, wisdom)
    docs = []
    for character in characters_list:
        doc = {
            "name": character,
            # ... charactercreator_character columns
            # ... item names?
            # ... weapon names?

        }
        # docs.append(doc)
        collection.insert_one(doc)

    # collection.insert_many(docs)


if __name__ == "__main__":
    client = mongo_client(getenv("MONGO_DB_PASSWORD"), DBNAME)
    db = client.test
    sl_conn, sl_curs = sl_connection(extraction_db=extraction_db)
    character_list = execute_query(sl_curs, q.GET_CHARACTERS_TABLE)
    doc_creation(db.test, sl_curs, character_list)
