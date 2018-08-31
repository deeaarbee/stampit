from backend.functions import core
from backend.models import Html


def get_html_details_from_object(html: Html):
    html_dict = dict()
    html_dict['name'] = html.name
    html_dict['category'] = html.category
    html_dict['code_type'] = html.code_type
    html_dict['html_code'] = html.html_code
    html_dict['unique_code'] = html.unique_code
    html_dict['created_at'] = html.created_at
    html_dict['updated_at'] = html.updated_at
    html_dict['count'] = html.count
    html_dict['status'] = html.status
    return html_dict


def get_all_html():
    htmls = core.get_all_html_objects()
    html_list = list()
    for html in htmls:
        html_list.append(get_html_details_from_object(html=html))
    return html_list


def increment_count(unique_code: str):
    core.increment_count_html_object(unique_code=unique_code)
    return True


def delete_code(unique_code: str):
    Html.objects.get(unique_code=unique_code).delete()
    return True


def change_status(unique_code: str):
    html = Html.objects.get(unique_code=unique_code)
    if html.status == "private":
        html.status = "public"
    else:
        html.status = "private"
    html.save()
    return True


def get_single_code(unique_code: str):
    return get_html_details_from_object(html=Html.objects.get(unique_code=unique_code))
