from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Matthew Etter in 3308"

@app.route('db_test')
def db_test():
    conn = psycopg2.connect("postgresql://glassware_db_user:BUQZeeMOe5wrTWcgSCYZkOfUMHSolGrS@dpg-dbke6lo8v5cc738cdgkg-a.oregon-postgres.render.com/glassware_db")
    conn.close()
    return "Database connection successful"
