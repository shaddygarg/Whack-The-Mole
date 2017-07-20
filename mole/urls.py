from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from game import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'mole.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/profile/',views.profile,name='profile'),
    url(r'^accounts/',views.profile,name='profile'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^game/',views.game,name='game'),
    url(r'^save/',views.save,name='save'),
    url(r'^leaderboard/',views.leaderboard,name='leaderboard'),
]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
