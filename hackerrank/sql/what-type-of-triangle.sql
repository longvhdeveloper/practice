SELECT IF(a = b AND b = c, "Equilateral", IF((a = b AND a + b > c) OR (b = c AND b + c > a) OR (a = c AND a + c > b), "Isosceles", IF(a + b > c and a + c > b and b + c > a ,"Scalene","Not A Triangle")))
FROM TRIANGLES;