import java.io.*;
import minipython.lexer.Lexer;
import minipython.parser.Parser;
import minipython.node.Start;

public class ParserTest {
	public static void main(String[] args)	{
		try {
			Parser parser = new Parser(new Lexer(
					new PushbackReader(new FileReader(args[0]), 1024)));
				
			Start ast = parser.parse();
			ast.apply(new ASTPrinter());
			
			//System.out.println(ast);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
