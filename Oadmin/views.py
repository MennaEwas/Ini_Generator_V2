import configparser
from django.http import HttpResponse
import yaml
import json

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class admin_view_selectg(LoginRequiredMixin, View):
    template_name = 'Oadmin/selectg.html'

    def get(self, request):
        return render(request, self.template_name, {'yaml_content': ''})

    def post(self, request):
        yaml_content = request.POST.get('yaml_content')
        yaml_data = yaml.safe_load(yaml_content) #convert into yaml object 
        
        with open('Myyaml.yaml', 'w') as yaml_file:
            yaml.dump(yaml_data, yaml_file)

        return HttpResponse("Finished!")







# BSP Params
# PCMLawSelect