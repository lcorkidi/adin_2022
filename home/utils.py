def user_group_str(user):
    from django.contrib.auth.models import Group
    for group in Group.objects.all():
        if Group.objects.get(name=group.name) in user.groups.all():
            return group.name