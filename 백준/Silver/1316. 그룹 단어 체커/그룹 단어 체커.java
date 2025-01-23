import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int count = 0;
        outer:
        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            boolean isGroup = true;

            // 문자열만큼 반복
            for (int j = 0; j < input.length(); j++) {
                char ch = input.charAt(j);
                String newInput = input.substring(j+1, input.length());

                if (newInput.indexOf(ch) > 0) { //그룹이 아닌지 확인
                    isGroup = false;
                    continue outer;
                }
            }

            if (isGroup) {
                count++;
            }
        }
        System.out.println(count);
    }
}