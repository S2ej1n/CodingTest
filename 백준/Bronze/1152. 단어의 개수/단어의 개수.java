import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine().trim();

        if (S.isEmpty()){
            System.out.println(0);
        }
        else {
            String[] strAry = S.split(" ");

            System.out.println(strAry.length);
        }
    }
}