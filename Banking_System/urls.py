"""
URL configuration for Banking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Banking_Login import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.members,name="basic"),
    path('404_page',views.page_404,name="404_page"),
    path('login',views.Login,name="login"),
    # path('register',views.members,name="register"),
    path('Account_Creation',views.account_creation,name="account_creation"),
    path('Debit_Auth',views.Debit_amount,name="debit_auth"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()