from django.urls import path
from . import views

app_name = 'ecom_app'
urlpatterns = [
    path('',views.allProductCategory,name='allProductCategory'),
    path('<slug:c_slug>/',views.allProductCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>',views.productDeatails,name='productDetails'),
]