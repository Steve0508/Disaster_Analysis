from database import get_connection

def most_affected_area():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT location, COUNT(*) AS count 
        FROM disasters 
        GROUP BY location 
        ORDER BY count DESC 
        LIMIT 5
    """)
    return cursor.fetchall()

def year_wise_disaster_count():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT YEAR(start_date) AS year, COUNT(*) 
        FROM disasters 
        GROUP BY year 
        ORDER BY year
    """)
    return cursor.fetchall()

def disaster_types_frequency():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_type, COUNT(*) 
        FROM disasters 
        GROUP BY disaster_type 
        ORDER BY COUNT(*) DESC
    """)
    return cursor.fetchall()

def top_countries_by_economic_loss():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT country, SUM(economic_loss) AS total_loss 
        FROM disasters 
        GROUP BY country 
        ORDER BY total_loss DESC 
        LIMIT 5
    """)
    return cursor.fetchall()

def population_affected_per_disaster():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_name, population_affected 
        FROM disasters 
        ORDER BY population_affected DESC 
        LIMIT 10
    """)
    return cursor.fetchall()

def total_disasters_per_country():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT country, COUNT(*) 
        FROM disasters 
        GROUP BY country 
        ORDER BY COUNT(*) DESC
    """)
    return cursor.fetchall()

def avg_duration_by_disaster_type():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_type, 
        AVG(DATEDIFF(end_date, start_date)) AS avg_duration 
        FROM disasters 
        WHERE end_date IS NOT NULL AND start_date IS NOT NULL
        GROUP BY disaster_type
    """)
    return cursor.fetchall()

def recent_10_disasters():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_name, disaster_type, start_date, location 
        FROM disasters 
        ORDER BY start_date DESC 
        LIMIT 10
    """)
    return cursor.fetchall()

def cities_with_highest_relief():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT location, COUNT(*) AS relief_count
        FROM disasters
        WHERE relief_measures_taken IS NOT NULL AND relief_measures_taken != ''
        GROUP BY location 
        ORDER BY relief_count DESC 
        LIMIT 5
    """)
    return cursor.fetchall()

def monthly_disaster_count():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT MONTH(start_date) AS month, COUNT(*) 
        FROM disasters 
        GROUP BY month 
        ORDER BY month
    """)
    return cursor.fetchall()

def relief_aid_distribution_summary():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_type, COUNT(*) AS relief_cases 
        FROM disasters 
        WHERE relief_measures_taken IS NOT NULL AND relief_measures_taken != ''
        GROUP BY disaster_type
    """)
    return cursor.fetchall()

def avg_economic_loss_by_region():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT region, AVG(economic_loss) 
        FROM disasters 
        GROUP BY region
    """)
    return cursor.fetchall()

def top_5_deadliest_disasters():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT disaster_name, deaths, location 
        FROM disasters 
        ORDER BY deaths DESC 
        LIMIT 2
    """)
    return cursor.fetchall()

def countries_with_most_floods():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT country, COUNT(*) 
        FROM disasters 
        WHERE disaster_type = 'Flood' 
        GROUP BY country 
        ORDER BY COUNT(*) DESC
    """)
    return cursor.fetchall()

def disaster_count_by_severity():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT severity_level, COUNT(*) 
        FROM disasters 
        GROUP BY severity_level 
        ORDER BY COUNT(*) DESC
    """)
    return cursor.fetchall()
