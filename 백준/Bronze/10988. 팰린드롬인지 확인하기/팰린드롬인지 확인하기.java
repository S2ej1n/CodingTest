import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        StringBuilder sb = new StringBuilder(word);

        int r = word.equals(sb.reverse().toString())? 1 : 0;
        System.out.println(r);
    }
}