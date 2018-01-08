#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from models import project,job,extravars



class Project_form(forms.ModelForm):
    class Meta:
        model = project
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'path': forms.TextInput(attrs={'class': 'form-control'}),
            'online_status': forms.Select(attrs={'class': 'form-control'}),          
        }


class Job_form(forms.ModelForm):
    class Meta:
        model = job
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'playbook': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}), 
            'online_status': forms.Select(attrs={'class': 'form-control'}),          
        }

class Extravars_form(forms.ModelForm):
    class Meta:
        model = extravars
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'vars': forms.Textarea(attrs={'class': 'form-control'}),
            'job': forms.Select(attrs={'class': 'form-control'}), 
            'online_status': forms.Select(attrs={'class': 'form-control'}),          
        }