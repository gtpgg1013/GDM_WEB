from django.contrib import admin
from .models import TrainDataset, TrainDatasetImage, Algorithm, GenerativeModel, TrainDatasetDefect
from .models import ResultDataset, ResultDatasetImage, InputInferenceDataset, InputInferenceDatasetImage

# Register your models here.
class TrainDatasetAdmin(admin.ModelAdmin):
    search_fields = ['dataset_name']

class TrainDatasetDefectAdmin(admin.ModelAdmin):
    search_fields = ['ds_image_class_name']

class TrainDatasetImageAdmin(admin.ModelAdmin):
    search_fields = ['ds_image_name']

class AlgorithmAdmin(admin.ModelAdmin):
    search_fields = ['al_name']

class GenerativeModelAdmin(admin.ModelAdmin):
    search_fields = ['model_version']

class ResultDatasetAdmin(admin.ModelAdmin):
    search_fields = ['res_dataset_name']

class ResultDatasetImageAdmin(admin.ModelAdmin):
    search_fields = ['rds_image_name']

class InputInferenceDatasetAdmin(admin.ModelAdmin):
    search_fields = ['ii_dataset_name']

class InputInferenceDatasetImageAdmin(admin.ModelAdmin):
    search_fields = ['ii_ds_image_name']


admin.site.register(TrainDataset, TrainDatasetAdmin)
admin.site.register(TrainDatasetDefect, TrainDatasetDefectAdmin)
admin.site.register(TrainDatasetImage, TrainDatasetImageAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)
admin.site.register(GenerativeModel, GenerativeModelAdmin)
admin.site.register(ResultDataset, ResultDatasetAdmin)
admin.site.register(ResultDatasetImage, ResultDatasetImageAdmin)
admin.site.register(InputInferenceDataset, InputInferenceDatasetAdmin)
admin.site.register(InputInferenceDatasetImage, InputInferenceDatasetImageAdmin)