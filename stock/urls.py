from stock.views import stock_list, stock_detail, stock_buy, stock_sell, account

from django.urls import path

from stock.views import stock_list

from stock.views import stock_list, stock_detail, stock_buy



urlpatterns = [
    path('list/', stock_list, name='list'),
    path('detail/<int:pk>/', stock_detail, name='detail'),
    path('buy/<int:pk>/', stock_buy, name='buy'),
    path('sell/<int:pk>/', stock_sell, name='sell'),   # новый маршрут
    path('account/', account, name='account'),
]
