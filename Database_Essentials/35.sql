SELECT state, COUNT(DISTINCT city) AS total_cities
FROM addressinfo
GROUP BY state;
