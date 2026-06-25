# Write your MySQL query statement below
select emAIL
FROM PERSON
GROUP BY EMAIL
HAVING COUNT(*)>1;