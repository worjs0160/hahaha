# from django_filters import (
#     FilterSet,
#     CharFilter,
# )
# from .models import Attendance

# # AttendanceListViewSet filter
# class AttendanceListFilter(FilterSet):
#     coach = CharFilter(field_name="user", lookup_expr="coach")
#     team = CharFilter(field_name="user", lookup_expr="team")
#     startWorkTime = CharFilter(lookup_expr="icontains")
#     finishWorkTime = CharFilter(lookup_expr="icontains")

#     class Meta:
#         model = Attendance
#         fields = ["user", "coach", "team", "startWorkTime", "finishWorkTime",]

#     def __init__(self, *args, **kwargs):
#         super(AttendanceListFilter, self).__init__(*args, **kwargs)
        