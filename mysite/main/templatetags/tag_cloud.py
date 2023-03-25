from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("main/components/tag-cloud.html")
def sidebar_tag_cloud():
    x = Tag.objects.all()
    return {"tags": x}


# to be added to home.html
# {% tag_cloud %}
# {% sidebar_tag_cloud %}
