from django.urls import path
from main.views import show_main, add_product, product_detail, show_xml, show_json, show_xml_by_id, show_json_by_id , register, login_user, logout_user, product_list,edit_product, delete_product
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import product_list 
from . import views
from django.urls import path
from . import views  # single import for all views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-list/', views.product_list, name='product_list'),
    path('products/<str:id>/', views.product_detail, name='product_detail'),
    path('products/<str:id>/edit/', views.edit_product, name='edit_product'),
    path('products/<str:id>/delete/', views.delete_product, name='delete_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/', views.show_json, name='show_json'),
    path('json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('product-detail-json/<str:id>/', views.product_detail_json, name='product_detail_json'),
    path('product-list-json/', views.product_list_json, name='product_list_json'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login-ajax/', views.login_user_ajax, name='login_user_ajax'),
    path('register-ajax/', views.register_user_ajax, name='register_user_ajax'),
    path('add-product-entry-ajax/', views.add_product_entry_ajax, name='add_product_entry_ajax'),
    path('update-product-entry-ajax/<str:id>/', views.update_product_entry_ajax, name='update_product_entry_ajax'),
    path('delete-product-entry-ajax/<str:id>/', views.delete_product_entry_ajax, name='delete_product_entry_ajax'),
]
