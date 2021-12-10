from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('customer.html',views.customer,name='customer'),
    path('create_user.html',views.create_user,name='create_user'),
    path('transfer.html',views.transfer,name='transfer'),
    path('transaction.html',views.transaction,name='transaction'),
    path('transaction_history.html',views.transaction_history,name='transaction_history'),
]