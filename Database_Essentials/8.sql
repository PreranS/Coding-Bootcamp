SELECT 
    x.xray_id,
    x.date,
    x.ca
FROM memberinfo m
JOIN cardiodiagnosis c
    ON m.member_id = c.memberinfo_member_id
JOIN xray x
    ON c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE m.firstname = 'ajay'
  AND DATE(c.date) = '2019-01-26';
