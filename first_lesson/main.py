import django_orm_setings

from control_system.models import User

User(
    name="Dave",
    email = 'user@user.com',
    role = 'user'
).save()