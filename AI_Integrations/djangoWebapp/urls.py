from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/',views.register_user,name='register'),
    path('prompt/', views.chat_gpt_prompt_page, name='prompt'),
    path('ollama-prompt/', views.ollama_prompt_page, name='ollama-prompt'),
    path('chat-history/', views.user_chat_history, name='history'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('llava-prompt/', views.llava_promp_page, name='change_password'),

]