from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from .api import views as api_views

from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^home/$',  views.home, name='home'),
    url(r'^dev/(?P<pk>[0-9]+)$',  views.dev_deatil, name='devdetail'),
    url(
        regex=r'^api/chat/$',
        view=api_views.chatboots,
    ),
    url(
        regex=r'^api/chat/train/$',
        view=api_views.chatbot_traner,
    ),
    url(
        regex=r'^api/chat/selftrain/$',
        view=api_views.chatbot_self_traner,
    ),
    url(
        regex=r'^api/recognizer/$',
        view=api_views.recognition,
    ),
    url(
        regex=r'^api/sendmail/$',
        view=api_views.sendmail,
    )
]
