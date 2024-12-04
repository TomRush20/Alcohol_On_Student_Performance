-- How does alcohol consumption affect academic performance by Workday
SELECT 
	g.final_grade,
	AVG(s.workday_alcohol) as "Average Workday Consumption"  
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Workday Consumption" DESC;

-- Overview
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