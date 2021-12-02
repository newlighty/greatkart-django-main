from django.db.models.signals import per_save #post_save
from django.dispatch import receiver
from .models import Post
from django.utils.text import slugify

@receiver(per_save, sender=Post)
def create_category_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=create_uniqe_slug(instance)


def create_uniqe_slug(instance,newslug=None):
    if newslug is not None:
        slug=newslug
    else:
        slug=slugify(instance.n,allow_unicode=True)

    instanceClass=instance.__class__
    qs=instance.objects.filter(slug=slug)

    if qs.exists():
        newslug=f"{slug}-{qs.fist().id}"
        return create_uniqe_slug(instance,newslug)

    return slug   