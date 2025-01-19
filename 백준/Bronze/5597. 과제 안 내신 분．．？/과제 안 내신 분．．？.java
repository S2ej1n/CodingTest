import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] student = new int[30];

        for (int n = 0; n < 28; n++){
            int k = Integer.parseInt(br.readLine());
            student[k-1] = k;
        }
       
        for (int n = 0; n < 30; n++){
            if (student[n] == 0){
                System.out.println(n+1);
            }
        }
    }
}