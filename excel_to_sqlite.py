import pandas as pd
import sqlite3

pozicije = pd.read_excel(
    'proracun_2022.xlsx', 
    sheet_name='podaci', 
    header=0
    )

db_connnect = sqlite3.connect('db.sqlite3')

cursor = db_connnect.cursor()

cursor.execute(
    """
    DROP TABLE IF EXISTS pozicija
    """
)

cursor.execute(
    """
    CREATE TABLE pozicija (
        id int NOT NULL,
        godina INTEGER  NOT NULL,
        pozicija_sifra varchar(255)  NOT NULL,
        konto3 INTEGER NOT NULL,
        pozicija_naziv varchar(255)  NOT NULL,
        planirano REAL,
        razdjel varchar(255)  NOT NULL,
        glava varchar(255)  NOT NULL,
        program varchar(255)  NOT NULL,
        aktivnost varchar(255)  NOT NULL,
        kategorija varchar(255)  NOT NULL,
        podkategorija varchar(255)  NOT NULL,
        PRIMARY KEY (id)
        );
     """
)

pozicije.to_sql('pozicija', db_connnect, if_exists='append', index=False)

print(pd.read_sql("SELECT * FROM pozicija LIMIT 5", db_connnect))
