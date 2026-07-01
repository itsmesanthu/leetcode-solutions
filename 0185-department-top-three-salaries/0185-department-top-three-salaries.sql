SELECT Department,Employee , Salary
FROM(SELECT  
D.NAME AS Department,
E.NAME AS Employee,
E.SALARY AS Salary,
DENSE_RANK() OVER(PARTITION BY E.departmentId
 ORDER BY E.SALARY DESC) AS SAL_RANK FROM Employee E JOIN Department D ON E.departmentId =D.ID) T WHERE SAL_RANK<=3;