from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page_view, name='main'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('save_record', save_record_view, name='save_record'),
    path('account', account_view, name='account'),
    path('delete_record/<int:record_id>/', delete_view, name='delete_record')
]
