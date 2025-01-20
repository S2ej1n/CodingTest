import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        String[] alphaNum = {"","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ",""};
        int sum = 0;
        for (int i = 0; i < input.length(); i++) {
            String c = String.valueOf(input.charAt(i));
            for (int j = 0; j < alphaNum.length; j++) {
                if (alphaNum[j].contains(c)) {
                    sum += j+2;
                }
            }
        }
        System.out.println(sum);
    }
}