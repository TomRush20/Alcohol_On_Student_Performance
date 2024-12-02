import sqlite3
import pandas as pd

def sqlite_to_dataframe(sql_script):
    # Create a connection to an in-memory SQLite database
    conn = sqlite3.connect('student_alcohol_data.db')
    cursor = conn.cursor()
    
    # Execute the provided SQL script
    cursor.execute(sql_script)
    
    results = cursor.fetchall()

    # Fetch column names from the cursor
    column_names = [description[0] for description in cursor.description]
    
    # Convert to DataFrame with column names
    results = pd.DataFrame(results, columns=column_names)

    
    # Close the connection
    conn.close()
    
    return results

Q8 = """
SELECT
	sex,
	round(SUM(workday_alcohol) / CAST(COUNT(sex) AS REAL),2) AS 'Male_Workday_Consumpton',
	round(SUM(weekend_alcohol) / CAST(COUNT(sex) AS REAL),2) AS 'Male_Weekend_Consumption'
FROM
	student
GROUP BY
	sex
"""
Q8 = sqlite_to_dataframe(Q8)


