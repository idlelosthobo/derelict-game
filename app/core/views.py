from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('core.view_home')
def home(response):
    return render(response, "core/page.html", {})
