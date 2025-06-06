# The following has been generated automatically from src/core/expression/qgsexpressionnode.h
QgsExpressionNode.ntUnaryOperator = QgsExpressionNode.NodeType.ntUnaryOperator
QgsExpressionNode.ntBinaryOperator = QgsExpressionNode.NodeType.ntBinaryOperator
QgsExpressionNode.ntInOperator = QgsExpressionNode.NodeType.ntInOperator
QgsExpressionNode.ntFunction = QgsExpressionNode.NodeType.ntFunction
QgsExpressionNode.ntLiteral = QgsExpressionNode.NodeType.ntLiteral
QgsExpressionNode.ntColumnRef = QgsExpressionNode.NodeType.ntColumnRef
QgsExpressionNode.ntCondition = QgsExpressionNode.NodeType.ntCondition
QgsExpressionNode.ntIndexOperator = QgsExpressionNode.NodeType.ntIndexOperator
QgsExpressionNode.ntBetweenOperator = QgsExpressionNode.NodeType.ntBetweenOperator
try:
    QgsExpressionNode.NamedNode.__attribute_docs__ = {'name': 'Node name', 'node': 'Node'}
    QgsExpressionNode.NamedNode.__annotations__ = {'name': str, 'node': 'QgsExpressionNode'}
    QgsExpressionNode.NamedNode.__doc__ = """Named node"""
    QgsExpressionNode.NamedNode.__group__ = ['expression']
except (NameError, AttributeError):
    pass
try:
    QgsExpressionNode.__attribute_docs__ = {'parserFirstLine': 'First line in the parser this node was found.\n\n.. note::\n\n   This might not be complete for all nodes. Currently\n   only :py:class:`QgsExpressionNode` has this complete', 'parserFirstColumn': 'First column in the parser this node was found.\n\n.. note::\n\n   This might not be complete for all nodes. Currently\n   only :py:class:`QgsExpressionNode` has this complete', 'parserLastLine': 'Last line in the parser this node was found.\n\n.. note::\n\n   This might not be complete for all nodes. Currently\n   only :py:class:`QgsExpressionNode` has this complete', 'parserLastColumn': 'Last column in the parser this node was found.\n\n.. note::\n\n   This might not be complete for all nodes. Currently\n   only :py:class:`QgsExpressionNode` has this complete'}
    QgsExpressionNode.__annotations__ = {'parserFirstLine': int, 'parserFirstColumn': int, 'parserLastLine': int, 'parserLastColumn': int}
    QgsExpressionNode.__abstract_methods__ = ['nodeType', 'dump', 'clone', 'referencedColumns', 'referencedVariables', 'referencedFunctions', 'needsGeometry', 'isStatic']
    QgsExpressionNode.__group__ = ['expression']
except (NameError, AttributeError):
    pass
try:
    QgsExpressionNode.NodeList.__virtual_methods__ = ['dump']
    QgsExpressionNode.NodeList.__group__ = ['expression']
except (NameError, AttributeError):
    pass
