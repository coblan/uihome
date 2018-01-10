# encoding:utf-8

from __future__ import unicode_literals

from helpers.director.engine import BaseEngine,page,fa,page_dc

class PcMenu(BaseEngine):
    url_name='uihome'
    menu=[
        # {'label':'监督员','url':page('inspector.inspector'),'icon':fa('fa-user-secret'),
         # 'submenu':[
             # {'label':'实时点位','url':page('inspector.inspector_map')},
             # {'label':'监督员名单','url':page('inspector.inspector')},
             # {'label':'监督员分组','url':page('inspector.inspectorgroup')}
             # ]},
        {'label':'资源','url':page('ui_rs'),'icon':fa('fa-map-o')},
        {'label':'资源标签','url':page('ui_rs_tag'),'icon':fa('fa-map-o')}
    ]

PcMenu.add_pages(page_dc)