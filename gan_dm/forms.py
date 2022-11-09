from django import forms

from gan_dm.models import ResultDataset

class ResultDatasetForm(forms.ModelForm):
    class Meta:
        model = ResultDataset
        fields = ['res_dataset_name', 'res_dataset_description', 'res_dataset_count', 'res_dataset_class_list']
        
        # widgets = {
        #     'res_dataset_class_list': forms.CheckboxSelectMultiple,
        # }
        
        labels = {
            'res_dataset_name': 'dataset 이름',
            'res_dataset_description': 'dataset 설명',
            'res_dataset_count' : '이미지 생성 장수',
        }