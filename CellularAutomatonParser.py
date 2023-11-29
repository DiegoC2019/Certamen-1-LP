# Generated from .//CellularAutomaton.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,
        6,0,0,7,0,2,4,6,8,10,12,0,0,38,0,14,1,0,0,0,2,16,1,0,0,0,4,18,1,
        0,0,0,6,37,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,0,12,43,1,0,0,0,14,15,
        3,2,1,0,15,1,1,0,0,0,16,17,3,4,2,0,17,3,1,0,0,0,18,19,5,1,0,0,19,
        20,5,2,0,0,20,21,5,3,0,0,21,22,5,4,0,0,22,23,3,6,3,0,23,24,5,5,0,
        0,24,25,5,6,0,0,25,26,5,4,0,0,26,27,3,8,4,0,27,28,5,5,0,0,28,29,
        5,7,0,0,29,30,5,4,0,0,30,31,3,10,5,0,31,32,5,5,0,0,32,33,5,8,0,0,
        33,34,5,4,0,0,34,35,3,12,6,0,35,36,5,9,0,0,36,5,1,0,0,0,37,38,5,
        11,0,0,38,7,1,0,0,0,39,40,5,11,0,0,40,9,1,0,0,0,41,42,5,11,0,0,42,
        11,1,0,0,0,43,44,5,10,0,0,44,13,1,0,0,0,0
    ]

class CellularAutomatonParser ( Parser ):

    grammarFileName = "CellularAutomaton.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CONFIG'", "'('", "'infectados'", "'='", 
                     "','", "'capas'", "'tamano'", "'propagacion'", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "INT", "WS" ]

    RULE_prog = 0
    RULE_instruccion = 1
    RULE_configuration = 2
    RULE_infectados = 3
    RULE_capas = 4
    RULE_tamano = 5
    RULE_propagacion = 6

    ruleNames =  [ "prog", "instruccion", "configuration", "infectados", 
                   "capas", "tamano", "propagacion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    BOOL=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(CellularAutomatonParser.InstruccionContext,0)


        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CellularAutomatonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def configuration(self):
            return self.getTypedRuleContext(CellularAutomatonParser.ConfigurationContext,0)


        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_instruccion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = CellularAutomatonParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.configuration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def infectados(self):
            return self.getTypedRuleContext(CellularAutomatonParser.InfectadosContext,0)


        def capas(self):
            return self.getTypedRuleContext(CellularAutomatonParser.CapasContext,0)


        def tamano(self):
            return self.getTypedRuleContext(CellularAutomatonParser.TamanoContext,0)


        def propagacion(self):
            return self.getTypedRuleContext(CellularAutomatonParser.PropagacionContext,0)


        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_configuration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfiguration" ):
                return visitor.visitConfiguration(self)
            else:
                return visitor.visitChildren(self)




    def configuration(self):

        localctx = CellularAutomatonParser.ConfigurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_configuration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(CellularAutomatonParser.T__0)
            self.state = 19
            self.match(CellularAutomatonParser.T__1)
            self.state = 20
            self.match(CellularAutomatonParser.T__2)
            self.state = 21
            self.match(CellularAutomatonParser.T__3)
            self.state = 22
            self.infectados()
            self.state = 23
            self.match(CellularAutomatonParser.T__4)
            self.state = 24
            self.match(CellularAutomatonParser.T__5)
            self.state = 25
            self.match(CellularAutomatonParser.T__3)
            self.state = 26
            self.capas()
            self.state = 27
            self.match(CellularAutomatonParser.T__4)
            self.state = 28
            self.match(CellularAutomatonParser.T__6)
            self.state = 29
            self.match(CellularAutomatonParser.T__3)
            self.state = 30
            self.tamano()
            self.state = 31
            self.match(CellularAutomatonParser.T__4)
            self.state = 32
            self.match(CellularAutomatonParser.T__7)
            self.state = 33
            self.match(CellularAutomatonParser.T__3)
            self.state = 34
            self.propagacion()
            self.state = 35
            self.match(CellularAutomatonParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InfectadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CellularAutomatonParser.INT, 0)

        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_infectados

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfectados" ):
                return visitor.visitInfectados(self)
            else:
                return visitor.visitChildren(self)




    def infectados(self):

        localctx = CellularAutomatonParser.InfectadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_infectados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CellularAutomatonParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CellularAutomatonParser.INT, 0)

        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_capas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapas" ):
                return visitor.visitCapas(self)
            else:
                return visitor.visitChildren(self)




    def capas(self):

        localctx = CellularAutomatonParser.CapasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_capas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CellularAutomatonParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TamanoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CellularAutomatonParser.INT, 0)

        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_tamano

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTamano" ):
                return visitor.visitTamano(self)
            else:
                return visitor.visitChildren(self)




    def tamano(self):

        localctx = CellularAutomatonParser.TamanoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tamano)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(CellularAutomatonParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropagacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(CellularAutomatonParser.BOOL, 0)

        def getRuleIndex(self):
            return CellularAutomatonParser.RULE_propagacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropagacion" ):
                return visitor.visitPropagacion(self)
            else:
                return visitor.visitChildren(self)




    def propagacion(self):

        localctx = CellularAutomatonParser.PropagacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_propagacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(CellularAutomatonParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





