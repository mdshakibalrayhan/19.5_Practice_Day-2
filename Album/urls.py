from django.urls import path
from .import views
urlpatterns = [
    path('add_album/', views.AddAlbumView.as_view(),name='add_album'),
    path('edit_album/<int:id>', views.EditAlbumView.as_view(),name='edit_album'),
    path('delete_album/<int:id>', views.DeleteAlbumview.as_view(),name='delete_album'),
    path('',views.home,name='homepage'),
]
