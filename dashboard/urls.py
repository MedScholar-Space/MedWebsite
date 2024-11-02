from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('accounts/password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
path('password_change/',
auth_views.PasswordChangeView.as_view(),
name='password_change'),
path('password_change/done/',
auth_views.PasswordChangeDoneView.as_view(),
name='password_change_done'),
path('register/', views.register, name='register'),
path('account/edit/', views.edit, name='edit'),
path('', views.dashboard, name='dashboard'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)