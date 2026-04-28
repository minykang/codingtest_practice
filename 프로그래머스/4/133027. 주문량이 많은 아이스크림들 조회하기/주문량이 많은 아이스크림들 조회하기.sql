select f.FLAVOR
from FIRST_HALF as f
join JULY as j
on f.FLAVOR = j.FLAVOR
group by FLAVOR
order by f.TOTAL_ORDER + sum(j.TOTAL_ORDER) desc
limit 3;