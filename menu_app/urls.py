'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list),
]
'''

from django.contrib import admin
from django.urls import path
from menu_app.views import CategoryListView, PostByCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
]