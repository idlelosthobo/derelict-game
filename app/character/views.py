from django.shortcuts import render, reverse, redirect
from django.views import generic
from app.character import forms, models
from app.player.models import Player


class CharacterSelectView(generic.ListView):

    model = models.Character
    template_name = 'character/character_select_page.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        return models.Character.objects.filter(user=self.request.user)


class CharacterCreateFormView(generic.CreateView):

    model = models.Character
    template_name = 'character/character_create_page.html'
    form_class = forms.CharacterCreateForm
    acquisition_pk = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreateFormView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("character_select_view")


def character_pick(request, pk):

    if request.user.is_authenticated:
        if request.method == "GET":
            # todo: This needs to have a protection from picking a character that is not yours.
            Player.objects.filter(user=request.user).update(character=pk)
            return redirect('ui_game')
    else:
        return redirect('login')
