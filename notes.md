# Notes for Bangazon Project 

## Orders are not being completed (Issue #1)

In order_view.js module, the order was not being saved using .save(). Added order.save() to line 69 and that fixed the issue. 
```
order.save()
```

## Same user profile always returned (Issue #2) 
In profile_view.py module, the UserSerializer (line 69) was only getting the first user so I changed it to a get(username=request.auth.user) to grab the user that logged in. 
```
serializer = UserSerializer(User.objects.get(username=request.auth.user))
```

## Incorrect result for minimum products sold (Issue #3) 
* Created a products_20.py module.
* Created a TopProductList(View) 
* Created a list_with_20_products.html module to store the template to be displayed on the DOM. 

## Can't remove an item from the cart (Issue #4) 
* Commented out lines 281-282 on the product_view.py module. 
* Very hacky, need to ask why this worked and how to fix it properly!!!

## Payment type info is incorrect (Issue #5) 
On payment_type_view.py module, the data on the payment type dictionary was switched.  

```
merchant_name=request.data['acctNumber'],
acct_number=request.data['merchant']
```
Switched to 

```
merchant_name=request.data['merchant'],
acct_number=request.data['acctNumber']
```

## All payment types are being returned (Issue #6) 
* On payment_type_view.py, line 21 was returning all() payment types. 
```
payment_types = PaymentType.objects.all()
```
Switched to ...
```
payment_types = PaymentType.objects.filter(customer=request.auth.user)
```

## Get list of products over a specified price (Issue #7) 

## Increase maximum possible price (issue#8) 

## Division by zero error on products (Issue #9)

## Get products by location (Issue #10) 


## Users can favorite/unfavorite a store (Issue #11) 
Added a POST action method and a DELETE action method. On store_view.py, lines 48-60.
```
@action(methods=['post'], detail=True)
def favorite(self, request, pk):
    user = request.auth.user
    store = Store.objects.get(pk=pk)
    store.favorites.add(user)
    return Response({'message': 'Favorite Store'}, status=status.HTTP_201_CREATED)
```
```
@action(methods=['delete'], detail=True)
def unfavorite(self, request, pk):
    user = request.auth.user
    store = Store.objects.get(pk=pk)
    store.favorites.remove(user)
    return Response({'message': 'Unfavorite Store'}, status=status.HTTP_201_CREATED)
```

## User can like or dislike products (Issue #12) 
Added a POST action method and a DELETE action method. On product_view.py, lines 66-78.
```
@action(methods=['post'], detail=True)
def like(self, request, pk):
    user = request.auth.user
    product = Product.objects.get(pk=pk)
    product.likes.add(user)
    return Response({'message': 'Liked Product'}, status=status.HTTP_201_CREATED)
```
```
@action(methods=['delete'], detail=True)
def unlike(self, request, pk):
    user = request.auth.user
    product = Product.objects.get(pk=pk)
    product.likes.remove(user)
    return Response({'message': 'Unlike Product'}, status=status.HTTP_201_CREATED)
```

## TEST: Complete order by adding payment type (Issue #13) 

## TEST: New line item is not added to closed order (Issue #14) 

## TEST: Delete payment type (Issue #15)

## TEST: Delete product (Issue #16) 

## TEST: Product can be rated. Assert average rating exists. (Issue #17)

## REPORT: Expensive products (Issue #18) 
Created a products_inexpensive.py module and add an InexpensiveProductList View to iterate through the products that contain a price key that has a value of greater than 1000. 

## REPORT: Inexpensive products (Issue #19) 
Created a products_expensive.py module and add an ExpensiveProductList View to iterate through the products that contain a price key that has a value of less than 1000. 

## REPORT: Completed orders (Issue #20) 
Created an complete_orders.py module and add an CompleteOrdersList View to iterate through the orders that contain a completed_on key that has a value of NOT NULL. 

## REPORT: Incomplete orders (Issue #21) 
Created an incomplete_orders.py module and add an IncompleteOrdersList View to iterate through the orders that contain a completed_on key that has a value of NULL. 

## REPORT: Favorited sellers by customer (Issue #22) 
Created a favorited_stores.py module and add a FavoritedStoreList View to iterate through to find the stores that each customer has favorited using SQL commands. 

## Add recommended products to user profile (Issue #23) 
On the user_serializer.py module, add a recommendations field to the UserSerializer class. 
```
fields = ('username', 'first_name', 'last_name', 'orders',
                  'favorites', 'store', 'recommended_by', 'recommendations')
```