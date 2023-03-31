from django.shortcuts import render
from django.views import View

from bucket.tasks import all_bucket_objects_task
from utils.mixins import SuperUserRequireMixin


class BucketList(SuperUserRequireMixin, View):
    def get(self, request):
        context = {
            'objects': all_bucket_objects_task(),
        }
        return render(request, 'bucket/list.html', context)
