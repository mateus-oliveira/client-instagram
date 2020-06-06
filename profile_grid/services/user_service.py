from ..models import User


def create_user(new_user):
    user, created = User.objects.get_or_create(
        id_instagram = new_user.id_instagram,
        username = new_user.username,
        accsess_token = new_user.accsess_token,
    )

    