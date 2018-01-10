# encoding:utf-8
from __future__ import unicode_literals

from .models import UiResource
from helpers.director.db_tools import to_dict

def get_global():
    return globals()

def get_rs_list():
    ls = [to_dict(x) for x in UiResource.objects.all()]
    return ls
