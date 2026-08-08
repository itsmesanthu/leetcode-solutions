select s.student_id,s.student_name,sb.subject_name,count(e.subject_name) as attended_exams
from students s cross join subjects sb 
left  join examinations e
on sb.subject_name=e.subject_name and e.student_id=s.student_id
group by s.student_id, sb.subject_name ,  s.student_name
order by s.student_id, sb.subject_name
;