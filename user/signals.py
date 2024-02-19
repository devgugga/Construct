from django.dispatch import receiver
from django.db.models.signals import post_save
from rolepermissions.roles import assign_role
from .models import Users


@receiver(post_save, sender=Users)
def define_user_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.role == "V":
            assign_role(instance, "vendedor")
        elif instance.role == "G":
            assign_role(instance, "gerente")
