import itertools

from django import template

register = template.Library()

@register.filter
def chunks(values, chunk_size):
    values = iter(values)
    chunk_size = int(chunk_size)
    while True:
        chunk = list(itertools.islice(values, chunk_size))
        if chunk:
            yield chunk
        else:
            break
