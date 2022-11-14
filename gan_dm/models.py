from email.policy import default
from ssl import create_default_context
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TrainDataset(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dataset_name = models.CharField(max_length=200)
    dataset_description = models.TextField()
    dataset_type = models.CharField(max_length=200) # 2 type : GEN (generate) / TRSF (transfer)
    dataset_num_classes = models.IntegerField(default=1)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.dataset_name

class TrainDatasetDefect(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tds = models.ForeignKey(TrainDataset, on_delete=models.CASCADE)
    # sort된 idx
    ds_image_class_num = models.CharField(max_length=50)
    # sort된 폴더명
    ds_image_class_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.ds_image_class_name

class TrainDatasetImage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tds = models.ForeignKey(TrainDataset, on_delete=models.CASCADE)
    ds_image_path = models.CharField(max_length=1000)
    ds_image_name = models.CharField(max_length=200)
    ds_image_class_num = models.CharField(max_length=50)
    ds_image_class_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.ds_image_name

class Algorithm(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    al_name = models.CharField(max_length=200)
    al_branch = models.CharField(max_length=200)
    al_git_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.al_name
        
class GenerativeModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tds = models.ForeignKey(TrainDataset, on_delete=models.CASCADE)
    model_version = models.CharField(max_length=50)
    model_path = models.CharField(max_length=1000)
    model_name = models.CharField(max_length=200)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.model_name


class ResultDataset(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gen_model = models.ForeignKey(GenerativeModel, on_delete=models.CASCADE, default=1)
    res_dataset_name = models.CharField(max_length=200)
    res_dataset_description = models.TextField()
    res_dataset_count = models.IntegerField()
    res_dataset_class_list = models.CharField(max_length=200, default='[]')
    res_dataset_zip_path = models.CharField(max_length=500, default='')
    res_dataset_trial = models.IntegerField(default=0)
    res_process_finished_YN = models.BooleanField(default=False)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.res_dataset_name

class ResultDatasetImage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rds = models.ForeignKey(ResultDataset, on_delete=models.CASCADE)
    res_ds_image_path = models.CharField(max_length=1000)
    res_ds_image_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.res_ds_image_name

class InputInferenceDataset(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ii_dataset_name = models.CharField(max_length=200)
    ii_dataset_description = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.ii_dataset_name

class InputInferenceDatasetImage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    iids = models.ForeignKey(InputInferenceDataset, on_delete=models.CASCADE)
    ii_ds_image_path  = models.CharField(max_length=1000)
    ii_ds_image_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.ii_ds_image_name
