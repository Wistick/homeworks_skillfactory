from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    with open('news/templatetags/censor.txt', 'r', encoding='UTF8') as file:
        file = file.readlines()[0].split()
        if isinstance(value, str):
            for word in file:
                value = value.replace(word, '#%$#')
            return str(value)
        raise ValueError('Нельзя пременить фильтр не к строке')
