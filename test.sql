select name, quantity
from bangazon_api_orderproduct o
join bangazon_api_product p on o.product_id = p.id
group by p.name 
order by quantity desc 
limit 20 