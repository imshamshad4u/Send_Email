from .import views
from django.urls import path
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.register, name="register"),
    # path('otp_verification/', views.otp_verification, name='otp_verification'),
    # path('home/', views.home, name="home")
]
