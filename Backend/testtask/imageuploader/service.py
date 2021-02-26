import os
from datetime import datetime, timezone
from uuid import uuid4
from django.core.mail import send_mail


def new_image_action(image_action, obj, action_type):
    image_action.objects.create(
        image_id=obj.id,
        type=action_type,
        from_image=obj.image
    )


def send_image_uploaded_mail(user, obj):
    send_mail('Test', f'{user.username}; {datetime.now(timezone.utc).astimezone()}; {obj.image.url}',
              'elfarych@gmail.com', [user.email], fail_silently=False)


def path_and_rename(path, prefix):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}{}.{}".format(prefix, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)

    return wrapper
