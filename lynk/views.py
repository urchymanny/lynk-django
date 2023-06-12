""" Views for the lynk Project """
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, JsonResponse
from .models import User, Element
from .forms import UserSignupForm, UserLoginForm, UpdateUserForm, CreateElementForm, UpdateElementForm
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    form = UserSignupForm()

    context = {
        'form': form,
        "error_message": ""
    }
    return render(request, "lynk/auth/signup.html", context)


def create_user(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile', user_id=user.id)
        else:
            error_message = form.errors
            context = {
                'form': form,
                'error_message': error_message,
            }
            return render(request, 'lynk/auth/signup.html', context)
    else:
        form = UserSignupForm()

        context = {
            'form': form,
            'error_message': ""
        }
        return render(request, 'lynk/auth/signup.html', context)


def login(request):
    form = UserLoginForm()

    context = {
        'form': form,
        "error_message": ""
    }
    return render(request, "lynk/auth/login.html", context)


def login_user(request):
    if request.method == 'POST':
        try:
            fusername = request.POST.get('username', None)
            fpass = request.POST.get('password', None)
            print(request.POST.get('username', None))
            user = get_object_or_404(User, username=fusername)
            if user.password == fpass:
                return redirect('profile', user_id=user.id)
            else:
                raise Http404("User does not exist or password incorrect")
        except User.DoesNotExist:
            raise Http404("User does not exist")

    form = UserLoginForm()

    context = {
        'form': form,
        "error_message": ""
    }

    return render(request, "lynk/auth/login.html", context)


def logout(request):
    return redirect('login')


def profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        elements = Element.objects.filter(user=user)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    context = {
        'user': user,
        'elements': elements
    }
    return render(request, "lynk/profile/show.html", context)


def edit_profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        form = UpdateUserForm(instance=user)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, "lynk/profile/edit.html", context)
    except User.DoesNotExist:
        raise Http404("User does not exist")


def update_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('profile', user_id=user.id)
        else:
            error_message = form.errors
            context = {
                'form': form,
                'error_message': error_message,
            }
            return render(request, "lynk/profile/edit.html", context)
    else:
        form = UpdateUserForm(instance=user)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, "lynk/profile/edit.html", context)


def public_show(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    elements = Element.objects.filter(user=user)
    context = {
        'user': user,
        'elements': elements,
    }
    return render(request, "lynk/public/show.html", context)


def add_element(request, user_id):
    form = CreateElementForm()
    user = User.objects.get(pk=user_id)

    context = {
        'form': form,
        'user': user,
        'error_message': ""
    }
    return render(request, 'lynk/elements/new.html', context)


def create_element(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = CreateElementForm(request.POST)
        if form.is_valid():
            el = form.save(commit=False)
            el.user = user
            el.save()
            return redirect('profile', user_id=user_id)
        else:
            error_message = form.errors
            context = {
                'form': form,
                'error_message': error_message,
            }
            return render(request, 'lynk/elements/new.html', context)
    else:
        form = CreateElementForm()

        context = {
            'form': form,
            'user': user,
            'error_message': ""
        }
        return render(request, 'lynk/elements/new.html', context)


def edit_element(request, element_id, user_id):
    try:
        user = User.objects.get(pk=user_id)
        element = Element.objects.get(pk=element_id)
        form = UpdateElementForm(instance=element)
        context = {
            'form': form,
            'element': element,
            'user': user,
        }
        return render(request, "lynk/elements/edit.html", context)
    except Element.DoesNotExist:
        raise Http404("Element does not exist")


def update_element(request, element_id, user_id):
    user = User.objects.get(pk=user_id)
    element = Element.objects.get(pk=element_id)

    if request.method == 'POST':
        form = UpdateElementForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user.id)
        else:

            error_message = form.errors
            context = {
                'form': form,
                'user': user,
                'element': element,
                'error_message': error_message,
            }
            return render(request, "lynk/elements/edit.html", context)
    else:
        form = UpdateElementForm(instance=element)
        context = {
            'form': form,
            'element': element,
            'user': user,
        }
        return render(request, "lynk/elements/edit.html", context)


@csrf_exempt
def delete_element(request, element_id, user_id):
    element = get_object_or_404(Element, id=element_id)

    if request.method == 'POST' and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        element.delete()

        # Prepare the response data
        response_data = {
            'message': 'element has been deleted successfully.'
        }

        return JsonResponse(response_data)
    else:
        # Return an error response if the request is not valid
        response_data = {
            'error': 'This is an API only request',
        }
        return JsonResponse(response_data, status=400)
