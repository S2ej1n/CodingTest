import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] croatia = {"c=","c-","dz=","d-","lj","nj","s=","z="};

        String input = br.readLine();

        for (int i = 0; i < croatia.length; i++) {
            if (input.contains(croatia[i])){
                input = input.replace(croatia[i], "H");
            }
        }
        System.out.println(input.length());
    }
}