from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from my_permission.service.permission_service import check_user_permission, permission_data_from_t1_table, \
    permission_data_from_t2_table, permission_data_from_t3_table


# @login_required
@permission_required('my_permission.view_t1')
def show_first_table(request):
    get_user_group = check_user_permission(request)
    data = permission_data_from_t1_table(get_user_group)
    context = {
        'data': data
    }
    return render(request, 'my_permission/data_first.html', context=context)


# @login_required
@permission_required('my_permission.view_t2')
def show_second_table(request):
    get_user_group = check_user_permission(request)
    data = permission_data_from_t2_table(get_user_group)
    context = {
        'data': data
    }
    return render(request, 'my_permission/data_second.html', context=context)


# @login_required
@permission_required('my_permission.view_t3')
def show_third_table(request):
    get_user_group = check_user_permission(request)
    data = permission_data_from_t3_table(get_user_group)
    context = {
        'data': data
    }
    return render(request, 'my_permission/data_third.html', context=context)
