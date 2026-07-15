SELECT U.NAME AS name,ifnull(sum( R.distance),0) as travelled_distance  FROM Users U left JOIN RIDES R ON U.ID=R.USER_ID
group by u.id,u.name
ORDER BY travelled_distance  DESC, u.name ASC;