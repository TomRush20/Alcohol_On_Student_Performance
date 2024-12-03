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

# All students scatter plot, study & going out times
byGrade = """
SELECT final_grade as 'Final Grade' ,round(AVG(study_time),2) AS 'Average Study Ranking', round(AVG(go_out),2) AS 'Average Party Ranking'
FROM student
INNER JOIN grades
ON student.student_id = grades.student_id
GROUP BY final_grade 
ORDER BY round(AVG(study_time),2) DESC
"""
byGrade = sqlite_to_dataframe(byGrade)


# How does alcohol consumption vary among genders?
Q8 = """
SELECT
	sex as Gender,
	round(AVG(workday_alcohol),2) AS 'Workday Consumpton',
	round(AVG(weekend_alcohol),2) AS 'Weekend Consumption'
FROM
	student
GROUP BY
	Gender
"""
Q8 = sqlite_to_dataframe(Q8)

# Should students abstain from alcohol in order to do better in school?
Q6 = """
SELECT SUM((student.workday_alcohol + student.weekend_alcohol)) AS Alcohol_Consumption, grades.final_grade AS Final_Grade
FROM student
INNER JOIN grades 
ON student.student_id = grades.student_id
GROUP BY grades.final_grade
ORDER BY grades.final_grade ASC;
"""
Q6 = sqlite_to_dataframe(Q6)
