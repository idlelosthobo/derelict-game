from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('core.view_home')
def ui_game(response):
    return render(response, "ui/ui_game.html", {})
