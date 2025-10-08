from django.urls import path
from main.views import show_main, add, detail, show_xml, show_json, show_json_by_id, show_xml_by_id, \
                        register, login_user, logout_user, edit_product, delete_product, \
                        add_ajax, update_product_ajax, delete_product_ajax, \
                        login_ajax, register_ajax, logout_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', add, name='add'),
    path('detail/<str:id>/', detail, name='detail'),
    path('xml/', show_xml, name='show_xml'),
#    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
#    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit', edit_product, name='edit'),
    path('news/<int:id>/delete', delete_product, name='delete'),
    path('products/json/', show_json, name='show_json'),
    path('products/<int:product_id>/json/', show_json_by_id, name='show_json_by_id'),

    # AJAX CRUD
    path('products/create-ajax/', add_ajax, name='create_product_ajax'),
    path('products/<int:id>/update-ajax/', update_product_ajax, name='update_product_ajax'),
    path('products/<int:id>/delete-ajax/', delete_product_ajax, name='delete_product_ajax'),

    # Auth AJAX
    path('auth/login-ajax/', login_ajax, name='login_ajax'),
    path('auth/register-ajax/', register_ajax, name='register_ajax'),
    path('auth/logout-ajax/', logout_ajax, name='logout_ajax'),
]
