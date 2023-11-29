# Generated from .//CellularAutomaton.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CellularAutomatonParser import CellularAutomatonParser
else:
    from CellularAutomatonParser import CellularAutomatonParser

# This class defines a complete generic visitor for a parse tree produced by CellularAutomatonParser.

class CellularAutomatonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CellularAutomatonParser#prog.
    def visitProg(self, ctx:CellularAutomatonParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#instruccion.
    def visitInstruccion(self, ctx:CellularAutomatonParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#configuration.
    def visitConfiguration(self, ctx:CellularAutomatonParser.ConfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#infectados.
    def visitInfectados(self, ctx:CellularAutomatonParser.InfectadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#capas.
    def visitCapas(self, ctx:CellularAutomatonParser.CapasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#tamano.
    def visitTamano(self, ctx:CellularAutomatonParser.TamanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CellularAutomatonParser#propagacion.
    def visitPropagacion(self, ctx:CellularAutomatonParser.PropagacionContext):
        return self.visitChildren(ctx)



del CellularAutomatonParser