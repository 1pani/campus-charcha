
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from se import views

urlpatterns = [
    url(r'^index/', views.login_page),
    url(r'^topic/', views.topic_page),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^home/', views.home_page),
    url(r'^user/create/', views.question),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.UserFormView, name='signup'),
    url(r'^addquestion/$', views.question),
    url(r'^answer/$', views.answer),
    url(r'^logout/$', views.logout_view),
    url(r'^comment/$', views.comment_view),
    url(r'^upvote/$', views.upvote_view),
    url(r'^downvote/$', views.downvote_view),
    url(r'^poll/', include('poll.urls')),

]
