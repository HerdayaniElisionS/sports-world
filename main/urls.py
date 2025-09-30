from django.urls import path
from main.views import show_main, add_product, product_detail, show_xml, show_json, show_xml_by_id, show_json_by_id , register, login_user, logout_user, product_list,edit_product, delete_product
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import product_list 

app_name = 'main'


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('products/<str:id>/', product_detail, name='product_detail'),
    path('product-list/', product_list, name='product_list'),
    path('products/<str:id>/edit/', edit_product, name='edit_product'),
    path('products/<str:id>/delete/', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]