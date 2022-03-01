select o.id, u.first_name || ' ' || u.last_name as full_name, o.created_on, SUM(p.price) as total_price
from bangazon_api_order o
join auth_user u on o.user_id = u.id
join bangazon_api_orderproduct op on o.id = op.order_id
join bangazon_api_product p on op.product_id = p.id
where o.completed_on is null
group by op.order_id