import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] matrix = new int[9][9];
        int max = Integer.MIN_VALUE;
        String index = "";

        for (int i = 0; i < 9; i ++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            outer:
            for (int j = 0; j < 9; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if(matrix[i][j] == 99){
                    max = 99;
                    index = (i+1) + " " + (j+1);
                    break outer;
                } else if(matrix[i][j] > max){
                    max = matrix[i][j];
                    index = (i+1) + " " + (j+1);
                }
            }
        }
        System.out.println(max);
        System.out.println(index);
    }
}