# encoding:utf-8
from __future__ import unicode_literals
from django.contrib import admin
from helpers.director.shortcut import TablePage,ModelTable,page_dc,ModelFields,FormPage,model_dc,regist_director,RowFilter
# Register your models here.
from .models import Tag,UiResource

regist_director(name='ui_rs_tag',src_model=Tag)

class UiRsTablePage(TablePage):
    class UiRsTable(ModelTable):
        model = UiResource
        exclude=[]
        
        def dict_row(self, inst):
            return {'tags':[unicode(x) for x in inst.tags.all()]}
    
    tableCls=UiRsTable

    def get_template(self, prefer=None):
        return 'ui_rs/ui_rs.html'

class UiRsFormPage(FormPage):
    class UiRsForm(ModelFields):
        class Meta:
            model=UiResource
            exclude=[]
    fieldsCls=UiRsForm
    def get_template(self, prefer=None):
        return 'ui_rs/ui_rs_form.html'

model_dc[UiResource]={'fields':UiRsFormPage.UiRsForm}

page_dc.update({
    'ui_rs':UiRsTablePage,
    'ui_rs.edit':UiRsFormPage
})
    