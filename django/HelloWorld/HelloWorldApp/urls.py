from django.conf.urls import url
from .import views
from django.conf.urls.static import static

from HelloWorldApp.views import foo, foo1,foo2,foo3,foo4

#from current package

urlpatterns=[
    url(r'^/$',views.foo,name='foo'),
    
    #url(r'^$' views.foo, name='foo')
    ]
