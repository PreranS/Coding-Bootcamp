SELECT COUNT(b.blood_id) AS total_blood_tests
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.lastname = 'aberson';
