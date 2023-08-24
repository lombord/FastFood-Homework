from django.urls import path, include

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-dish/', DishCreateView.as_view(), name='add_dish'),
    path('dish/<int:pk>/', include([
        path('', DishView.as_view(), name='dish'),
        path('update/', DishUpdateView.as_view(), name='update_dish'),
        path('delete/', DishDeleteView.as_view(), name='delete_dish'),
    ])),
]
