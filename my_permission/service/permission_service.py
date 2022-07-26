from django.contrib.auth.models import Group
from my_permission.models import T1, T2, T3


def check_user_permission(request):
    first_group = Group.objects.get(name='group_1')
    if request.user in first_group.user_set.all():
        return 'group_1'
    second_group = Group.objects.get(name='group_2')
    if request.user in second_group.user_set.all():
        return 'group_2'
    third_group = Group.objects.get(name='group_3')
    if request.user in third_group.user_set.all():
        return 'group_3'


def permission_data_from_t1_table(user_group: str):
    if user_group == 'group_1':
        return T1.objects.all()
    elif user_group == 'group_2':
        return T1.objects.filter(name='ДФО')


def permission_data_from_t2_table(user_group: str):
    if user_group == 'group_1':
        return T2.objects.all()
    elif user_group == 'group_2':
        return T2.objects.filter(name='ДФО')
    elif user_group == 'group_3':
        return T2.objects.filter(name='СФО')


def permission_data_from_t3_table(user_group: str):
    if user_group == 'group_1':
        return T3.objects.all()
    elif user_group == 'group_3':
        return T3.objects.filter(name='СФО')
