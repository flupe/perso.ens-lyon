from docutils import nodes

class icon(nodes.Inline, nodes.TextElement): pass
class annotation(nodes.General, nodes.Element): pass
class statement(nodes.General, nodes.Element): pass
