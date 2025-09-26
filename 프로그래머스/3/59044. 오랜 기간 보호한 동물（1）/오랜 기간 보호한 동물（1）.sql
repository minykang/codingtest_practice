-- 코드를 입력하세요
SELECT i.NAME, i.DATETIME
from ANIMAL_INS i
left join ANIMAL_OUTS o
    on o.ANIMAL_ID = i.ANIMAL_ID
where o.ANIMAL_ID is Null
order by i.DATETIME asc
limit 3;