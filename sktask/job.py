#! /usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE, STDOUT, call
from django.shortcuts import render
from django.http import HttpResponse
from models import job,extravars,project
import os
from skconfig.views import get_dir
from django.contrib.auth.decorators import login_required
from skaccounts.permission import permission_verify
import logging
from lib.log import log
from lib.setup import get_playbook, get_roles
from .models import history
from .forms import Job_form
from django.shortcuts import render_to_response, RequestContext
from skcmdb.api import get_object
import json
# var info

proj_base_dir = get_dir("pro_path")



@login_required()
@permission_verify()
def job_index(request):
    temp_name = "sktask/sktask_header.html"
    alljob = job.objects.all()
    return render_to_response('sktask/job_index.html', locals(), RequestContext(request))

@login_required()
@permission_verify()
def job_add(request):
    temp_name = "sktask/sktask_header.html"
    if request.method == "POST":
        job_form = Job_form(request.POST)
        if job_form.is_valid():
            job_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render_to_response("sktask/job_add.html", locals(), RequestContext(request))
    else:
        display_control = "none"
        job_form = Job_form()
        return render_to_response("sktask/job_add.html", locals(), RequestContext(request))





@login_required()
@permission_verify()
def job_del(request):
    temp_name = "sktask/sktask_header.html"
    job_id = request.GET.get('id', '')
    if job_id:
        job.objects.filter(id=job_id).delete()
    if request.method == 'POST':
        job_items = request.POST.getlist('job_check', [])
        if job_items:
            for n in job_items:
                job.objects.filter(id=n).delete()
    
    alljob = job.objects.all()
    return render_to_response("sktask/job_index.html", locals(), RequestContext(request))


@login_required()
@permission_verify()
# def job_edit(request, ids):
#     obj = job.objects.get(id=ids)
#     alljob = job.objects.all()
#     return render_to_response("sktask/job_edit.html", locals(), RequestContext(request))

def job_edit(request, ids):
    status = 0
#     asset_types = online_status
    obj = get_object(job, id=ids)
#     obj = job.objects.get(id=ids)
    if request.method == 'POST':
        obj_f = Job_form(request.POST, instance=obj)
        if obj_f.is_valid():
            obj_f.save()
            status = 1
        else:
            status = 2
    else:
        obj_f = Job_form(instance=obj)      
    return render_to_response("sktask/job_edit.html", locals(), RequestContext(request))

@login_required
@permission_verify()
def job_detail(request, ids):
    proj_base_dir = get_dir("pro_path")
    obj={}  
    obj_job = get_object(job, id=ids)
    obj_playbook=obj_job.playbook
    obj_project = get_object(project, name=obj_job.project)
    obj_pro_path=obj_project.path
    pkfile = proj_base_dir +  obj_pro_path + "/" + obj_playbook
  
    
    obj["name"] = obj_playbook
    with open(pkfile, 'r') as f:
        obj["content"] = f.read()
   

 
    return render_to_response('sktask/job_detail.html', locals(), RequestContext(request))

