"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from Rango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rango/', include('Rango.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 下面步骤是用于开发环境，在生产环境的话应该用别的方法（目前还没看到）
"""要想使用上传或存储的媒体文件必须做下面的配置：
1.在settings.py文件中添加MEDIA_DIR=os.path.join(BASE_DIR, 'media')
MEDIA_ROOT=MEDIA_DIR,MEDIA_URL='/media/'
2.在settings.py文件中的TEMPLATES的context_processors列表里添加媒体文件上下文处理器
3.在项目的urls.py文件的urlpatterns里添加static()方法
4.最后记得在项目根目录创建文件夹media(和manage.py在同级目录)
完成以上步骤就可以在浏览器上像访问static文件那样访问到媒体文件类如：
http:127.0.0.1:8000/media/cat.jpg"""


"""如果你是使用git和别人一起协同开发，最好不要将数据库文件如db.sqilte3上传，当别人更改数据库时容易引起冲突"""