from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Matthew Etter in 3308"

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://glassware_db_user:BUQZeeMOe5wrTWcgSCYZkOfUMHSolGrS@dpg-dbke6lo8v5cc738cdgkg-a.oregon-postgres.render.com/glassware_db")
    conn.close()
    return "Database connection successful"


# create the initial basketball table
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://glassware_db_user:BUQZeeMOe5wrTWcgSCYZkOfUMHSolGrS@dpg-dbke6lo8v5cc738cdgkg-a.oregon-postgres.render.com/glassware_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created!"


# populate table
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://glassware_db_user:BUQZeeMOe5wrTWcgSCYZkOfUMHSolGrS@dpg-dbke6lo8v5cc738cdgkg-a.oregon-postgres.render.com/glassware_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);

    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully populated!"

# 
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://glassware_db_user:BUQZeeMOe5wrTWcgSCYZkOfUMHSolGrS@dpg-dbke6lo8v5cc738cdgkg-a.oregon-postgres.render.com/glassware_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string