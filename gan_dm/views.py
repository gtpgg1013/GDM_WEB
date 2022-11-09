from http.client import HTTPResponse
from urllib import response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ResultDataset, ResultDatasetImage, TrainDataset, TrainDatasetImage, Algorithm, GenerativeModel
from .forms import ResultDatasetForm
from django.http import FileResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import requests
import json

# Create your views here.
@login_required(login_url='common:login')
def index(request):
    """
    메인 페이지, 모델 리스트 / 모델 학습 설명
    """
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    gen_model_list = GenerativeModel.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(gen_model_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'gen_model_list': page_obj}
    return render(request, 'gan_dm/main.html', context)

@login_required(login_url='common:login')
def train(request):
    return redirect('gan_dm:index')

@login_required(login_url='common:login')
def inference(request, gen_model_id):
    """
        gan_dm 추론 요청
    """
    gen_model = get_object_or_404(GenerativeModel, pk=gen_model_id)
    train_dataset = gen_model.tds
    num_classes = train_dataset.dataset_num_classes
    class_range = list(range(1, num_classes + 1))

    if request.method == 'POST':
        form = ResultDatasetForm(request.POST)
        list_item = request.POST.getlist('res_dataset_class_list')
        if form.is_valid():
            result_dataset = form.save(commit=False)
            result_dataset.author = request.user  # 추가한 속성 author 적용
            result_dataset.create_date = timezone.now()
            result_dataset.res_dataset_class_list = list_item
            '''
            여기에서 뭔가 다른 서비스에서 추론하는 로직이 껴있어야 하지 않을까?
            async api를 찌르고, 일단 200 리턴 받음.
            그리고 finish_rds api가 찔리는 것으로 rds YN값 변경! (다운로드 가능)
            그리고 여기 로직에서 folder구조까지 다 만들어줘야 함
            즉, 우리 flow상 Data Pipeline + Inference Engine이라고 할 수 있음.
            '''
            result_dataset.save()
            print(result_dataset.id)
            rds_id = result_dataset.id
            tmp = requests.get('http://127.0.0.1:8001/inference/{}/'.format(rds_id))
            print(tmp)
            
            return redirect('common:mypage')
    else:
        form = ResultDatasetForm()
    context = {'form': form, 'class_range' : class_range}
    return render(request, 'gan_dm/inference_form.html', context)

@login_required(login_url='common:login')
def download(request, rds_id):
    '''
    다운로드 로직 작성
    '''
    result_dataset = get_object_or_404(ResultDataset, pk=rds_id)
    # file_path = os.path.abspath("media/")
    file_path = os.path.abspath(os.path.dirname(result_dataset.res_dataset_zip_path))
    file_name = os.path.basename(result_dataset.res_dataset_zip_path)
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    return response

# fast api server와 통신
@api_view(['POST'])
def finish_rds(request, rds_id):
    if request.method == 'POST':
        result_dataset = get_object_or_404(ResultDataset, pk=rds_id)
        print(result_dataset)
        img_path_list = request.POST.getlist('result_file_path_list')
        for img_path in img_path_list:
            rdi = ResultDatasetImage()
            rdi.author = result_dataset.author
            rdi.rds = result_dataset
            rdi.res_ds_image_path = img_path
            rdi.res_ds_image_name = os.path.basename(img_path)
            rdi.create_date = timezone.now()
            rdi.save()
            print(img_path)
        # .get(res_dataset_trial=num_trial)

        zip_path = request.POST.get('zip_path')
        result_dataset.res_process_finished_YN  = True
        result_dataset.res_dataset_zip_path = zip_path
        result_dataset.save()
        return Response(status=200)
    else:
        return HttpResponse('This API only support HTTP POST Method.')