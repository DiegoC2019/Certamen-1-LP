// Generated from c://Users//diego//OneDrive//Escritorio//multicapa_bueno//CellularAutomaton.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CellularAutomatonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		BOOL=10, INT=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"BOOL", "INT", "WS"
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


	public CellularAutomatonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CellularAutomaton.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\fc\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tV\b\t\u0001\n\u0004"+
		"\nY\b\n\u000b\n\f\nZ\u0001\u000b\u0004\u000b^\b\u000b\u000b\u000b\f\u000b"+
		"_\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0001\u0000\u0002\u0001\u000009\u0003\u0000\t\n\r"+
		"\r  e\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001"+
		"\u0019\u0001\u0000\u0000\u0000\u0003 \u0001\u0000\u0000\u0000\u0005\""+
		"\u0001\u0000\u0000\u0000\u0007-\u0001\u0000\u0000\u0000\t/\u0001\u0000"+
		"\u0000\u0000\u000b1\u0001\u0000\u0000\u0000\r7\u0001\u0000\u0000\u0000"+
		"\u000f>\u0001\u0000\u0000\u0000\u0011J\u0001\u0000\u0000\u0000\u0013U"+
		"\u0001\u0000\u0000\u0000\u0015X\u0001\u0000\u0000\u0000\u0017]\u0001\u0000"+
		"\u0000\u0000\u0019\u001a\u0005C\u0000\u0000\u001a\u001b\u0005O\u0000\u0000"+
		"\u001b\u001c\u0005N\u0000\u0000\u001c\u001d\u0005F\u0000\u0000\u001d\u001e"+
		"\u0005I\u0000\u0000\u001e\u001f\u0005G\u0000\u0000\u001f\u0002\u0001\u0000"+
		"\u0000\u0000 !\u0005(\u0000\u0000!\u0004\u0001\u0000\u0000\u0000\"#\u0005"+
		"i\u0000\u0000#$\u0005n\u0000\u0000$%\u0005f\u0000\u0000%&\u0005e\u0000"+
		"\u0000&\'\u0005c\u0000\u0000\'(\u0005t\u0000\u0000()\u0005a\u0000\u0000"+
		")*\u0005d\u0000\u0000*+\u0005o\u0000\u0000+,\u0005s\u0000\u0000,\u0006"+
		"\u0001\u0000\u0000\u0000-.\u0005=\u0000\u0000.\b\u0001\u0000\u0000\u0000"+
		"/0\u0005,\u0000\u00000\n\u0001\u0000\u0000\u000012\u0005c\u0000\u0000"+
		"23\u0005a\u0000\u000034\u0005p\u0000\u000045\u0005a\u0000\u000056\u0005"+
		"s\u0000\u00006\f\u0001\u0000\u0000\u000078\u0005t\u0000\u000089\u0005"+
		"a\u0000\u00009:\u0005m\u0000\u0000:;\u0005a\u0000\u0000;<\u0005n\u0000"+
		"\u0000<=\u0005o\u0000\u0000=\u000e\u0001\u0000\u0000\u0000>?\u0005p\u0000"+
		"\u0000?@\u0005r\u0000\u0000@A\u0005o\u0000\u0000AB\u0005p\u0000\u0000"+
		"BC\u0005a\u0000\u0000CD\u0005g\u0000\u0000DE\u0005a\u0000\u0000EF\u0005"+
		"c\u0000\u0000FG\u0005i\u0000\u0000GH\u0005o\u0000\u0000HI\u0005n\u0000"+
		"\u0000I\u0010\u0001\u0000\u0000\u0000JK\u0005)\u0000\u0000K\u0012\u0001"+
		"\u0000\u0000\u0000LM\u0005T\u0000\u0000MN\u0005r\u0000\u0000NO\u0005u"+
		"\u0000\u0000OV\u0005e\u0000\u0000PQ\u0005F\u0000\u0000QR\u0005a\u0000"+
		"\u0000RS\u0005l\u0000\u0000ST\u0005s\u0000\u0000TV\u0005e\u0000\u0000"+
		"UL\u0001\u0000\u0000\u0000UP\u0001\u0000\u0000\u0000V\u0014\u0001\u0000"+
		"\u0000\u0000WY\u0007\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000YZ\u0001"+
		"\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000"+
		"[\u0016\u0001\u0000\u0000\u0000\\^\u0007\u0001\u0000\u0000]\\\u0001\u0000"+
		"\u0000\u0000^_\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001"+
		"\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000ab\u0006\u000b\u0000\u0000"+
		"b\u0018\u0001\u0000\u0000\u0000\u0004\u0000UZ_\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}