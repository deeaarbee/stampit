from backend.models import Html, User
import string
import random


def random_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def add_html_object(name: str, html_code: str, category: str, code_type: str, status: str):
    html = Html()
    html.name = name
    html.user = User.objects.get(username="drbalaji97")
    html.category = category
    html.code_type = code_type
    html.html_code = html_code
    html.status = status
    html.unique_code = random_generator()
    html.save()
    return html


def get_all_html_objects(user: User):
    htmls = Html.objects.filter(user=user).all()
    return htmls


def increment_count_html_object(unique_code: str):
    html = Html.objects.get(unique_code=unique_code)
    html.count += 1
    html.save()
