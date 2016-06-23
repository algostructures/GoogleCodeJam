import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static PrintWriter pw;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new FileReader("C:/Users/Saurabh/Desktop/CodeJamIN/Asm.in"));
		pw = new PrintWriter(new BufferedWriter(new FileWriter("C:/Users/Saurabh/Desktop/CodeJamOut/Asm.out")));
		final int MAX_CASES = readInt();
		for(int casenum = 1; casenum <= MAX_CASES; casenum++) {
			pw.printf("Case #%d: ", casenum);
			String s[] = readLine().split("\\s+");
			for(int i = s.length-1; i >= 0; i--){
				pw.print(s[i]+" ");
			}
			pw.println();
		}
		pw.close();
	}

	public static int readInt() {
		return Integer.parseInt(nextToken());
	}

	public static long readLong() {
		return Long.parseLong(nextToken());
	}

	public static double readDouble() {
		return Double.parseDouble(nextToken());
	}

	public static String nextToken() {
		while(st == null || !st.hasMoreTokens())	{
			try {
				if(!br.ready())	{
					pw.close();
					System.exit(0);
				}
				st = new StringTokenizer(br.readLine());
			}
			catch(IOException e) {
				System.err.println(e);
				System.exit(1);
			}
		}
		return st.nextToken();
	}

	public static String readLine()	{
		st = null;
		try {
			return br.readLine();
		}
		catch(IOException e) {
			System.err.println(e);
			System.exit(1);
			return null;
		}
	}

}


