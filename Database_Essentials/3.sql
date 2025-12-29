SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = '2019-04-11'
ORDER BY cardioarrestdetected DESC;
