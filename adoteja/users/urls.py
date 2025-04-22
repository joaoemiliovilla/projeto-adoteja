from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # criando a rota para redirecionar para a pagina de detalhes do usuário
    path('profile/', views.user_profile_view, name="user_profile"),
]