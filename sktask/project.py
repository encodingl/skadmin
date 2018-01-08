#! /usr/bin/env python
# -*- coding: utf-8 -*-
# update by guohongze@126.com
from django.shortcuts import render_to_response, redirect, HttpResponse, HttpResponseRedirect, RequestContext
from django.contrib.auth.decorators import login_required
from hashlib import sha1
from django.contrib import auth
from forms import Project_form
from models import project
from django.core.urlresolvers import reverse
from skaccounts.permission import permission_verify
from django.shortcuts import render
from django.http import HttpResponse


@login_required()
@permission_verify()
def project_index(request):
    temp_name = "sktask/sktask_header.html"
    allproject = project.objects.all()
    print allproject
    return render_to_response('sktask/project_index.html', locals(), RequestContext(request))

 
@login_required
@permission_verify()
def project_add(request):
    temp_name = "sktask/sktask_header.html"
    if request.method == "POST":
        project_form = Project_form(request.POST)
        if project_form.is_valid():
            project_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render_to_response("sktask/project_add.html", locals(), RequestContext(request))
    else:
        display_control = "none"
        project_form = Project_form()
        return render_to_response("sktask/project_add.html", locals(), RequestContext(request))
 
@login_required()
@permission_verify()
def project_del(request):
#    temp_name = "sktask/setup-header.html"
    project_id = request.GET.get('id', '')
    if project_id:
        project.objects.filter(id=project_id).delete()
    
  
    return HttpResponse(u'删除成功')

@login_required
@permission_verify()
def project_edit(request, ids):
    obj = project.objects.get(id=ids)
 
    if request.method == 'POST':
        form = Project_form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            status = 1
        else:
            status = 3
    else:
        form = Project_form(instance=obj)
    # ids = ids
    # kwvars = {
    #     'ids': ids,
    #     'form': form,
    #     'request': request,
    # }
 
    return render_to_response('sktask/project_edit.html', locals(), RequestContext(request))
 
# 
# @login_required
# @permission_verify()
# def reset_password(request, ids):
#     user = get_user_model().objects.get(id=ids)
#     newpassword = get_user_model().objects.make_random_password(length=10, allowed_chars='abcdefghjklmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789')
#     print '====>ResetPassword:%s-->%s' % (user.username, newpassword)
#     user.set_password(newpassword)
#     user.save()
# 
#     kwvars = {
#         'object': user,
#         'newpassword': newpassword,
#         'request': request,
#     }
# 
#     return render_to_response('skaccounts/reset_password.html', kwvars, RequestContext(request))
# 
# 
# @login_required
# def change_password(request):
#     temp_name = "skaccounts/accounts-header.html"
#     if request.method == 'POST':
#         form = ChangePasswordForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('logout'))
#     else:
#         form = ChangePasswordForm(user=request.user)
# 
#     kwvars = {
#         'form': form,
#         'request': request,
#         'temp_name': temp_name,
#     }
# 
#     return render_to_response('skaccounts/change_password.html', kwvars, RequestContext(request))