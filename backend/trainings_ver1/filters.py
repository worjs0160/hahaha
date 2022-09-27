# from django_filters import (
#     FilterSet,
#     CharFilter,
# )
# from .models import Training


# class TrainingByUserFilter(FilterSet):
#     user = CharFilter(field_name="user")
#     trainingDate = CharFilter(field_name="trainingDate", lookup_expr="icontains")

#     class Meta:
#         model = Training
#         fields = ["user", "trainingDate"]

#     def __init__(self, *args, **kwargs):
#         super(TrainingByUserFilter, self).__init__(*args, **kwargs)
        