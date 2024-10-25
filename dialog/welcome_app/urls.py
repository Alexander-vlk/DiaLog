from django.urls import path

from welcome_app.views import welcome_page


app_name = 'welcome_app'
urlpatterns = [
    path('', welcome_page, name='welcome'),
]
