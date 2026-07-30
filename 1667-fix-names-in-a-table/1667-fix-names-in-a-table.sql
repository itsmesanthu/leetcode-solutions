SELECT USER_ID,
CONCAT(UPPER(SUBSTR(NAME,1,1)),LOWER(SUBSTR(NAME,2))) AS name from users
order by user_id;