import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        char a = 'a';

        for (int i = 0; i < 26; i++) {
            System.out.print(S.indexOf(a) + " ");
            a ++;
        }
    }
}