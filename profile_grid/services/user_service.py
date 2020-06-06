from ..models import User


def create_user(new_user):
    user = User.objects.create(
        id_instagram = new_user.id_instagram,
        username = new_user.username,
        access_token = new_user.access_token,
    )
    return user


def find_user(id_instagram):
    try:
        user = User.objects.get(id_instagram=id_instagram)
        return user
    except User.DoesNotExist:
        return None

def update_user(old_user, new_user):
    old_user.id_instagram = new_user.id_instagram
    old_user.username = new_user.username
    old_user.access_token = new_user.access_token
    old_user.save(force_update=True)

    