SELECT c.*
FROM memberinfo m
JOIN cardiodiagnosis c
ON m.member_id = c.memberinfo_member_id
WHERE m.firstname LIKE 'a%';
