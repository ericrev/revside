#!/usr/local/bin/python2.7
#
# This was used to generate the SQL statements to add counties.
# 1. Start with base location_county in place
# 2. Load all needed counties into locations_allcounty
# 3. Run script and the needed SQL statements will be printed
# 4. Pass commands to SQL client
# 5. Further modify data or generate fixtures with dump and load as needed

import psycopg2

lines = []

try:
    conn = psycopg2.connect("dbname='revup' user='engine' host='localhost' password=''")
except:
    print "no database connection"

cur = conn.cursor()
cur.execute("SELECT name, state_id FROM locations_allcounty;")
rows = cur.fetchall()

for row in rows:
    s = "%s,%s" % (row[0], row[1])
    lines.append(s)

cur.close()
cur = conn.cursor()

for line in lines:
    words = line.split(',')
    cpre = words[0]
    county = cpre.replace("'", "''")
    state_id = int(words[1])
    qs = "SELECT * FROM locations_county WHERE name='%s' AND state_id=%d;" % (county, state_id)
    cur.execute(qs)
    r = cur.fetchall()
    if not r:
        print "INSERT INTO locations_county(name, state_id) VALUES('%s', %d);" % (county, state_id)
