WITH filtered AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
groups_cte AS (
    SELECT *,
           id - rn AS grp
    FROM filtered
)
SELECT id,
       visit_date,
       people
FROM groups_cte
WHERE grp IN (
    SELECT grp
    FROM groups_cte
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;