# Points rool URLconf at the polls.urls module

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
]