SELECT ID, NAME, HOST_ID
from PLACES
where HOST_ID IN(
    select HOST_ID
    from PLACES
    group by HOST_ID
    having count(*) >=2
)
order by ID;