SELECT EXTRACT(MONTH FROM x.date) AS month,
       COUNT(DISTINCT m.member_id) AS count
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN xray x
  ON c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE a.state = 'Special Provinces'
GROUP BY month
ORDER BY month;
