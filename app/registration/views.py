from app.registration.forms import RegisterForm, UserEditForm
from django.shortcuts import render, redirect, get_object_or_404


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            user = form.save()
            user.is_employee = False
            user.is_active = False
            user.save()

            return redirect("/accounts/register_success")

        else:

            return redirect("/accounts/register")

    else:
        form = RegisterForm()

    return render(response, "registration/register_form.html", {"form": form})


def register_success(response):

    return render(response, "registration/register_success.html", {})


