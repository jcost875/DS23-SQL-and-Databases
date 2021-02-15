"""SQLite3 - Example of a connection"""
import sqlite3
import queries as q


# STEP 1 - Make a conn object to your DB
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


# STEP 2 - Make your cursor through the conn object
# STEP 4 - Execute that query
# STEP 5 - Pull the results
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


if __name__ == "__main__":
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])
    print(len(results))
