from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from blog.forms import SearchForm


def account_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.is_staff = True
            Profile.objects.create(user=new_user)
            new_user.save()
            print(new_user)
            return redirect('accounts:account_login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {
        'user_form': user_form,
    })


@login_required
def account_profile(request):
    form_search = SearchForm()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated successfully!!!')

        else:
            messages.error(request, 'Error Updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'registration/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'form_search': form_search,
    })
