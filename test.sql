select u.first_name || ' ' || u.last_name as full_name, s.name
from auth_user u
join bangazon_api_favorite f on u.id = f.customer_id
join bangazon_api_store s on f.store_id = s.id
group by full_name