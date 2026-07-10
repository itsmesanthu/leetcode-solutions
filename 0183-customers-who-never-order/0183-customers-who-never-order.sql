SELECT C.NAME AS  Customers  FROM   Customers C LEFT JOIN Orders O ON C.ID=O. customerId 
WHERE O.customerId IS NULL;