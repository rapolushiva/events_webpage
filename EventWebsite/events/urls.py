from django.urls import path

from events import views

urlpatterns=[
    path("", views.homepagefun, name='homepage'),
    path('addevent/',views.addevent, name='addevent'),
    path('showevent/', views.showevent, name='showevent'),
    path('updateevent/<int:pk>',views.updateevent , name='updateevent'),
    path('search/', views.searchbar, name='searchbar'),
]