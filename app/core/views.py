from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import permission_required


@permission_required('core.view_home')
def home(response):
    return redirect(reverse('ui_game'))
    # return render(response, "core/page.html", {})
