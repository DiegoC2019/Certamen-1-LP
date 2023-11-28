// Generated from c://Users//diego//OneDrive//Documentos//GitHub//Certamen-1-LP//CellularAutomaton.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CellularAutomatonParser}.
 */
public interface CellularAutomatonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CellularAutomatonParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CellularAutomatonParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(CellularAutomatonParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(CellularAutomatonParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#configuration}.
	 * @param ctx the parse tree
	 */
	void enterConfiguration(CellularAutomatonParser.ConfigurationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#configuration}.
	 * @param ctx the parse tree
	 */
	void exitConfiguration(CellularAutomatonParser.ConfigurationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#infectados}.
	 * @param ctx the parse tree
	 */
	void enterInfectados(CellularAutomatonParser.InfectadosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#infectados}.
	 * @param ctx the parse tree
	 */
	void exitInfectados(CellularAutomatonParser.InfectadosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#capas}.
	 * @param ctx the parse tree
	 */
	void enterCapas(CellularAutomatonParser.CapasContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#capas}.
	 * @param ctx the parse tree
	 */
	void exitCapas(CellularAutomatonParser.CapasContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#tamano}.
	 * @param ctx the parse tree
	 */
	void enterTamano(CellularAutomatonParser.TamanoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#tamano}.
	 * @param ctx the parse tree
	 */
	void exitTamano(CellularAutomatonParser.TamanoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CellularAutomatonParser#propagacion}.
	 * @param ctx the parse tree
	 */
	void enterPropagacion(CellularAutomatonParser.PropagacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CellularAutomatonParser#propagacion}.
	 * @param ctx the parse tree
	 */
	void exitPropagacion(CellularAutomatonParser.PropagacionContext ctx);
}