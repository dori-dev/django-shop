from django.shortcuts import redirect
from django.views import View
from django.contrib import messages


from bucket.tasks import download_object_task
from utils.mixins import SuperUserRequireMixin


class DownloadBucket(SuperUserRequireMixin, View):
    def get(self, request):
        key = request.GET.get('key')
        if key:
            download_object_task.delay(key)
            messages.success(
                request,
                "The object downloaded in <b>aws</b> folder!",
                "success",
            )
        return redirect('bucket:list')
