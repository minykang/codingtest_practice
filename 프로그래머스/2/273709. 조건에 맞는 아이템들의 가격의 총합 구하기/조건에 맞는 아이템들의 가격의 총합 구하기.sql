select  distinct (select sum(price)
            from item_info
        where RARITY = 'LEGEND') as TOTAL_PRICE
from item_info