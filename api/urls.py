from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, DjangoAuthentication
#from piston.doc import documentation_view

from step2.api.handlers import *

auth = DjangoAuthentication('/accounts/login', 'next');

project = Resource(handler=ProjectHandler, authentication=auth)
projects = Resource(handler=ProjectsHandler, authentication=auth)

task = Resource(handler=TaskHandler, authentication=auth)
all_tasks = Resource(handler=AllTasksHandler, authentication=auth)
project_tasks = Resource(handler=ProjectTasksHandler, authentication=auth)

forum = Resource(handler=ForumHandler, authentication=auth)
forums = Resource(handler=ForumsHandler, authentication=auth)
forum_threads = Resource(handler=ForumThreadsHandler, authentication=auth)
thread_posts = Resource(handler=ThreadPostsHandler, authentication=auth)

urlpatterns = patterns('',
                       url(r'^projects/$', projects),
                       url(r'^projects/(\d+)/$', project),

                       url(r'^projects/tasks/$', all_tasks),
                       url(r'^projects/(\d+)/tasks/$', project_tasks),

                       url(r'^projects/tasks/(\d+)/$', task),

                       url(r'^forums/$', forums),
                       url(r'^forums/(?P<forum_id>\d+)/$', forum),
                       url(r'^projects/(?P<project_id>\d+)/forum/$', forum),

                       url(r'^forums/(\d+)/threads/$', forum_threads),
                       url(r'^forums/threads/(\d+)/posts/$', thread_posts),
                       )

