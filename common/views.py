from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from gan_dm.models import ResultDataset

from .forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

@login_required(login_url='common:login')
def mypage(request):
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    my_resultdataset_list = ResultDataset.objects.filter(author=request.user).order_by('-create_date')
    # 페이징처리
    paginator = Paginator(my_resultdataset_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'my_resultdataset_list': page_obj, 'uesr': request.user}
    return render(request, 'common/mypage.html', context)