from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from  .views import ShoppingCartView, TodosView

urlpatterns=[
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('todos', TodosView.as_view(), name='todos'),


]