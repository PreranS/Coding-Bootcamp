SELECT COUNT(*) AS count
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
  AND m.age BETWEEN 50 AND 60;
