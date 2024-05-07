from django import template
from menu.models import MenuItem
register = template.Library()
from pprint import pprint


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context):
    path = context.request.path[1:-1]
    path = 'menu' if path == 'base' else path
    nodes = MenuItem.objects.with_tree_fields()
    origin_node = nodes.first()
    target_node = nodes.get(url=path)
    return {"origin_node": origin_node,
            "target_node": target_node
            }


@register.inclusion_tag('ul.html')
def get_child_nodes(node, target_node):
    return {"nodes": node.children.with_tree_fields(),
            "target_node": target_node,
            "parents": target_node.ancestors()
            }


@register.inclusion_tag('ul_stop.html')
def get_child_nodes_stop(node):
    return {"nodes": node.children.with_tree_fields(),
            }

