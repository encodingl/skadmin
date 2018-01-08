#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from sktask import project,job,extravars,task

urlpatterns = [
   
    url(r'^project/index/$', project.project_index, name='project_index'),
    url(r'^project/add/$', project.project_add, name='project_add'),
    url(r'^project/delete/$', project.project_del, name='project_del'),
    url(r'^project/edit/(?P<ids>\d+)/$', project.project_edit, name='project_edit'),
 
    url(r'^job/$', job.job_index, name='job_index'),
    url(r'^job/del/$', job.job_del, name='job_del'),
    url(r'^job/add/$', job.job_add, name='job_add'),
    
    url(r'^job/edit/(?P<ids>\d+)/$', job.job_edit, name='job_edit'),
    url(r'^job/detail/(?P<ids>\d+)/$', job.job_detail, name='job_detail'),
   
    

# 
    url(r'^extravars/$', extravars.extravars_index, name='extravars_index'),
    url(r'^extravars/del/$', extravars.extravars_del, name='extravars_del'),
    url(r'^extravars/add/$', extravars.extravars_add, name='extravars_add'),
    url(r'^extravars/edit/(?P<ids>\d+)/$', extravars.extravars_edit, name='extravars_edit'),
    
    url(r'^task/$', task.task_index, name='task_index'),
    url(r'^task/jobsearch/$', task.job_search, name='job_search'),
    url(r'^task/varsearch/$', task.extravars_search, name='extravars_search'),
    url(r'^task/hostsfilechange/$', task.hostfile_change, name='hostfile_change'),
    url(r'^task/submit/$', task.task_submit, name='task_submit'),
    

 
]
