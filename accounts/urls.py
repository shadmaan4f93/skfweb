from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
LoginView,
LogoutView,
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetCompleteView,
PasswordChangeView,
PasswordChangeDoneView,
)

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', LoginView.as_view(), {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': 'accounts/login'}, name='logout'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]