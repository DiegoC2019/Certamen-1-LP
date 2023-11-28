// Generated from c://Users//diego//OneDrive//Documentos//GitHub//Certamen-1-LP//CellularAutomaton.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CellularAutomatonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		BOOL=10, INT=11, WS=12;
	public static final int
		RULE_prog = 0, RULE_instruccion = 1, RULE_configuration = 2, RULE_infectados = 3, 
		RULE_capas = 4, RULE_tamano = 5, RULE_propagacion = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "instruccion", "configuration", "infectados", "capas", "tamano", 
			"propagacion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'CONFIG'", "'('", "'infectados'", "'='", "','", "'capas'", "'tamano'", 
			"'propagacion'", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "BOOL", "INT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CellularAutomaton.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CellularAutomatonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public ConfigurationContext configuration() {
			return getRuleContext(ConfigurationContext.class,0);
		}
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruccion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			configuration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConfigurationContext extends ParserRuleContext {
		public InfectadosContext infectados() {
			return getRuleContext(InfectadosContext.class,0);
		}
		public CapasContext capas() {
			return getRuleContext(CapasContext.class,0);
		}
		public TamanoContext tamano() {
			return getRuleContext(TamanoContext.class,0);
		}
		public PropagacionContext propagacion() {
			return getRuleContext(PropagacionContext.class,0);
		}
		public ConfigurationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configuration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterConfiguration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitConfiguration(this);
		}
	}

	public final ConfigurationContext configuration() throws RecognitionException {
		ConfigurationContext _localctx = new ConfigurationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_configuration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(T__0);
			setState(19);
			match(T__1);
			setState(20);
			match(T__2);
			setState(21);
			match(T__3);
			setState(22);
			infectados();
			setState(23);
			match(T__4);
			setState(24);
			match(T__5);
			setState(25);
			match(T__3);
			setState(26);
			capas();
			setState(27);
			match(T__4);
			setState(28);
			match(T__6);
			setState(29);
			match(T__3);
			setState(30);
			tamano();
			setState(31);
			match(T__4);
			setState(32);
			match(T__7);
			setState(33);
			match(T__3);
			setState(34);
			propagacion();
			setState(35);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InfectadosContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CellularAutomatonParser.INT, 0); }
		public InfectadosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_infectados; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterInfectados(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitInfectados(this);
		}
	}

	public final InfectadosContext infectados() throws RecognitionException {
		InfectadosContext _localctx = new InfectadosContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_infectados);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CapasContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CellularAutomatonParser.INT, 0); }
		public CapasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_capas; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterCapas(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitCapas(this);
		}
	}

	public final CapasContext capas() throws RecognitionException {
		CapasContext _localctx = new CapasContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_capas);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TamanoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CellularAutomatonParser.INT, 0); }
		public TamanoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tamano; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterTamano(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitTamano(this);
		}
	}

	public final TamanoContext tamano() throws RecognitionException {
		TamanoContext _localctx = new TamanoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tamano);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PropagacionContext extends ParserRuleContext {
		public TerminalNode BOOL() { return getToken(CellularAutomatonParser.BOOL, 0); }
		public PropagacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propagacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).enterPropagacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CellularAutomatonListener ) ((CellularAutomatonListener)listener).exitPropagacion(this);
		}
	}

	public final PropagacionContext propagacion() throws RecognitionException {
		PropagacionContext _localctx = new PropagacionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_propagacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(BOOL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\f.\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0000"+
		"\u0000\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000\u0000&\u0000\u000e\u0001"+
		"\u0000\u0000\u0000\u0002\u0010\u0001\u0000\u0000\u0000\u0004\u0012\u0001"+
		"\u0000\u0000\u0000\u0006%\u0001\u0000\u0000\u0000\b\'\u0001\u0000\u0000"+
		"\u0000\n)\u0001\u0000\u0000\u0000\f+\u0001\u0000\u0000\u0000\u000e\u000f"+
		"\u0003\u0002\u0001\u0000\u000f\u0001\u0001\u0000\u0000\u0000\u0010\u0011"+
		"\u0003\u0004\u0002\u0000\u0011\u0003\u0001\u0000\u0000\u0000\u0012\u0013"+
		"\u0005\u0001\u0000\u0000\u0013\u0014\u0005\u0002\u0000\u0000\u0014\u0015"+
		"\u0005\u0003\u0000\u0000\u0015\u0016\u0005\u0004\u0000\u0000\u0016\u0017"+
		"\u0003\u0006\u0003\u0000\u0017\u0018\u0005\u0005\u0000\u0000\u0018\u0019"+
		"\u0005\u0006\u0000\u0000\u0019\u001a\u0005\u0004\u0000\u0000\u001a\u001b"+
		"\u0003\b\u0004\u0000\u001b\u001c\u0005\u0005\u0000\u0000\u001c\u001d\u0005"+
		"\u0007\u0000\u0000\u001d\u001e\u0005\u0004\u0000\u0000\u001e\u001f\u0003"+
		"\n\u0005\u0000\u001f \u0005\u0005\u0000\u0000 !\u0005\b\u0000\u0000!\""+
		"\u0005\u0004\u0000\u0000\"#\u0003\f\u0006\u0000#$\u0005\t\u0000\u0000"+
		"$\u0005\u0001\u0000\u0000\u0000%&\u0005\u000b\u0000\u0000&\u0007\u0001"+
		"\u0000\u0000\u0000\'(\u0005\u000b\u0000\u0000(\t\u0001\u0000\u0000\u0000"+
		")*\u0005\u000b\u0000\u0000*\u000b\u0001\u0000\u0000\u0000+,\u0005\n\u0000"+
		"\u0000,\r\u0001\u0000\u0000\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}