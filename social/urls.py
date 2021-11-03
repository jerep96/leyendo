from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('index', views.index, name="index"),
	path('', views.feed, name='feed'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/index.html'), name='logout'),
	path('post/<str:type>', views.url, name='post'),
	path('eliminar/<str:urls>', views.eliminarProducto, name='eliminar'),
	path('editar/<str:title>/<str:type>', views.editarUrl, name='editar'),
	path('leyendo/<str:username>/', views.link, name='link'),
	path('ver/<str:username>/', views.ver, name='ver'),
	path('editprofile/<str:username>/', views.editprofile, name='editprofile'),
	path('action', views.actions, name='action'),
	path('save-group-ordering', views.save_new_ordering, name='save-group-ordering'),

	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
