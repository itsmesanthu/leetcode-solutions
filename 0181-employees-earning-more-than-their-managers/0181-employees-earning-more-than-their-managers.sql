# Write your MySQL query statement below
SELECT E.NAME AS Employee FROM Employee E INNER JOIN Employee M ON E.managerId=M.ID WHERE E.SALARY>M.SALARY;