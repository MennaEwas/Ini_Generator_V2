import yaml
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FilesUpload

class admin_view_selectg(LoginRequiredMixin, View):
    template_name = 'Oadmin/selectg.html'

    def get(self, request):
        files = FilesUpload.objects.values_list('id','file')
        return render(request, self.template_name, {'files': files})

    def post(self, request):
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file = file2)
        document.save()
        return HttpResponse("file uploaded")
 

class show_all(LoginRequiredMixin, View):
    template_name = 'Oadmin/show_all.html'

    def get(self, request):
        files_names = request.GET.get('file_content', '')  # Retrieve the file content from the query parameter
        return render(request, self.template_name, {'content': files_names})


class show(LoginRequiredMixin, View):
    template_name = 'Oadmin/show.html'

    def get(self, request):
        file_content = request.GET.get('file_content', '')  # Retrieve the file content from the query parameter
        return render(request, self.template_name, {'content': file_content})

