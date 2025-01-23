import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double totalScore = 0;
        double sum = 0;
        for (int i = 0; i < 20; i++) {
            String s = br.readLine();
            String[] split = s.split(" ");
            if (split[2].equals("P")) {

            }else {
                totalScore += Double.parseDouble(split[1]);
            }

            if (split[2].equals("A+")){
                sum += Double.parseDouble(split[1])*4.5;
            } else if (split[2].equals("A0")){
                sum += Double.parseDouble(split[1])*4.0;
            } else if (split[2].equals("B+")){
                sum += Double.parseDouble(split[1])*3.5;
            }else if (split[2].equals("B0")){
                sum += Double.parseDouble(split[1])*3.0;
            }else if (split[2].equals("C+")){
                sum += Double.parseDouble(split[1])*2.5;
            }else if (split[2].equals("C0")){
                sum += Double.parseDouble(split[1])*2.0;
            }else if (split[2].equals("D+")){
                sum += Double.parseDouble(split[1])*1.5;
            }else if (split[2].equals("D0")) {
                sum += Double.parseDouble(split[1])*1.0;
            } else if (split[2].equals("F")) {
                sum += Double.parseDouble(split[1]) * 0;
            }
        }
        System.out.println(sum/totalScore);
    }
}