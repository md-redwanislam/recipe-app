from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from .models import CustomUser

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            if data["password"] != data["confirm_password"]:
                form.add_error("confirm_password", "Passwords do not match.")
                return render(
                    request,
                    "auth/registration.html",
                    {"form": form}
                )

            if CustomUser.objects.filter(email__iexact=data["email"]).exists():
                form.add_error("email", "This email is already registered.")
                return render(
                    request,
                    "auth/registration.html",
                    {"form": form}
                )

            CustomUser.objects.create_user(
                email=data["email"],
                password=data["password"],
                name=data["name"],
                phone=data["phone"],
                bio=data["bio"],
                profile_picture=data["profile_picture"],
            )

            messages.success(request, "Your account has been created successfully!")
            return redirect("login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "auth/registration.html",
        {"form": form}
    )

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                email=email,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect("/")

            form.add_error(None, "Invalid email or password.")

    else:
        form = LoginForm()

    return render(
        request,
        "auth/login.html",
        {"form": form}
    )

@login_required(login_url='/auth/login/')
def profile_view(request):
    user = request.user

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            data = form.cleaned_data

            user.name = data["name"]
            user.phone = data["phone"]
            user.bio = data["bio"]

            if data["profile_picture"]:
                old_picture = user.profile_picture

                user.profile_picture = data["profile_picture"]
                user.save()

                if old_picture:
                    old_picture.delete(save=False)
            else:
                user.save()

            messages.success(request, "Profile updated successfully!")
            return redirect("profile")

    else:
        form = ProfileForm(initial={
            "name": user.name,
            "phone": user.phone,
            "bio": user.bio,
        })

    return render(
        request,
        "profile.html",
        {"form": form, "profile_user": user}
    )

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("login")

    return redirect("login")

