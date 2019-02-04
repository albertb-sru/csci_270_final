#!/usr/bin/env python3
# Made by Albert Brandt
# db_handler.py

import sqlite3;
import time;

# Log birthtest information to the logs.db file
def addLog(name, db, da, pp, cp, z):
    conn = sqlite3.connect('logs.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS logs (timestamp float, firstname text, date_birth float, days_alive int, personality_id int, chyr_id int, zodiac_id int)''')
    cur.execute("INSERT INTO logs (timestamp, firstname, date_birth, days_alive, personality_id, chyr_id, zodiac_id) VALUES ('" + str(time.time()) + "', '" + name + "', '" + str(db) + "', '" + str(da) + "',  '" + str(pp) + "', '" + str(cp) + "', '" + str(z) + "')")
    conn.commit()
    conn.close()

def getLogs():
    conn = sqlite3.connect('logs.db');

    cur = conn.cursor();
    return cur.execute('SELECT * FROM logs');

    
