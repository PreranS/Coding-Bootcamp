SELECT
  CASE
    WHEN m.age BETWEEN 40 AND 50 THEN '40-50'
    WHEN m.age BETWEEN 51 AND 60 THEN '50-60'
  END AS age_group,
  AVG(b.bloodpressure) AS avg_bp
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
GROUP BY age_group;
