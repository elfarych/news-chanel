from django.urls import path
from . import views


urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('coins/', views.CoinListView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('news/', views.PostListView.as_view()),
    path('get_coins/', views.add_coins),
    path('delete_coins/', views.delete_coins),
    path('update_coins/', views.update_coins),
    path('get_categories/', views.add_categories),
    path('update_data/', views.update_data)
]
