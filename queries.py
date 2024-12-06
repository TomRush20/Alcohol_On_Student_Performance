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

#Data Overview
overview_sql = """
SELECT 
	s.student_id ,
	s.sex ,
	s.age ,
	s.parent_status ,
	s.study_time ,
	s.failures ,
	s.activities ,
	s.higher_edu ,
	s.family_relationship ,
	s.free_time ,
	s.go_out ,
	s.workday_alcohol ,
	s.weekend_alcohol ,
	s.health_status ,
	s.absences ,
	s.currently_dating ,
	s.tutored ,
	g.s1_grade ,
	g.s2_grade ,
	g.final_grade 
FROM
	student s
JOIN
	grades g
ON s.student_id = g.student_id ;
"""

overview_sql = sqlite_to_dataframe(overview_sql)

#Does alcohol consumption affect student performance?
Q1 = """
SELECT 
	g.final_grade as "Final Grade",
	AVG(s.workday_alcohol) as "Average Daily Consumption"  
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Daily Consumption" DESC;
"""
Q1 = sqlite_to_dataframe(Q1)

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

# Does being in a relationship affect drinking habits?

Q7 = """
SELECT 
    workday_alcohol AS "Workday Alcohol Consumption",
    currently_dating AS "Currently Dating",
    COUNT(*) AS "Count of Students",
    ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY currently_dating)), 1) || '%' AS "Percent of Total"
FROM student
GROUP BY workday_alcohol, currently_dating;
"""
Q7 = sqlite_to_dataframe(Q7)



Q10 = """
SELECT
	student.workday_alcohoL,
	grades.final_grade,
	COUNT(final_grade) AS final_grade_count
FROM
	student
INNER JOIN grades
		USING(student_id)
GROUP BY
	student.workday_alcohol,
	grades.final_grade
ORDER BY
	student.workday_alcohol;
"""
Q10 = sqlite_to_dataframe(Q10)
