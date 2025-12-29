SELECT a.state, COUNT(DISTINCT m.member_id) AS count
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN wearabledevicedata w
  ON c.cardio_id = w.cardiodiagnosis_cardio_id
JOIN xray x
  ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s
  ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE c.cardioarrestdetected = 1
  AND w.slope = 2
GROUP BY a.state;
