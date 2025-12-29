SELECT *
FROM memberinfo as m
JOIN addressinfo as a
ON m.member_id = a.memberinfo_member_id
WHERE city='Flora';