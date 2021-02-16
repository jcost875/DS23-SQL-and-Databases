"""Queries for sqlite to PostGreSQL pipeline"""

select_all = """
  SELECT * FROM {};
"""

create_character_table = """
  CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
"""


# create_test_table_statement = """
#   CREATE TABLE IF NOT EXISTS test_table (
#     id SERIAL PRIMARY KEY,
#     name varchar(20),
#     age INT
#   );
# """

# test_insert_statement = """
#   INSERT INTO test_table (name, age)
#   VALUES
#   (
#     'Steven',
#     25
#   ),
#   (
#     'Alfred',
#     85
#   );
# """
