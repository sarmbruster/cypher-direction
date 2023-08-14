# partial fork from ANTLR's Trees.py with a fub fixed

from io import StringIO
from antlr4.Token import Token
from antlr4.Utils import escapeWhitespace
from antlr4.tree.Tree import RuleNode, ErrorNode, TerminalNode, Tree, ParseTree

class Trees(object):

    @classmethod
    def findAllTokenNodes(cls, t:ParseTree, ttype:int):
        return cls.findAllNodes(t, ttype, True)

    @classmethod
    def findAllRuleNodes(cls, t:ParseTree, ruleIndex:int):
        return cls.findAllNodes(t, ruleIndex, False)

    @classmethod
    def findAllNodes(cls, t:ParseTree, index:int, findTokens:bool):
        nodes = []
        cls._findAllNodes(t, index, findTokens, nodes)
        return nodes

    @classmethod
    def _findAllNodes(cls, t:ParseTree, index:int, findTokens:bool, nodes:list):
        from antlr4.ParserRuleContext import ParserRuleContext
        # check this node (the root) first
        if findTokens and isinstance(t, TerminalNode):
            if t.symbol.type==index:
                nodes.append(t)
        elif not findTokens and isinstance(t, ParserRuleContext):
            if t.getRuleIndex() == index:
                nodes.append(t)
        # check children
        for i in range(0, t.getChildCount()):
            cls._findAllNodes(t.getChild(i), index, findTokens, nodes)

    @classmethod
    def descendants(cls, t:ParseTree):
        nodes = [t]
        for i in range(0, t.getChildCount()):
            nodes.extend(cls.descendants(t.getChild(i)))
        return nodes
