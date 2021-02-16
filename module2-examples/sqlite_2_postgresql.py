"""A pipeline that transfers data from sqlite to postgreSQL"""
import sqlite3
import psycopg2
import queries as q

DBNAME = "ikvpcyhw"
USER = "ikvpcyhw"
PASSWORD = "eEMfyVIkvbd9Z2RczR2hD5rlE4hvrAp2"
HOST = "ziggy.db.elephantsql.com"

sqlite_rpg_db = "rpg_db.sqlite3"


# sqlite database handlers

def sqlite_connect(sqlite_db):
    """Returns sqlite connection"""
    sqlite_conn = sqlite3.connect(sqlite_db)
    return sqlite_conn


# PostGreSQL database handlers

def pg_connect(dbname, user, password, host):
    """Returns pg connection object"""
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    return pg_conn


def create_cursor(conn):
    """Returns cursor"""
    curs = conn.cursor()
    return curs


def execute_query(curs, query, reading=True):
    """Executes query"""
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        curs.close()
        return results

    return "This statement worked!"


def add_characters(pg_curs, character_list):
    """Grabbing characters from sqlite"""
    insert_character_statement = """
      INSERT INTO charactercreator_character
      (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
      VALUES {};
    """
    for character in character_list:
        insert_character_statement.format(character)
        pg_curs.execute(insert_character_statement)


if __name__ == "__main__":
    # creates conn and curs for pg
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    # creates conn and curs for sl
    sl_conn = sqlite_connect(sqlite_rpg_db)
    sl_curs = create_cursor(sl_conn)

    execute_query(pg_curs, q.create_character_table, reading=False)
    character_list = execute_query(
        sl_curs, q.select_all.format("charactercreator_character"))
    add_characters(pg_curs, character_list)

    # execute_query(
    #     pg_curs, q.create_test_table_statement, reading=False)
    # execute_query(pg_curs, q.test_insert_statement, reading=False)
    pg_conn.commit()

    # all_pg_data = execute_query(pg_curs, q.select_all.format("test_table"))
    # all_sqlite_data = execute_query(
    #     sl_curs, q.select_all.format("charactercreator_character"))
    # print(all_sqlite_data)
