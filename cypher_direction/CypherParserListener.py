# Generated from /home/stefan/lib/neo4j/neo4j/community/cypher/front-end/antlr-parser/src/main/antlr4/org/neo4j/cypher/internal/parser/CypherParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser

# This class defines a complete listener for a parse tree produced by CypherParser.
class CypherParserListener(ParseTreeListener):

    # Enter a parse tree produced by CypherParser#statements.
    def enterStatements(self, ctx:CypherParser.StatementsContext):
        pass

    # Exit a parse tree produced by CypherParser#statements.
    def exitStatements(self, ctx:CypherParser.StatementsContext):
        pass


    # Enter a parse tree produced by CypherParser#statement.
    def enterStatement(self, ctx:CypherParser.StatementContext):
        pass

    # Exit a parse tree produced by CypherParser#statement.
    def exitStatement(self, ctx:CypherParser.StatementContext):
        pass


    # Enter a parse tree produced by CypherParser#singleQueryOrCommand.
    def enterSingleQueryOrCommand(self, ctx:CypherParser.SingleQueryOrCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#singleQueryOrCommand.
    def exitSingleQueryOrCommand(self, ctx:CypherParser.SingleQueryOrCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#singleQueryOrCommandWithUseClause.
    def enterSingleQueryOrCommandWithUseClause(self, ctx:CypherParser.SingleQueryOrCommandWithUseClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#singleQueryOrCommandWithUseClause.
    def exitSingleQueryOrCommandWithUseClause(self, ctx:CypherParser.SingleQueryOrCommandWithUseClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#periodicCommitQueryHintFailure.
    def enterPeriodicCommitQueryHintFailure(self, ctx:CypherParser.PeriodicCommitQueryHintFailureContext):
        pass

    # Exit a parse tree produced by CypherParser#periodicCommitQueryHintFailure.
    def exitPeriodicCommitQueryHintFailure(self, ctx:CypherParser.PeriodicCommitQueryHintFailureContext):
        pass


    # Enter a parse tree produced by CypherParser#regularQuery.
    def enterRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#regularQuery.
    def exitRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        pass


    # Enter a parse tree produced by CypherParser#union.
    def enterUnion(self, ctx:CypherParser.UnionContext):
        pass

    # Exit a parse tree produced by CypherParser#union.
    def exitUnion(self, ctx:CypherParser.UnionContext):
        pass


    # Enter a parse tree produced by CypherParser#singleQuery.
    def enterSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#singleQuery.
    def exitSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        pass


    # Enter a parse tree produced by CypherParser#singleQueryWithUseClause.
    def enterSingleQueryWithUseClause(self, ctx:CypherParser.SingleQueryWithUseClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#singleQueryWithUseClause.
    def exitSingleQueryWithUseClause(self, ctx:CypherParser.SingleQueryWithUseClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#clause.
    def enterClause(self, ctx:CypherParser.ClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#clause.
    def exitClause(self, ctx:CypherParser.ClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#useClause.
    def enterUseClause(self, ctx:CypherParser.UseClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#useClause.
    def exitUseClause(self, ctx:CypherParser.UseClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#returnClause.
    def enterReturnClause(self, ctx:CypherParser.ReturnClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#returnClause.
    def exitReturnClause(self, ctx:CypherParser.ReturnClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#returnBody.
    def enterReturnBody(self, ctx:CypherParser.ReturnBodyContext):
        pass

    # Exit a parse tree produced by CypherParser#returnBody.
    def exitReturnBody(self, ctx:CypherParser.ReturnBodyContext):
        pass


    # Enter a parse tree produced by CypherParser#returnItem.
    def enterReturnItem(self, ctx:CypherParser.ReturnItemContext):
        pass

    # Exit a parse tree produced by CypherParser#returnItem.
    def exitReturnItem(self, ctx:CypherParser.ReturnItemContext):
        pass


    # Enter a parse tree produced by CypherParser#returnItems.
    def enterReturnItems(self, ctx:CypherParser.ReturnItemsContext):
        pass

    # Exit a parse tree produced by CypherParser#returnItems.
    def exitReturnItems(self, ctx:CypherParser.ReturnItemsContext):
        pass


    # Enter a parse tree produced by CypherParser#orderItem.
    def enterOrderItem(self, ctx:CypherParser.OrderItemContext):
        pass

    # Exit a parse tree produced by CypherParser#orderItem.
    def exitOrderItem(self, ctx:CypherParser.OrderItemContext):
        pass


    # Enter a parse tree produced by CypherParser#skip.
    def enterSkip(self, ctx:CypherParser.SkipContext):
        pass

    # Exit a parse tree produced by CypherParser#skip.
    def exitSkip(self, ctx:CypherParser.SkipContext):
        pass


    # Enter a parse tree produced by CypherParser#limit.
    def enterLimit(self, ctx:CypherParser.LimitContext):
        pass

    # Exit a parse tree produced by CypherParser#limit.
    def exitLimit(self, ctx:CypherParser.LimitContext):
        pass


    # Enter a parse tree produced by CypherParser#whereClause.
    def enterWhereClause(self, ctx:CypherParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#whereClause.
    def exitWhereClause(self, ctx:CypherParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#withClause.
    def enterWithClause(self, ctx:CypherParser.WithClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#withClause.
    def exitWithClause(self, ctx:CypherParser.WithClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#createClause.
    def enterCreateClause(self, ctx:CypherParser.CreateClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#createClause.
    def exitCreateClause(self, ctx:CypherParser.CreateClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#setClause.
    def enterSetClause(self, ctx:CypherParser.SetClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#setClause.
    def exitSetClause(self, ctx:CypherParser.SetClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#setItem.
    def enterSetItem(self, ctx:CypherParser.SetItemContext):
        pass

    # Exit a parse tree produced by CypherParser#setItem.
    def exitSetItem(self, ctx:CypherParser.SetItemContext):
        pass


    # Enter a parse tree produced by CypherParser#removeClause.
    def enterRemoveClause(self, ctx:CypherParser.RemoveClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#removeClause.
    def exitRemoveClause(self, ctx:CypherParser.RemoveClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#removeItem.
    def enterRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        pass

    # Exit a parse tree produced by CypherParser#removeItem.
    def exitRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        pass


    # Enter a parse tree produced by CypherParser#deleteClause.
    def enterDeleteClause(self, ctx:CypherParser.DeleteClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#deleteClause.
    def exitDeleteClause(self, ctx:CypherParser.DeleteClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#matchClause.
    def enterMatchClause(self, ctx:CypherParser.MatchClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#matchClause.
    def exitMatchClause(self, ctx:CypherParser.MatchClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#matchMode.
    def enterMatchMode(self, ctx:CypherParser.MatchModeContext):
        pass

    # Exit a parse tree produced by CypherParser#matchMode.
    def exitMatchMode(self, ctx:CypherParser.MatchModeContext):
        pass


    # Enter a parse tree produced by CypherParser#hints.
    def enterHints(self, ctx:CypherParser.HintsContext):
        pass

    # Exit a parse tree produced by CypherParser#hints.
    def exitHints(self, ctx:CypherParser.HintsContext):
        pass


    # Enter a parse tree produced by CypherParser#indexHintBody.
    def enterIndexHintBody(self, ctx:CypherParser.IndexHintBodyContext):
        pass

    # Exit a parse tree produced by CypherParser#indexHintBody.
    def exitIndexHintBody(self, ctx:CypherParser.IndexHintBodyContext):
        pass


    # Enter a parse tree produced by CypherParser#mergeClause.
    def enterMergeClause(self, ctx:CypherParser.MergeClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#mergeClause.
    def exitMergeClause(self, ctx:CypherParser.MergeClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#unwindClause.
    def enterUnwindClause(self, ctx:CypherParser.UnwindClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#unwindClause.
    def exitUnwindClause(self, ctx:CypherParser.UnwindClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#callClause.
    def enterCallClause(self, ctx:CypherParser.CallClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#callClause.
    def exitCallClause(self, ctx:CypherParser.CallClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#procedureName.
    def enterProcedureName(self, ctx:CypherParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by CypherParser#procedureName.
    def exitProcedureName(self, ctx:CypherParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by CypherParser#procedureArgument.
    def enterProcedureArgument(self, ctx:CypherParser.ProcedureArgumentContext):
        pass

    # Exit a parse tree produced by CypherParser#procedureArgument.
    def exitProcedureArgument(self, ctx:CypherParser.ProcedureArgumentContext):
        pass


    # Enter a parse tree produced by CypherParser#procedureResultItem.
    def enterProcedureResultItem(self, ctx:CypherParser.ProcedureResultItemContext):
        pass

    # Exit a parse tree produced by CypherParser#procedureResultItem.
    def exitProcedureResultItem(self, ctx:CypherParser.ProcedureResultItemContext):
        pass


    # Enter a parse tree produced by CypherParser#loadCSVClause.
    def enterLoadCSVClause(self, ctx:CypherParser.LoadCSVClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#loadCSVClause.
    def exitLoadCSVClause(self, ctx:CypherParser.LoadCSVClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#foreachClause.
    def enterForeachClause(self, ctx:CypherParser.ForeachClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#foreachClause.
    def exitForeachClause(self, ctx:CypherParser.ForeachClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryClause.
    def enterSubqueryClause(self, ctx:CypherParser.SubqueryClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryClause.
    def exitSubqueryClause(self, ctx:CypherParser.SubqueryClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryInTransactionsParameters.
    def enterSubqueryInTransactionsParameters(self, ctx:CypherParser.SubqueryInTransactionsParametersContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryInTransactionsParameters.
    def exitSubqueryInTransactionsParameters(self, ctx:CypherParser.SubqueryInTransactionsParametersContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryInTransactionsBatchParameters.
    def enterSubqueryInTransactionsBatchParameters(self, ctx:CypherParser.SubqueryInTransactionsBatchParametersContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryInTransactionsBatchParameters.
    def exitSubqueryInTransactionsBatchParameters(self, ctx:CypherParser.SubqueryInTransactionsBatchParametersContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryInTransactionsErrorParameters.
    def enterSubqueryInTransactionsErrorParameters(self, ctx:CypherParser.SubqueryInTransactionsErrorParametersContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryInTransactionsErrorParameters.
    def exitSubqueryInTransactionsErrorParameters(self, ctx:CypherParser.SubqueryInTransactionsErrorParametersContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryInTransactionsReportParameters.
    def enterSubqueryInTransactionsReportParameters(self, ctx:CypherParser.SubqueryInTransactionsReportParametersContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryInTransactionsReportParameters.
    def exitSubqueryInTransactionsReportParameters(self, ctx:CypherParser.SubqueryInTransactionsReportParametersContext):
        pass


    # Enter a parse tree produced by CypherParser#patternList.
    def enterPatternList(self, ctx:CypherParser.PatternListContext):
        pass

    # Exit a parse tree produced by CypherParser#patternList.
    def exitPatternList(self, ctx:CypherParser.PatternListContext):
        pass


    # Enter a parse tree produced by CypherParser#pattern.
    def enterPattern(self, ctx:CypherParser.PatternContext):
        pass

    # Exit a parse tree produced by CypherParser#pattern.
    def exitPattern(self, ctx:CypherParser.PatternContext):
        pass


    # Enter a parse tree produced by CypherParser#quantifier.
    def enterQuantifier(self, ctx:CypherParser.QuantifierContext):
        pass

    # Exit a parse tree produced by CypherParser#quantifier.
    def exitQuantifier(self, ctx:CypherParser.QuantifierContext):
        pass


    # Enter a parse tree produced by CypherParser#anonymousPattern.
    def enterAnonymousPattern(self, ctx:CypherParser.AnonymousPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#anonymousPattern.
    def exitAnonymousPattern(self, ctx:CypherParser.AnonymousPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#shortestPathPattern.
    def enterShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#shortestPathPattern.
    def exitShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#maybeQuantifiedRelationshipPattern.
    def enterMaybeQuantifiedRelationshipPattern(self, ctx:CypherParser.MaybeQuantifiedRelationshipPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#maybeQuantifiedRelationshipPattern.
    def exitMaybeQuantifiedRelationshipPattern(self, ctx:CypherParser.MaybeQuantifiedRelationshipPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#patternElement.
    def enterPatternElement(self, ctx:CypherParser.PatternElementContext):
        pass

    # Exit a parse tree produced by CypherParser#patternElement.
    def exitPatternElement(self, ctx:CypherParser.PatternElementContext):
        pass


    # Enter a parse tree produced by CypherParser#pathPatternAtoms.
    def enterPathPatternAtoms(self, ctx:CypherParser.PathPatternAtomsContext):
        pass

    # Exit a parse tree produced by CypherParser#pathPatternAtoms.
    def exitPathPatternAtoms(self, ctx:CypherParser.PathPatternAtomsContext):
        pass


    # Enter a parse tree produced by CypherParser#selector.
    def enterSelector(self, ctx:CypherParser.SelectorContext):
        pass

    # Exit a parse tree produced by CypherParser#selector.
    def exitSelector(self, ctx:CypherParser.SelectorContext):
        pass


    # Enter a parse tree produced by CypherParser#pathPatternNonEmpty.
    def enterPathPatternNonEmpty(self, ctx:CypherParser.PathPatternNonEmptyContext):
        pass

    # Exit a parse tree produced by CypherParser#pathPatternNonEmpty.
    def exitPathPatternNonEmpty(self, ctx:CypherParser.PathPatternNonEmptyContext):
        pass


    # Enter a parse tree produced by CypherParser#nodePattern.
    def enterNodePattern(self, ctx:CypherParser.NodePatternContext):
        pass

    # Exit a parse tree produced by CypherParser#nodePattern.
    def exitNodePattern(self, ctx:CypherParser.NodePatternContext):
        pass


    # Enter a parse tree produced by CypherParser#parenthesizedPath.
    def enterParenthesizedPath(self, ctx:CypherParser.ParenthesizedPathContext):
        pass

    # Exit a parse tree produced by CypherParser#parenthesizedPath.
    def exitParenthesizedPath(self, ctx:CypherParser.ParenthesizedPathContext):
        pass


    # Enter a parse tree produced by CypherParser#nodeLabels.
    def enterNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        pass

    # Exit a parse tree produced by CypherParser#nodeLabels.
    def exitNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpressionPredicate.
    def enterLabelExpressionPredicate(self, ctx:CypherParser.LabelExpressionPredicateContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpressionPredicate.
    def exitLabelExpressionPredicate(self, ctx:CypherParser.LabelExpressionPredicateContext):
        pass


    # Enter a parse tree produced by CypherParser#labelOrRelType.
    def enterLabelOrRelType(self, ctx:CypherParser.LabelOrRelTypeContext):
        pass

    # Exit a parse tree produced by CypherParser#labelOrRelType.
    def exitLabelOrRelType(self, ctx:CypherParser.LabelOrRelTypeContext):
        pass


    # Enter a parse tree produced by CypherParser#labelOrRelTypes.
    def enterLabelOrRelTypes(self, ctx:CypherParser.LabelOrRelTypesContext):
        pass

    # Exit a parse tree produced by CypherParser#labelOrRelTypes.
    def exitLabelOrRelTypes(self, ctx:CypherParser.LabelOrRelTypesContext):
        pass


    # Enter a parse tree produced by CypherParser#properties.
    def enterProperties(self, ctx:CypherParser.PropertiesContext):
        pass

    # Exit a parse tree produced by CypherParser#properties.
    def exitProperties(self, ctx:CypherParser.PropertiesContext):
        pass


    # Enter a parse tree produced by CypherParser#relationshipPattern.
    def enterRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#relationshipPattern.
    def exitRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#leftArrow.
    def enterLeftArrow(self, ctx:CypherParser.LeftArrowContext):
        pass

    # Exit a parse tree produced by CypherParser#leftArrow.
    def exitLeftArrow(self, ctx:CypherParser.LeftArrowContext):
        pass


    # Enter a parse tree produced by CypherParser#arrowLine.
    def enterArrowLine(self, ctx:CypherParser.ArrowLineContext):
        pass

    # Exit a parse tree produced by CypherParser#arrowLine.
    def exitArrowLine(self, ctx:CypherParser.ArrowLineContext):
        pass


    # Enter a parse tree produced by CypherParser#rightArrow.
    def enterRightArrow(self, ctx:CypherParser.RightArrowContext):
        pass

    # Exit a parse tree produced by CypherParser#rightArrow.
    def exitRightArrow(self, ctx:CypherParser.RightArrowContext):
        pass


    # Enter a parse tree produced by CypherParser#pathLength.
    def enterPathLength(self, ctx:CypherParser.PathLengthContext):
        pass

    # Exit a parse tree produced by CypherParser#pathLength.
    def exitPathLength(self, ctx:CypherParser.PathLengthContext):
        pass


    # Enter a parse tree produced by CypherParser#pathLengthLiteral.
    def enterPathLengthLiteral(self, ctx:CypherParser.PathLengthLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#pathLengthLiteral.
    def exitPathLengthLiteral(self, ctx:CypherParser.PathLengthLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression.
    def enterLabelExpression(self, ctx:CypherParser.LabelExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression.
    def exitLabelExpression(self, ctx:CypherParser.LabelExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression4.
    def enterLabelExpression4(self, ctx:CypherParser.LabelExpression4Context):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression4.
    def exitLabelExpression4(self, ctx:CypherParser.LabelExpression4Context):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression4Is.
    def enterLabelExpression4Is(self, ctx:CypherParser.LabelExpression4IsContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression4Is.
    def exitLabelExpression4Is(self, ctx:CypherParser.LabelExpression4IsContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression3.
    def enterLabelExpression3(self, ctx:CypherParser.LabelExpression3Context):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression3.
    def exitLabelExpression3(self, ctx:CypherParser.LabelExpression3Context):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression3Is.
    def enterLabelExpression3Is(self, ctx:CypherParser.LabelExpression3IsContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression3Is.
    def exitLabelExpression3Is(self, ctx:CypherParser.LabelExpression3IsContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression2.
    def enterLabelExpression2(self, ctx:CypherParser.LabelExpression2Context):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression2.
    def exitLabelExpression2(self, ctx:CypherParser.LabelExpression2Context):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression2Is.
    def enterLabelExpression2Is(self, ctx:CypherParser.LabelExpression2IsContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression2Is.
    def exitLabelExpression2Is(self, ctx:CypherParser.LabelExpression2IsContext):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression1.
    def enterLabelExpression1(self, ctx:CypherParser.LabelExpression1Context):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression1.
    def exitLabelExpression1(self, ctx:CypherParser.LabelExpression1Context):
        pass


    # Enter a parse tree produced by CypherParser#labelExpression1Is.
    def enterLabelExpression1Is(self, ctx:CypherParser.LabelExpression1IsContext):
        pass

    # Exit a parse tree produced by CypherParser#labelExpression1Is.
    def exitLabelExpression1Is(self, ctx:CypherParser.LabelExpression1IsContext):
        pass


    # Enter a parse tree produced by CypherParser#expression.
    def enterExpression(self, ctx:CypherParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#expression.
    def exitExpression(self, ctx:CypherParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#expression12.
    def enterExpression12(self, ctx:CypherParser.Expression12Context):
        pass

    # Exit a parse tree produced by CypherParser#expression12.
    def exitExpression12(self, ctx:CypherParser.Expression12Context):
        pass


    # Enter a parse tree produced by CypherParser#expression11.
    def enterExpression11(self, ctx:CypherParser.Expression11Context):
        pass

    # Exit a parse tree produced by CypherParser#expression11.
    def exitExpression11(self, ctx:CypherParser.Expression11Context):
        pass


    # Enter a parse tree produced by CypherParser#expression10.
    def enterExpression10(self, ctx:CypherParser.Expression10Context):
        pass

    # Exit a parse tree produced by CypherParser#expression10.
    def exitExpression10(self, ctx:CypherParser.Expression10Context):
        pass


    # Enter a parse tree produced by CypherParser#expression9.
    def enterExpression9(self, ctx:CypherParser.Expression9Context):
        pass

    # Exit a parse tree produced by CypherParser#expression9.
    def exitExpression9(self, ctx:CypherParser.Expression9Context):
        pass


    # Enter a parse tree produced by CypherParser#expression8.
    def enterExpression8(self, ctx:CypherParser.Expression8Context):
        pass

    # Exit a parse tree produced by CypherParser#expression8.
    def exitExpression8(self, ctx:CypherParser.Expression8Context):
        pass


    # Enter a parse tree produced by CypherParser#expression7.
    def enterExpression7(self, ctx:CypherParser.Expression7Context):
        pass

    # Exit a parse tree produced by CypherParser#expression7.
    def exitExpression7(self, ctx:CypherParser.Expression7Context):
        pass


    # Enter a parse tree produced by CypherParser#comparisonExpression6.
    def enterComparisonExpression6(self, ctx:CypherParser.ComparisonExpression6Context):
        pass

    # Exit a parse tree produced by CypherParser#comparisonExpression6.
    def exitComparisonExpression6(self, ctx:CypherParser.ComparisonExpression6Context):
        pass


    # Enter a parse tree produced by CypherParser#expression6.
    def enterExpression6(self, ctx:CypherParser.Expression6Context):
        pass

    # Exit a parse tree produced by CypherParser#expression6.
    def exitExpression6(self, ctx:CypherParser.Expression6Context):
        pass


    # Enter a parse tree produced by CypherParser#expression5.
    def enterExpression5(self, ctx:CypherParser.Expression5Context):
        pass

    # Exit a parse tree produced by CypherParser#expression5.
    def exitExpression5(self, ctx:CypherParser.Expression5Context):
        pass


    # Enter a parse tree produced by CypherParser#expression4.
    def enterExpression4(self, ctx:CypherParser.Expression4Context):
        pass

    # Exit a parse tree produced by CypherParser#expression4.
    def exitExpression4(self, ctx:CypherParser.Expression4Context):
        pass


    # Enter a parse tree produced by CypherParser#expression3.
    def enterExpression3(self, ctx:CypherParser.Expression3Context):
        pass

    # Exit a parse tree produced by CypherParser#expression3.
    def exitExpression3(self, ctx:CypherParser.Expression3Context):
        pass


    # Enter a parse tree produced by CypherParser#expression2.
    def enterExpression2(self, ctx:CypherParser.Expression2Context):
        pass

    # Exit a parse tree produced by CypherParser#expression2.
    def exitExpression2(self, ctx:CypherParser.Expression2Context):
        pass


    # Enter a parse tree produced by CypherParser#postFix1.
    def enterPostFix1(self, ctx:CypherParser.PostFix1Context):
        pass

    # Exit a parse tree produced by CypherParser#postFix1.
    def exitPostFix1(self, ctx:CypherParser.PostFix1Context):
        pass


    # Enter a parse tree produced by CypherParser#property.
    def enterProperty(self, ctx:CypherParser.PropertyContext):
        pass

    # Exit a parse tree produced by CypherParser#property.
    def exitProperty(self, ctx:CypherParser.PropertyContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyExpression.
    def enterPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyExpression.
    def exitPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#expression1.
    def enterExpression1(self, ctx:CypherParser.Expression1Context):
        pass

    # Exit a parse tree produced by CypherParser#expression1.
    def exitExpression1(self, ctx:CypherParser.Expression1Context):
        pass


    # Enter a parse tree produced by CypherParser#NummericLiteral.
    def enterNummericLiteral(self, ctx:CypherParser.NummericLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#NummericLiteral.
    def exitNummericLiteral(self, ctx:CypherParser.NummericLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#StringsLiteral.
    def enterStringsLiteral(self, ctx:CypherParser.StringsLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#StringsLiteral.
    def exitStringsLiteral(self, ctx:CypherParser.StringsLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#OtherLiteral.
    def enterOtherLiteral(self, ctx:CypherParser.OtherLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#OtherLiteral.
    def exitOtherLiteral(self, ctx:CypherParser.OtherLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#BooleanLiteral.
    def enterBooleanLiteral(self, ctx:CypherParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#BooleanLiteral.
    def exitBooleanLiteral(self, ctx:CypherParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#KeywordLiteral.
    def enterKeywordLiteral(self, ctx:CypherParser.KeywordLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#KeywordLiteral.
    def exitKeywordLiteral(self, ctx:CypherParser.KeywordLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#caseExpression.
    def enterCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#caseExpression.
    def exitCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#listComprehension.
    def enterListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by CypherParser#listComprehension.
    def exitListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by CypherParser#listComprehensionWhereAndBar.
    def enterListComprehensionWhereAndBar(self, ctx:CypherParser.ListComprehensionWhereAndBarContext):
        pass

    # Exit a parse tree produced by CypherParser#listComprehensionWhereAndBar.
    def exitListComprehensionWhereAndBar(self, ctx:CypherParser.ListComprehensionWhereAndBarContext):
        pass


    # Enter a parse tree produced by CypherParser#patternComprehension.
    def enterPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        pass

    # Exit a parse tree produced by CypherParser#patternComprehension.
    def exitPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        pass


    # Enter a parse tree produced by CypherParser#patternComprehensionPrefix.
    def enterPatternComprehensionPrefix(self, ctx:CypherParser.PatternComprehensionPrefixContext):
        pass

    # Exit a parse tree produced by CypherParser#patternComprehensionPrefix.
    def exitPatternComprehensionPrefix(self, ctx:CypherParser.PatternComprehensionPrefixContext):
        pass


    # Enter a parse tree produced by CypherParser#reduceExpression.
    def enterReduceExpression(self, ctx:CypherParser.ReduceExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#reduceExpression.
    def exitReduceExpression(self, ctx:CypherParser.ReduceExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#allExpression.
    def enterAllExpression(self, ctx:CypherParser.AllExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#allExpression.
    def exitAllExpression(self, ctx:CypherParser.AllExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#anyExpression.
    def enterAnyExpression(self, ctx:CypherParser.AnyExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#anyExpression.
    def exitAnyExpression(self, ctx:CypherParser.AnyExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#noneExpression.
    def enterNoneExpression(self, ctx:CypherParser.NoneExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#noneExpression.
    def exitNoneExpression(self, ctx:CypherParser.NoneExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#singleExpression.
    def enterSingleExpression(self, ctx:CypherParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#singleExpression.
    def exitSingleExpression(self, ctx:CypherParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#patternExpression.
    def enterPatternExpression(self, ctx:CypherParser.PatternExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#patternExpression.
    def exitPatternExpression(self, ctx:CypherParser.PatternExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#shortestPathExpression.
    def enterShortestPathExpression(self, ctx:CypherParser.ShortestPathExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#shortestPathExpression.
    def exitShortestPathExpression(self, ctx:CypherParser.ShortestPathExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#mapProjection.
    def enterMapProjection(self, ctx:CypherParser.MapProjectionContext):
        pass

    # Exit a parse tree produced by CypherParser#mapProjection.
    def exitMapProjection(self, ctx:CypherParser.MapProjectionContext):
        pass


    # Enter a parse tree produced by CypherParser#mapProjectionItem.
    def enterMapProjectionItem(self, ctx:CypherParser.MapProjectionItemContext):
        pass

    # Exit a parse tree produced by CypherParser#mapProjectionItem.
    def exitMapProjectionItem(self, ctx:CypherParser.MapProjectionItemContext):
        pass


    # Enter a parse tree produced by CypherParser#existsExpression.
    def enterExistsExpression(self, ctx:CypherParser.ExistsExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#existsExpression.
    def exitExistsExpression(self, ctx:CypherParser.ExistsExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#countExpression.
    def enterCountExpression(self, ctx:CypherParser.CountExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#countExpression.
    def exitCountExpression(self, ctx:CypherParser.CountExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#collectExpression.
    def enterCollectExpression(self, ctx:CypherParser.CollectExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#collectExpression.
    def exitCollectExpression(self, ctx:CypherParser.CollectExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#stringLiteral.
    def enterStringLiteral(self, ctx:CypherParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#stringLiteral.
    def exitStringLiteral(self, ctx:CypherParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#numberLiteral.
    def enterNumberLiteral(self, ctx:CypherParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#numberLiteral.
    def exitNumberLiteral(self, ctx:CypherParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#signedIntegerLiteral.
    def enterSignedIntegerLiteral(self, ctx:CypherParser.SignedIntegerLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#signedIntegerLiteral.
    def exitSignedIntegerLiteral(self, ctx:CypherParser.SignedIntegerLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#listLiteral.
    def enterListLiteral(self, ctx:CypherParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#listLiteral.
    def exitListLiteral(self, ctx:CypherParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#mapLiteral.
    def enterMapLiteral(self, ctx:CypherParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#mapLiteral.
    def exitMapLiteral(self, ctx:CypherParser.MapLiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyKeyName.
    def enterPropertyKeyName(self, ctx:CypherParser.PropertyKeyNameContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyKeyName.
    def exitPropertyKeyName(self, ctx:CypherParser.PropertyKeyNameContext):
        pass


    # Enter a parse tree produced by CypherParser#parameter.
    def enterParameter(self, ctx:CypherParser.ParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#parameter.
    def exitParameter(self, ctx:CypherParser.ParameterContext):
        pass


    # Enter a parse tree produced by CypherParser#parameterName.
    def enterParameterName(self, ctx:CypherParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by CypherParser#parameterName.
    def exitParameterName(self, ctx:CypherParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by CypherParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by CypherParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by CypherParser#functionName.
    def enterFunctionName(self, ctx:CypherParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CypherParser#functionName.
    def exitFunctionName(self, ctx:CypherParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CypherParser#functionArgument.
    def enterFunctionArgument(self, ctx:CypherParser.FunctionArgumentContext):
        pass

    # Exit a parse tree produced by CypherParser#functionArgument.
    def exitFunctionArgument(self, ctx:CypherParser.FunctionArgumentContext):
        pass


    # Enter a parse tree produced by CypherParser#namespace.
    def enterNamespace(self, ctx:CypherParser.NamespaceContext):
        pass

    # Exit a parse tree produced by CypherParser#namespace.
    def exitNamespace(self, ctx:CypherParser.NamespaceContext):
        pass


    # Enter a parse tree produced by CypherParser#variableList1.
    def enterVariableList1(self, ctx:CypherParser.VariableList1Context):
        pass

    # Exit a parse tree produced by CypherParser#variableList1.
    def exitVariableList1(self, ctx:CypherParser.VariableList1Context):
        pass


    # Enter a parse tree produced by CypherParser#variable.
    def enterVariable(self, ctx:CypherParser.VariableContext):
        pass

    # Exit a parse tree produced by CypherParser#variable.
    def exitVariable(self, ctx:CypherParser.VariableContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicNameList1.
    def enterSymbolicNameList1(self, ctx:CypherParser.SymbolicNameList1Context):
        pass

    # Exit a parse tree produced by CypherParser#symbolicNameList1.
    def exitSymbolicNameList1(self, ctx:CypherParser.SymbolicNameList1Context):
        pass


    # Enter a parse tree produced by CypherParser#createCommand.
    def enterCreateCommand(self, ctx:CypherParser.CreateCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#createCommand.
    def exitCreateCommand(self, ctx:CypherParser.CreateCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#command.
    def enterCommand(self, ctx:CypherParser.CommandContext):
        pass

    # Exit a parse tree produced by CypherParser#command.
    def exitCommand(self, ctx:CypherParser.CommandContext):
        pass


    # Enter a parse tree produced by CypherParser#commandWithUseGraph.
    def enterCommandWithUseGraph(self, ctx:CypherParser.CommandWithUseGraphContext):
        pass

    # Exit a parse tree produced by CypherParser#commandWithUseGraph.
    def exitCommandWithUseGraph(self, ctx:CypherParser.CommandWithUseGraphContext):
        pass


    # Enter a parse tree produced by CypherParser#dropCommand.
    def enterDropCommand(self, ctx:CypherParser.DropCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#dropCommand.
    def exitDropCommand(self, ctx:CypherParser.DropCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#alterCommand.
    def enterAlterCommand(self, ctx:CypherParser.AlterCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#alterCommand.
    def exitAlterCommand(self, ctx:CypherParser.AlterCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showCommand.
    def enterShowCommand(self, ctx:CypherParser.ShowCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showCommand.
    def exitShowCommand(self, ctx:CypherParser.ShowCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#terminateCommand.
    def enterTerminateCommand(self, ctx:CypherParser.TerminateCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#terminateCommand.
    def exitTerminateCommand(self, ctx:CypherParser.TerminateCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showAllCommand.
    def enterShowAllCommand(self, ctx:CypherParser.ShowAllCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showAllCommand.
    def exitShowAllCommand(self, ctx:CypherParser.ShowAllCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showNodeCommand.
    def enterShowNodeCommand(self, ctx:CypherParser.ShowNodeCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showNodeCommand.
    def exitShowNodeCommand(self, ctx:CypherParser.ShowNodeCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showRelationshipCommand.
    def enterShowRelationshipCommand(self, ctx:CypherParser.ShowRelationshipCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showRelationshipCommand.
    def exitShowRelationshipCommand(self, ctx:CypherParser.ShowRelationshipCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showRelCommand.
    def enterShowRelCommand(self, ctx:CypherParser.ShowRelCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showRelCommand.
    def exitShowRelCommand(self, ctx:CypherParser.ShowRelCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#showPropertyCommand.
    def enterShowPropertyCommand(self, ctx:CypherParser.ShowPropertyCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#showPropertyCommand.
    def exitShowPropertyCommand(self, ctx:CypherParser.ShowPropertyCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#yieldItem.
    def enterYieldItem(self, ctx:CypherParser.YieldItemContext):
        pass

    # Exit a parse tree produced by CypherParser#yieldItem.
    def exitYieldItem(self, ctx:CypherParser.YieldItemContext):
        pass


    # Enter a parse tree produced by CypherParser#yieldClause.
    def enterYieldClause(self, ctx:CypherParser.YieldClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#yieldClause.
    def exitYieldClause(self, ctx:CypherParser.YieldClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#showIndexesAllowBrief.
    def enterShowIndexesAllowBrief(self, ctx:CypherParser.ShowIndexesAllowBriefContext):
        pass

    # Exit a parse tree produced by CypherParser#showIndexesAllowBrief.
    def exitShowIndexesAllowBrief(self, ctx:CypherParser.ShowIndexesAllowBriefContext):
        pass


    # Enter a parse tree produced by CypherParser#showIndexesNoBrief.
    def enterShowIndexesNoBrief(self, ctx:CypherParser.ShowIndexesNoBriefContext):
        pass

    # Exit a parse tree produced by CypherParser#showIndexesNoBrief.
    def exitShowIndexesNoBrief(self, ctx:CypherParser.ShowIndexesNoBriefContext):
        pass


    # Enter a parse tree produced by CypherParser#showConstraintsAllowBriefAndYield.
    def enterShowConstraintsAllowBriefAndYield(self, ctx:CypherParser.ShowConstraintsAllowBriefAndYieldContext):
        pass

    # Exit a parse tree produced by CypherParser#showConstraintsAllowBriefAndYield.
    def exitShowConstraintsAllowBriefAndYield(self, ctx:CypherParser.ShowConstraintsAllowBriefAndYieldContext):
        pass


    # Enter a parse tree produced by CypherParser#showConstraintsAllowBrief.
    def enterShowConstraintsAllowBrief(self, ctx:CypherParser.ShowConstraintsAllowBriefContext):
        pass

    # Exit a parse tree produced by CypherParser#showConstraintsAllowBrief.
    def exitShowConstraintsAllowBrief(self, ctx:CypherParser.ShowConstraintsAllowBriefContext):
        pass


    # Enter a parse tree produced by CypherParser#showConstraintsAllowYield.
    def enterShowConstraintsAllowYield(self, ctx:CypherParser.ShowConstraintsAllowYieldContext):
        pass

    # Exit a parse tree produced by CypherParser#showConstraintsAllowYield.
    def exitShowConstraintsAllowYield(self, ctx:CypherParser.ShowConstraintsAllowYieldContext):
        pass


    # Enter a parse tree produced by CypherParser#showProcedures.
    def enterShowProcedures(self, ctx:CypherParser.ShowProceduresContext):
        pass

    # Exit a parse tree produced by CypherParser#showProcedures.
    def exitShowProcedures(self, ctx:CypherParser.ShowProceduresContext):
        pass


    # Enter a parse tree produced by CypherParser#showFunctions.
    def enterShowFunctions(self, ctx:CypherParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by CypherParser#showFunctions.
    def exitShowFunctions(self, ctx:CypherParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by CypherParser#showTransactions.
    def enterShowTransactions(self, ctx:CypherParser.ShowTransactionsContext):
        pass

    # Exit a parse tree produced by CypherParser#showTransactions.
    def exitShowTransactions(self, ctx:CypherParser.ShowTransactionsContext):
        pass


    # Enter a parse tree produced by CypherParser#terminateTransactions.
    def enterTerminateTransactions(self, ctx:CypherParser.TerminateTransactionsContext):
        pass

    # Exit a parse tree produced by CypherParser#terminateTransactions.
    def exitTerminateTransactions(self, ctx:CypherParser.TerminateTransactionsContext):
        pass


    # Enter a parse tree produced by CypherParser#showOrTerminateTransactions.
    def enterShowOrTerminateTransactions(self, ctx:CypherParser.ShowOrTerminateTransactionsContext):
        pass

    # Exit a parse tree produced by CypherParser#showOrTerminateTransactions.
    def exitShowOrTerminateTransactions(self, ctx:CypherParser.ShowOrTerminateTransactionsContext):
        pass


    # Enter a parse tree produced by CypherParser#stringsOrExpression.
    def enterStringsOrExpression(self, ctx:CypherParser.StringsOrExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#stringsOrExpression.
    def exitStringsOrExpression(self, ctx:CypherParser.StringsOrExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#showSettings.
    def enterShowSettings(self, ctx:CypherParser.ShowSettingsContext):
        pass

    # Exit a parse tree produced by CypherParser#showSettings.
    def exitShowSettings(self, ctx:CypherParser.ShowSettingsContext):
        pass


    # Enter a parse tree produced by CypherParser#createConstraint.
    def enterCreateConstraint(self, ctx:CypherParser.CreateConstraintContext):
        pass

    # Exit a parse tree produced by CypherParser#createConstraint.
    def exitCreateConstraint(self, ctx:CypherParser.CreateConstraintContext):
        pass


    # Enter a parse tree produced by CypherParser#cypherTypeName.
    def enterCypherTypeName(self, ctx:CypherParser.CypherTypeNameContext):
        pass

    # Exit a parse tree produced by CypherParser#cypherTypeName.
    def exitCypherTypeName(self, ctx:CypherParser.CypherTypeNameContext):
        pass


    # Enter a parse tree produced by CypherParser#constraintNodePattern.
    def enterConstraintNodePattern(self, ctx:CypherParser.ConstraintNodePatternContext):
        pass

    # Exit a parse tree produced by CypherParser#constraintNodePattern.
    def exitConstraintNodePattern(self, ctx:CypherParser.ConstraintNodePatternContext):
        pass


    # Enter a parse tree produced by CypherParser#constraintRelPattern.
    def enterConstraintRelPattern(self, ctx:CypherParser.ConstraintRelPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#constraintRelPattern.
    def exitConstraintRelPattern(self, ctx:CypherParser.ConstraintRelPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#createConstraintNodeCheck.
    def enterCreateConstraintNodeCheck(self, ctx:CypherParser.CreateConstraintNodeCheckContext):
        pass

    # Exit a parse tree produced by CypherParser#createConstraintNodeCheck.
    def exitCreateConstraintNodeCheck(self, ctx:CypherParser.CreateConstraintNodeCheckContext):
        pass


    # Enter a parse tree produced by CypherParser#createConstraintRelCheck.
    def enterCreateConstraintRelCheck(self, ctx:CypherParser.CreateConstraintRelCheckContext):
        pass

    # Exit a parse tree produced by CypherParser#createConstraintRelCheck.
    def exitCreateConstraintRelCheck(self, ctx:CypherParser.CreateConstraintRelCheckContext):
        pass


    # Enter a parse tree produced by CypherParser#dropConstraint.
    def enterDropConstraint(self, ctx:CypherParser.DropConstraintContext):
        pass

    # Exit a parse tree produced by CypherParser#dropConstraint.
    def exitDropConstraint(self, ctx:CypherParser.DropConstraintContext):
        pass


    # Enter a parse tree produced by CypherParser#dropConstraintNodeCheck.
    def enterDropConstraintNodeCheck(self, ctx:CypherParser.DropConstraintNodeCheckContext):
        pass

    # Exit a parse tree produced by CypherParser#dropConstraintNodeCheck.
    def exitDropConstraintNodeCheck(self, ctx:CypherParser.DropConstraintNodeCheckContext):
        pass


    # Enter a parse tree produced by CypherParser#createIndex.
    def enterCreateIndex(self, ctx:CypherParser.CreateIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#createIndex.
    def exitCreateIndex(self, ctx:CypherParser.CreateIndexContext):
        pass


    # Enter a parse tree produced by CypherParser#oldCreateIndex.
    def enterOldCreateIndex(self, ctx:CypherParser.OldCreateIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#oldCreateIndex.
    def exitOldCreateIndex(self, ctx:CypherParser.OldCreateIndexContext):
        pass


    # Enter a parse tree produced by CypherParser#createIndex_.
    def enterCreateIndex_(self, ctx:CypherParser.CreateIndex_Context):
        pass

    # Exit a parse tree produced by CypherParser#createIndex_.
    def exitCreateIndex_(self, ctx:CypherParser.CreateIndex_Context):
        pass


    # Enter a parse tree produced by CypherParser#createFulltextIndex.
    def enterCreateFulltextIndex(self, ctx:CypherParser.CreateFulltextIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#createFulltextIndex.
    def exitCreateFulltextIndex(self, ctx:CypherParser.CreateFulltextIndexContext):
        pass


    # Enter a parse tree produced by CypherParser#createLookupIndex.
    def enterCreateLookupIndex(self, ctx:CypherParser.CreateLookupIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#createLookupIndex.
    def exitCreateLookupIndex(self, ctx:CypherParser.CreateLookupIndexContext):
        pass


    # Enter a parse tree produced by CypherParser#lookupIndexFunctionName.
    def enterLookupIndexFunctionName(self, ctx:CypherParser.LookupIndexFunctionNameContext):
        pass

    # Exit a parse tree produced by CypherParser#lookupIndexFunctionName.
    def exitLookupIndexFunctionName(self, ctx:CypherParser.LookupIndexFunctionNameContext):
        pass


    # Enter a parse tree produced by CypherParser#dropIndex.
    def enterDropIndex(self, ctx:CypherParser.DropIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#dropIndex.
    def exitDropIndex(self, ctx:CypherParser.DropIndexContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyList.
    def enterPropertyList(self, ctx:CypherParser.PropertyListContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyList.
    def exitPropertyList(self, ctx:CypherParser.PropertyListContext):
        pass


    # Enter a parse tree produced by CypherParser#renameCommand.
    def enterRenameCommand(self, ctx:CypherParser.RenameCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#renameCommand.
    def exitRenameCommand(self, ctx:CypherParser.RenameCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#grantCommand.
    def enterGrantCommand(self, ctx:CypherParser.GrantCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#grantCommand.
    def exitGrantCommand(self, ctx:CypherParser.GrantCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#revokeCommand.
    def enterRevokeCommand(self, ctx:CypherParser.RevokeCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#revokeCommand.
    def exitRevokeCommand(self, ctx:CypherParser.RevokeCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#enableServerCommand.
    def enterEnableServerCommand(self, ctx:CypherParser.EnableServerCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#enableServerCommand.
    def exitEnableServerCommand(self, ctx:CypherParser.EnableServerCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#alterServer.
    def enterAlterServer(self, ctx:CypherParser.AlterServerContext):
        pass

    # Exit a parse tree produced by CypherParser#alterServer.
    def exitAlterServer(self, ctx:CypherParser.AlterServerContext):
        pass


    # Enter a parse tree produced by CypherParser#renameServer.
    def enterRenameServer(self, ctx:CypherParser.RenameServerContext):
        pass

    # Exit a parse tree produced by CypherParser#renameServer.
    def exitRenameServer(self, ctx:CypherParser.RenameServerContext):
        pass


    # Enter a parse tree produced by CypherParser#dropServer.
    def enterDropServer(self, ctx:CypherParser.DropServerContext):
        pass

    # Exit a parse tree produced by CypherParser#dropServer.
    def exitDropServer(self, ctx:CypherParser.DropServerContext):
        pass


    # Enter a parse tree produced by CypherParser#showServers.
    def enterShowServers(self, ctx:CypherParser.ShowServersContext):
        pass

    # Exit a parse tree produced by CypherParser#showServers.
    def exitShowServers(self, ctx:CypherParser.ShowServersContext):
        pass


    # Enter a parse tree produced by CypherParser#allocationCommand.
    def enterAllocationCommand(self, ctx:CypherParser.AllocationCommandContext):
        pass

    # Exit a parse tree produced by CypherParser#allocationCommand.
    def exitAllocationCommand(self, ctx:CypherParser.AllocationCommandContext):
        pass


    # Enter a parse tree produced by CypherParser#deallocateDatabaseFromServers.
    def enterDeallocateDatabaseFromServers(self, ctx:CypherParser.DeallocateDatabaseFromServersContext):
        pass

    # Exit a parse tree produced by CypherParser#deallocateDatabaseFromServers.
    def exitDeallocateDatabaseFromServers(self, ctx:CypherParser.DeallocateDatabaseFromServersContext):
        pass


    # Enter a parse tree produced by CypherParser#reallocateDatabases.
    def enterReallocateDatabases(self, ctx:CypherParser.ReallocateDatabasesContext):
        pass

    # Exit a parse tree produced by CypherParser#reallocateDatabases.
    def exitReallocateDatabases(self, ctx:CypherParser.ReallocateDatabasesContext):
        pass


    # Enter a parse tree produced by CypherParser#createRole.
    def enterCreateRole(self, ctx:CypherParser.CreateRoleContext):
        pass

    # Exit a parse tree produced by CypherParser#createRole.
    def exitCreateRole(self, ctx:CypherParser.CreateRoleContext):
        pass


    # Enter a parse tree produced by CypherParser#dropRole.
    def enterDropRole(self, ctx:CypherParser.DropRoleContext):
        pass

    # Exit a parse tree produced by CypherParser#dropRole.
    def exitDropRole(self, ctx:CypherParser.DropRoleContext):
        pass


    # Enter a parse tree produced by CypherParser#renameRole.
    def enterRenameRole(self, ctx:CypherParser.RenameRoleContext):
        pass

    # Exit a parse tree produced by CypherParser#renameRole.
    def exitRenameRole(self, ctx:CypherParser.RenameRoleContext):
        pass


    # Enter a parse tree produced by CypherParser#showRoles.
    def enterShowRoles(self, ctx:CypherParser.ShowRolesContext):
        pass

    # Exit a parse tree produced by CypherParser#showRoles.
    def exitShowRoles(self, ctx:CypherParser.ShowRolesContext):
        pass


    # Enter a parse tree produced by CypherParser#grantRole.
    def enterGrantRole(self, ctx:CypherParser.GrantRoleContext):
        pass

    # Exit a parse tree produced by CypherParser#grantRole.
    def exitGrantRole(self, ctx:CypherParser.GrantRoleContext):
        pass


    # Enter a parse tree produced by CypherParser#revokeRole.
    def enterRevokeRole(self, ctx:CypherParser.RevokeRoleContext):
        pass

    # Exit a parse tree produced by CypherParser#revokeRole.
    def exitRevokeRole(self, ctx:CypherParser.RevokeRoleContext):
        pass


    # Enter a parse tree produced by CypherParser#createUser.
    def enterCreateUser(self, ctx:CypherParser.CreateUserContext):
        pass

    # Exit a parse tree produced by CypherParser#createUser.
    def exitCreateUser(self, ctx:CypherParser.CreateUserContext):
        pass


    # Enter a parse tree produced by CypherParser#dropUser.
    def enterDropUser(self, ctx:CypherParser.DropUserContext):
        pass

    # Exit a parse tree produced by CypherParser#dropUser.
    def exitDropUser(self, ctx:CypherParser.DropUserContext):
        pass


    # Enter a parse tree produced by CypherParser#renameUser.
    def enterRenameUser(self, ctx:CypherParser.RenameUserContext):
        pass

    # Exit a parse tree produced by CypherParser#renameUser.
    def exitRenameUser(self, ctx:CypherParser.RenameUserContext):
        pass


    # Enter a parse tree produced by CypherParser#alterCurrentUser.
    def enterAlterCurrentUser(self, ctx:CypherParser.AlterCurrentUserContext):
        pass

    # Exit a parse tree produced by CypherParser#alterCurrentUser.
    def exitAlterCurrentUser(self, ctx:CypherParser.AlterCurrentUserContext):
        pass


    # Enter a parse tree produced by CypherParser#alterUser.
    def enterAlterUser(self, ctx:CypherParser.AlterUserContext):
        pass

    # Exit a parse tree produced by CypherParser#alterUser.
    def exitAlterUser(self, ctx:CypherParser.AlterUserContext):
        pass


    # Enter a parse tree produced by CypherParser#setPassword.
    def enterSetPassword(self, ctx:CypherParser.SetPasswordContext):
        pass

    # Exit a parse tree produced by CypherParser#setPassword.
    def exitSetPassword(self, ctx:CypherParser.SetPasswordContext):
        pass


    # Enter a parse tree produced by CypherParser#passwordExpression.
    def enterPasswordExpression(self, ctx:CypherParser.PasswordExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#passwordExpression.
    def exitPasswordExpression(self, ctx:CypherParser.PasswordExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#passwordChangeRequired.
    def enterPasswordChangeRequired(self, ctx:CypherParser.PasswordChangeRequiredContext):
        pass

    # Exit a parse tree produced by CypherParser#passwordChangeRequired.
    def exitPasswordChangeRequired(self, ctx:CypherParser.PasswordChangeRequiredContext):
        pass


    # Enter a parse tree produced by CypherParser#userStatus.
    def enterUserStatus(self, ctx:CypherParser.UserStatusContext):
        pass

    # Exit a parse tree produced by CypherParser#userStatus.
    def exitUserStatus(self, ctx:CypherParser.UserStatusContext):
        pass


    # Enter a parse tree produced by CypherParser#homeDatabase.
    def enterHomeDatabase(self, ctx:CypherParser.HomeDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#homeDatabase.
    def exitHomeDatabase(self, ctx:CypherParser.HomeDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#showUsers.
    def enterShowUsers(self, ctx:CypherParser.ShowUsersContext):
        pass

    # Exit a parse tree produced by CypherParser#showUsers.
    def exitShowUsers(self, ctx:CypherParser.ShowUsersContext):
        pass


    # Enter a parse tree produced by CypherParser#showCurrentUser.
    def enterShowCurrentUser(self, ctx:CypherParser.ShowCurrentUserContext):
        pass

    # Exit a parse tree produced by CypherParser#showCurrentUser.
    def exitShowCurrentUser(self, ctx:CypherParser.ShowCurrentUserContext):
        pass


    # Enter a parse tree produced by CypherParser#showSupportedPrivileges.
    def enterShowSupportedPrivileges(self, ctx:CypherParser.ShowSupportedPrivilegesContext):
        pass

    # Exit a parse tree produced by CypherParser#showSupportedPrivileges.
    def exitShowSupportedPrivileges(self, ctx:CypherParser.ShowSupportedPrivilegesContext):
        pass


    # Enter a parse tree produced by CypherParser#showPrivileges.
    def enterShowPrivileges(self, ctx:CypherParser.ShowPrivilegesContext):
        pass

    # Exit a parse tree produced by CypherParser#showPrivileges.
    def exitShowPrivileges(self, ctx:CypherParser.ShowPrivilegesContext):
        pass


    # Enter a parse tree produced by CypherParser#showRolePrivileges.
    def enterShowRolePrivileges(self, ctx:CypherParser.ShowRolePrivilegesContext):
        pass

    # Exit a parse tree produced by CypherParser#showRolePrivileges.
    def exitShowRolePrivileges(self, ctx:CypherParser.ShowRolePrivilegesContext):
        pass


    # Enter a parse tree produced by CypherParser#showUserPrivileges.
    def enterShowUserPrivileges(self, ctx:CypherParser.ShowUserPrivilegesContext):
        pass

    # Exit a parse tree produced by CypherParser#showUserPrivileges.
    def exitShowUserPrivileges(self, ctx:CypherParser.ShowUserPrivilegesContext):
        pass


    # Enter a parse tree produced by CypherParser#grantRoleManagement.
    def enterGrantRoleManagement(self, ctx:CypherParser.GrantRoleManagementContext):
        pass

    # Exit a parse tree produced by CypherParser#grantRoleManagement.
    def exitGrantRoleManagement(self, ctx:CypherParser.GrantRoleManagementContext):
        pass


    # Enter a parse tree produced by CypherParser#revokeRoleManagement.
    def enterRevokeRoleManagement(self, ctx:CypherParser.RevokeRoleManagementContext):
        pass

    # Exit a parse tree produced by CypherParser#revokeRoleManagement.
    def exitRevokeRoleManagement(self, ctx:CypherParser.RevokeRoleManagementContext):
        pass


    # Enter a parse tree produced by CypherParser#roleManagementPrivilege.
    def enterRoleManagementPrivilege(self, ctx:CypherParser.RoleManagementPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#roleManagementPrivilege.
    def exitRoleManagementPrivilege(self, ctx:CypherParser.RoleManagementPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#grantPrivilege.
    def enterGrantPrivilege(self, ctx:CypherParser.GrantPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#grantPrivilege.
    def exitGrantPrivilege(self, ctx:CypherParser.GrantPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#denyPrivilege.
    def enterDenyPrivilege(self, ctx:CypherParser.DenyPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#denyPrivilege.
    def exitDenyPrivilege(self, ctx:CypherParser.DenyPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#revokePrivilege.
    def enterRevokePrivilege(self, ctx:CypherParser.RevokePrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#revokePrivilege.
    def exitRevokePrivilege(self, ctx:CypherParser.RevokePrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#privilege.
    def enterPrivilege(self, ctx:CypherParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#privilege.
    def exitPrivilege(self, ctx:CypherParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#allPrivilege.
    def enterAllPrivilege(self, ctx:CypherParser.AllPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#allPrivilege.
    def exitAllPrivilege(self, ctx:CypherParser.AllPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#allPrivilegeType.
    def enterAllPrivilegeType(self, ctx:CypherParser.AllPrivilegeTypeContext):
        pass

    # Exit a parse tree produced by CypherParser#allPrivilegeType.
    def exitAllPrivilegeType(self, ctx:CypherParser.AllPrivilegeTypeContext):
        pass


    # Enter a parse tree produced by CypherParser#allPrivilegeTarget.
    def enterAllPrivilegeTarget(self, ctx:CypherParser.AllPrivilegeTargetContext):
        pass

    # Exit a parse tree produced by CypherParser#allPrivilegeTarget.
    def exitAllPrivilegeTarget(self, ctx:CypherParser.AllPrivilegeTargetContext):
        pass


    # Enter a parse tree produced by CypherParser#createPrivilege.
    def enterCreatePrivilege(self, ctx:CypherParser.CreatePrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#createPrivilege.
    def exitCreatePrivilege(self, ctx:CypherParser.CreatePrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#dropPrivilege.
    def enterDropPrivilege(self, ctx:CypherParser.DropPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#dropPrivilege.
    def exitDropPrivilege(self, ctx:CypherParser.DropPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#showPrivilege.
    def enterShowPrivilege(self, ctx:CypherParser.ShowPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#showPrivilege.
    def exitShowPrivilege(self, ctx:CypherParser.ShowPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#setPrivilege.
    def enterSetPrivilege(self, ctx:CypherParser.SetPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#setPrivilege.
    def exitSetPrivilege(self, ctx:CypherParser.SetPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#removePrivilege.
    def enterRemovePrivilege(self, ctx:CypherParser.RemovePrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#removePrivilege.
    def exitRemovePrivilege(self, ctx:CypherParser.RemovePrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#writePrivilege.
    def enterWritePrivilege(self, ctx:CypherParser.WritePrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#writePrivilege.
    def exitWritePrivilege(self, ctx:CypherParser.WritePrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#databasePrivilege.
    def enterDatabasePrivilege(self, ctx:CypherParser.DatabasePrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#databasePrivilege.
    def exitDatabasePrivilege(self, ctx:CypherParser.DatabasePrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#dbmsPrivilege.
    def enterDbmsPrivilege(self, ctx:CypherParser.DbmsPrivilegeContext):
        pass

    # Exit a parse tree produced by CypherParser#dbmsPrivilege.
    def exitDbmsPrivilege(self, ctx:CypherParser.DbmsPrivilegeContext):
        pass


    # Enter a parse tree produced by CypherParser#executeFunctionQualifier.
    def enterExecuteFunctionQualifier(self, ctx:CypherParser.ExecuteFunctionQualifierContext):
        pass

    # Exit a parse tree produced by CypherParser#executeFunctionQualifier.
    def exitExecuteFunctionQualifier(self, ctx:CypherParser.ExecuteFunctionQualifierContext):
        pass


    # Enter a parse tree produced by CypherParser#executeProcedureQualifier.
    def enterExecuteProcedureQualifier(self, ctx:CypherParser.ExecuteProcedureQualifierContext):
        pass

    # Exit a parse tree produced by CypherParser#executeProcedureQualifier.
    def exitExecuteProcedureQualifier(self, ctx:CypherParser.ExecuteProcedureQualifierContext):
        pass


    # Enter a parse tree produced by CypherParser#settingQualifier.
    def enterSettingQualifier(self, ctx:CypherParser.SettingQualifierContext):
        pass

    # Exit a parse tree produced by CypherParser#settingQualifier.
    def exitSettingQualifier(self, ctx:CypherParser.SettingQualifierContext):
        pass


    # Enter a parse tree produced by CypherParser#globs.
    def enterGlobs(self, ctx:CypherParser.GlobsContext):
        pass

    # Exit a parse tree produced by CypherParser#globs.
    def exitGlobs(self, ctx:CypherParser.GlobsContext):
        pass


    # Enter a parse tree produced by CypherParser#qualifiedGraphPrivilegesWithProperty.
    def enterQualifiedGraphPrivilegesWithProperty(self, ctx:CypherParser.QualifiedGraphPrivilegesWithPropertyContext):
        pass

    # Exit a parse tree produced by CypherParser#qualifiedGraphPrivilegesWithProperty.
    def exitQualifiedGraphPrivilegesWithProperty(self, ctx:CypherParser.QualifiedGraphPrivilegesWithPropertyContext):
        pass


    # Enter a parse tree produced by CypherParser#qualifiedGraphPrivileges.
    def enterQualifiedGraphPrivileges(self, ctx:CypherParser.QualifiedGraphPrivilegesContext):
        pass

    # Exit a parse tree produced by CypherParser#qualifiedGraphPrivileges.
    def exitQualifiedGraphPrivileges(self, ctx:CypherParser.QualifiedGraphPrivilegesContext):
        pass


    # Enter a parse tree produced by CypherParser#labelResource.
    def enterLabelResource(self, ctx:CypherParser.LabelResourceContext):
        pass

    # Exit a parse tree produced by CypherParser#labelResource.
    def exitLabelResource(self, ctx:CypherParser.LabelResourceContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyResource.
    def enterPropertyResource(self, ctx:CypherParser.PropertyResourceContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyResource.
    def exitPropertyResource(self, ctx:CypherParser.PropertyResourceContext):
        pass


    # Enter a parse tree produced by CypherParser#graphQualifier.
    def enterGraphQualifier(self, ctx:CypherParser.GraphQualifierContext):
        pass

    # Exit a parse tree produced by CypherParser#graphQualifier.
    def exitGraphQualifier(self, ctx:CypherParser.GraphQualifierContext):
        pass


    # Enter a parse tree produced by CypherParser#createDatabase.
    def enterCreateDatabase(self, ctx:CypherParser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#createDatabase.
    def exitCreateDatabase(self, ctx:CypherParser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#options_.
    def enterOptions_(self, ctx:CypherParser.Options_Context):
        pass

    # Exit a parse tree produced by CypherParser#options_.
    def exitOptions_(self, ctx:CypherParser.Options_Context):
        pass


    # Enter a parse tree produced by CypherParser#createCompositeDatabase.
    def enterCreateCompositeDatabase(self, ctx:CypherParser.CreateCompositeDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#createCompositeDatabase.
    def exitCreateCompositeDatabase(self, ctx:CypherParser.CreateCompositeDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#dropDatabase.
    def enterDropDatabase(self, ctx:CypherParser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#dropDatabase.
    def exitDropDatabase(self, ctx:CypherParser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#alterDatabase.
    def enterAlterDatabase(self, ctx:CypherParser.AlterDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#alterDatabase.
    def exitAlterDatabase(self, ctx:CypherParser.AlterDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#startDatabase.
    def enterStartDatabase(self, ctx:CypherParser.StartDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#startDatabase.
    def exitStartDatabase(self, ctx:CypherParser.StartDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#stopDatabase.
    def enterStopDatabase(self, ctx:CypherParser.StopDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#stopDatabase.
    def exitStopDatabase(self, ctx:CypherParser.StopDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#waitClause.
    def enterWaitClause(self, ctx:CypherParser.WaitClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#waitClause.
    def exitWaitClause(self, ctx:CypherParser.WaitClauseContext):
        pass


    # Enter a parse tree produced by CypherParser#showDatabase.
    def enterShowDatabase(self, ctx:CypherParser.ShowDatabaseContext):
        pass

    # Exit a parse tree produced by CypherParser#showDatabase.
    def exitShowDatabase(self, ctx:CypherParser.ShowDatabaseContext):
        pass


    # Enter a parse tree produced by CypherParser#databaseScopeList.
    def enterDatabaseScopeList(self, ctx:CypherParser.DatabaseScopeListContext):
        pass

    # Exit a parse tree produced by CypherParser#databaseScopeList.
    def exitDatabaseScopeList(self, ctx:CypherParser.DatabaseScopeListContext):
        pass


    # Enter a parse tree produced by CypherParser#graphScopeList.
    def enterGraphScopeList(self, ctx:CypherParser.GraphScopeListContext):
        pass

    # Exit a parse tree produced by CypherParser#graphScopeList.
    def exitGraphScopeList(self, ctx:CypherParser.GraphScopeListContext):
        pass


    # Enter a parse tree produced by CypherParser#createAlias.
    def enterCreateAlias(self, ctx:CypherParser.CreateAliasContext):
        pass

    # Exit a parse tree produced by CypherParser#createAlias.
    def exitCreateAlias(self, ctx:CypherParser.CreateAliasContext):
        pass


    # Enter a parse tree produced by CypherParser#dropAlias.
    def enterDropAlias(self, ctx:CypherParser.DropAliasContext):
        pass

    # Exit a parse tree produced by CypherParser#dropAlias.
    def exitDropAlias(self, ctx:CypherParser.DropAliasContext):
        pass


    # Enter a parse tree produced by CypherParser#alterAlias.
    def enterAlterAlias(self, ctx:CypherParser.AlterAliasContext):
        pass

    # Exit a parse tree produced by CypherParser#alterAlias.
    def exitAlterAlias(self, ctx:CypherParser.AlterAliasContext):
        pass


    # Enter a parse tree produced by CypherParser#showAliases.
    def enterShowAliases(self, ctx:CypherParser.ShowAliasesContext):
        pass

    # Exit a parse tree produced by CypherParser#showAliases.
    def exitShowAliases(self, ctx:CypherParser.ShowAliasesContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicAliasNameList.
    def enterSymbolicAliasNameList(self, ctx:CypherParser.SymbolicAliasNameListContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicAliasNameList.
    def exitSymbolicAliasNameList(self, ctx:CypherParser.SymbolicAliasNameListContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicAliasName.
    def enterSymbolicAliasName(self, ctx:CypherParser.SymbolicAliasNameContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicAliasName.
    def exitSymbolicAliasName(self, ctx:CypherParser.SymbolicAliasNameContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicNameOrStringParameterList.
    def enterSymbolicNameOrStringParameterList(self, ctx:CypherParser.SymbolicNameOrStringParameterListContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicNameOrStringParameterList.
    def exitSymbolicNameOrStringParameterList(self, ctx:CypherParser.SymbolicNameOrStringParameterListContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicNameOrStringParameter.
    def enterSymbolicNameOrStringParameter(self, ctx:CypherParser.SymbolicNameOrStringParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicNameOrStringParameter.
    def exitSymbolicNameOrStringParameter(self, ctx:CypherParser.SymbolicNameOrStringParameterContext):
        pass


    # Enter a parse tree produced by CypherParser#glob.
    def enterGlob(self, ctx:CypherParser.GlobContext):
        pass

    # Exit a parse tree produced by CypherParser#glob.
    def exitGlob(self, ctx:CypherParser.GlobContext):
        pass


    # Enter a parse tree produced by CypherParser#globRecursive.
    def enterGlobRecursive(self, ctx:CypherParser.GlobRecursiveContext):
        pass

    # Exit a parse tree produced by CypherParser#globRecursive.
    def exitGlobRecursive(self, ctx:CypherParser.GlobRecursiveContext):
        pass


    # Enter a parse tree produced by CypherParser#globPart.
    def enterGlobPart(self, ctx:CypherParser.GlobPartContext):
        pass

    # Exit a parse tree produced by CypherParser#globPart.
    def exitGlobPart(self, ctx:CypherParser.GlobPartContext):
        pass


    # Enter a parse tree produced by CypherParser#stringImage.
    def enterStringImage(self, ctx:CypherParser.StringImageContext):
        pass

    # Exit a parse tree produced by CypherParser#stringImage.
    def exitStringImage(self, ctx:CypherParser.StringImageContext):
        pass


    # Enter a parse tree produced by CypherParser#stringList.
    def enterStringList(self, ctx:CypherParser.StringListContext):
        pass

    # Exit a parse tree produced by CypherParser#stringList.
    def exitStringList(self, ctx:CypherParser.StringListContext):
        pass


    # Enter a parse tree produced by CypherParser#stringToken.
    def enterStringToken(self, ctx:CypherParser.StringTokenContext):
        pass

    # Exit a parse tree produced by CypherParser#stringToken.
    def exitStringToken(self, ctx:CypherParser.StringTokenContext):
        pass


    # Enter a parse tree produced by CypherParser#stringOrParameter.
    def enterStringOrParameter(self, ctx:CypherParser.StringOrParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#stringOrParameter.
    def exitStringOrParameter(self, ctx:CypherParser.StringOrParameterContext):
        pass


    # Enter a parse tree produced by CypherParser#mapOrParameter.
    def enterMapOrParameter(self, ctx:CypherParser.MapOrParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#mapOrParameter.
    def exitMapOrParameter(self, ctx:CypherParser.MapOrParameterContext):
        pass


    # Enter a parse tree produced by CypherParser#map.
    def enterMap(self, ctx:CypherParser.MapContext):
        pass

    # Exit a parse tree produced by CypherParser#map.
    def exitMap(self, ctx:CypherParser.MapContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicNamePositions.
    def enterSymbolicNamePositions(self, ctx:CypherParser.SymbolicNamePositionsContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicNamePositions.
    def exitSymbolicNamePositions(self, ctx:CypherParser.SymbolicNamePositionsContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicNameString.
    def enterSymbolicNameString(self, ctx:CypherParser.SymbolicNameStringContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicNameString.
    def exitSymbolicNameString(self, ctx:CypherParser.SymbolicNameStringContext):
        pass


    # Enter a parse tree produced by CypherParser#escapedSymbolicNameString.
    def enterEscapedSymbolicNameString(self, ctx:CypherParser.EscapedSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by CypherParser#escapedSymbolicNameString.
    def exitEscapedSymbolicNameString(self, ctx:CypherParser.EscapedSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by CypherParser#unescapedSymbolicNameString.
    def enterUnescapedSymbolicNameString(self, ctx:CypherParser.UnescapedSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by CypherParser#unescapedSymbolicNameString.
    def exitUnescapedSymbolicNameString(self, ctx:CypherParser.UnescapedSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by CypherParser#symbolicLabelNameString.
    def enterSymbolicLabelNameString(self, ctx:CypherParser.SymbolicLabelNameStringContext):
        pass

    # Exit a parse tree produced by CypherParser#symbolicLabelNameString.
    def exitSymbolicLabelNameString(self, ctx:CypherParser.SymbolicLabelNameStringContext):
        pass


    # Enter a parse tree produced by CypherParser#unescapedLabelSymbolicNameString.
    def enterUnescapedLabelSymbolicNameString(self, ctx:CypherParser.UnescapedLabelSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by CypherParser#unescapedLabelSymbolicNameString.
    def exitUnescapedLabelSymbolicNameString(self, ctx:CypherParser.UnescapedLabelSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by CypherParser#endOfFile.
    def enterEndOfFile(self, ctx:CypherParser.EndOfFileContext):
        pass

    # Exit a parse tree produced by CypherParser#endOfFile.
    def exitEndOfFile(self, ctx:CypherParser.EndOfFileContext):
        pass



del CypherParser