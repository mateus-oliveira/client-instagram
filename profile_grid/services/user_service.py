from ..models import User

def create_user(user):
    User.objects.create(
        id_instagram=user.id_instagram,
        username=user.username,
        token=user.token,
    )

def find_user_by_username(username):
    return User.objects.get(username=username)

def find_user_by_id(id):
    return User.objects.get(id_instagram=id)

def update_user(old_user, new_user):
    old_user.id_instagram = new_user.id_instagram
    old_user.username = new_user.username
    old_user.token = new_user.token
    old_user.save(force_update=True)
    