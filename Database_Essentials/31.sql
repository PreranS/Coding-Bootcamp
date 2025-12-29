SELECT gender, COUNT(*) AS count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;
