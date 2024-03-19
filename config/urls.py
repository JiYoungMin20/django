"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include #2024.03.14 include 추가
from pybo import views # 2024.03.14 추가

urlpatterns = [
    path('', views.index, name='index'), # / 페이지에 해당하는 urlpatterns 2024.03.18
    path('admin/', admin.site.urls),
    # path('pybo/', views.index),  # 2024.03.14 추가
    path('pybo/', include('pybo.urls')), # 2024.03.14 URL 분리하기
    path('common/', include('common.urls')), # 2024.03.18 common/urls.py 파일로 유도
]
