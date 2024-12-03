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

-- How does alcohol consumption affect academic performance by Weekend
SELECT 
	g.final_grade,
	AVG(s.weekend_alcohol) as "Average Weekend Consumption" 
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Weekend Consumption" DESC;
	
-- Does Studying less or drinking more have a more affect on academic performance
SELECT 
	AVG(s.study_time) as "Average Study Time" , -- numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours
	g.final_grade
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Study Time" DESC;

SELECT 
	(AVG(s.weekend_alcohol) + AVG(s.workday_alcohol)) / 2 as "Average Alcohol Consumption Week" ,
	g.final_grade
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Alcohol Consumption Week" DESC;

SELECT 
	(AVG(s.weekend_alcohol) + AVG(s.workday_alcohol)) / 2 as "Average Alcohol Consumption Week" ,
	AVG(s.study_time) as "Average Study Time" ,
	g.final_grade ,
	CASE 
		WHEN "Average Alcohol Consumption Week" > AVG(s.study_time)
			THEN "Drinking More Effect"
		ELSE
			"Studying More Effect"
	END as "More Effect"
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade;