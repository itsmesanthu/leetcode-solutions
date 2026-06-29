# Write your MySQL query statement below
SELECT P.firstName,P.lastName ,C.CITY,C.STATE FROM Person P  LEFT JOIN Address C ON P.personId =C.personId ;