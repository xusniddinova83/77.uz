from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Address

@receiver(post_save, sender=Address)
def log_address_created(sender, instance, created, **kwargs):
    if created:
        print(f"Yangi address yaratildi: {instance}")
