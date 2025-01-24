import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] charArray = new char[5][15];

        StringBuilder result = new StringBuilder();

        // 배열에 할당
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < 5; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length() ; j++) {
                charArray[i][j] = line.charAt(j);
            }
            for (int j = line.length(); j < 15; j++) {
                charArray[i][j] = ' ';
            }
        }

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (charArray[j][i] != ' ') {
                    System.out.print(charArray[j][i]);
                }
            }
        }
    }
}