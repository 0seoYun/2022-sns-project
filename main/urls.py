from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('introduction/', introduction, name='introduction'),
    path('picture/', picture, name="picture"),
    path('firstpage/', showfirst, name="showfirst"),
    path('secondpage/', showsecond, name="showsecond"),
    path('<str:id>',detail, name="detail"),
    path('new/',new, name="new"),
    path('create/',create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<str:post_id>/update_comment/<str:comment_id>', update_comment, name="update_comment"),
    path('delete_comment/<int:id>', delete_comment, name="delete_comment"),
    path('<str:post_id>/edit_comment/<str:comment_id>', edit_comment, name="edit_comment"),
    path('like_toggle/<int:post_id>/',like_toggle,name="like_toggle"),
    path('dislike_toggle/<int:post_id>/',dislike_toggle,name="dislike_toggle"),
    path('my_like/<int:post_id>',my_like, name='my_like'),
    path('my_dislike/<int:post_id>',my_dislike, name='my_dislike'),
]