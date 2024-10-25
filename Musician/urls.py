from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.RegistraionView.as_view(),name = 'register'),
    path('add_musician/', views.AddMusicianview.as_view(),name='add_musician'),
    path('edit_musician/<int:id>', views.EditMusicianView.as_view(),name='edit_musician'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout_page/',views.log_out_page,name='logout_page'),
 path('logout/', LogoutView.as_view( next_page='login'), name='logout'),
]
