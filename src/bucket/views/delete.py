from django.shortcuts import redirect
from django.views import View
from django.contrib import messages

from bucket.tasks import delete_object_task
from utils.mixins import SuperUserRequireMixin


class DeleteBucket(SuperUserRequireMixin, View):
    def get(self, request):
        key = request.GET.get('key')
        if key:
            delete_object_task.delay(key)
            messages.warning(
                request,
                "The object deleted successfully!",
                "warning",
            )
        return redirect('bucket:list')
