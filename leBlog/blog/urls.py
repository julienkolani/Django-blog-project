from django.contrib                 import admin
from django.urls                    import path
from django.contrib.auth.decorators import login_required
from blog.views                     import blogHome , blogCreate, blogDelete, blogDetail , blogUpdate

app_name = "blog"

urlpatterns = [
    path('',blogHome.as_view(), name='home'),
    path('create/',blogCreate.as_view(), name='create'),
    path('<str:slug>/',blogDetail.as_view(), name='post'),
    path('edit/<str:slug>/',blogUpdate.as_view(), name='edit'),
    path('delete/<str:slug>/',blogDelete.as_view(), name='delete')
]