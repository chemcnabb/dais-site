from django import template
from itertools import cycle as itertools_cycle, groupby
register = template.Library()
from django.template.base import render_value_in_context, Node

@register.filter
def classname(obj):
    return obj.__class__.__name__


class CycleNode(Node):
    def __init__(self, cyclevars, variable_name=None, silent=False):
        self.cyclevars = cyclevars
        self.variable_name = variable_name
        self.silent = silent

    def render(self, context):
        if self not in context.render_context:
            # First time the node is rendered in template
            context.render_context[self] = itertools_cycle(self.cyclevars)
        cycle_iter = context.render_context[self]
        value = next(cycle_iter).resolve(context)
        if self.variable_name:
            context[self.variable_name] = value
        if self.silent:
            return ''
        return value


@register.simple_tag(takes_context=True)
def row_counter(context):


    row_count = context["row_count"]
    if row_count == 0:
        row_count = 1
    else:
        row_count = 0
    context["row_count"] = row_count
    return row_count