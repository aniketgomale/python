from django.urls import path
from .import views
import product.views

urlpatterns = [
    # path('',views.home, name='home'),
    path('create/',views.create,name='create'),
    # path('base/',views.base,name='base')
    path('<int:product_id>',views.detail,name='detail'),

    # path('<int:product_id>/upvote',views.upvote,name='upvote'),
]