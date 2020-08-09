from django.contrib.auth.models import Permission

PERM = Permission.objects.get(codename='blogger')
TEST = "HAI"
