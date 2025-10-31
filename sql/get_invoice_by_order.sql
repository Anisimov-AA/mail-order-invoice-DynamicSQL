SELECT 
    o.ono AS order_num,
    c.cname AS customer_name,
    c.cno AS customer_num,
    c.zip,
    z.city,
    e.ename AS taken_by,
    o.received AS received_on,
    o.shipped AS shipped_on,
    od.pno AS part_num,
    p.pname AS part_name,
    od.qty AS quantity,
    p.prices AS price,
    (od.qty * p.prices) AS line_total
FROM orders o
JOIN customers c ON o.cno = c.cno
JOIN employees e ON o.eno = e.eno
JOIN odetails od ON o.ono = od.ono
JOIN parts p ON od.pno = p.pno
LEFT JOIN zipcodes z ON c.zip = z.zip
WHERE o.ono = %s