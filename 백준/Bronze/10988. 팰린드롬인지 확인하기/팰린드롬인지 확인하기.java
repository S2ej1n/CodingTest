import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        StringBuilder sb = new StringBuilder(word);

        if (word.equals(sb.reverse().toString())){
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}