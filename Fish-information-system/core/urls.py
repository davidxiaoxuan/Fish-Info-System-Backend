"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import test_endpoint, home, search_fish, fish_detail, register_user, login_user  # 确保导入了register_user和login_user视图

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),  # 设置默认主页路径
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/test-endpoint/', test_endpoint),  # 确保路径正确
    path('api/search/', search_fish, name='search_fish'),  # 添加搜索路径
    path('api/fish/<int:id>/', fish_detail, name='fish_detail'),
    path('api/register/', register_user, name='register_user'),  # 添加注册路径
    path('api/login/', login_user, name='login_user'),  # 添加登录路径
]
