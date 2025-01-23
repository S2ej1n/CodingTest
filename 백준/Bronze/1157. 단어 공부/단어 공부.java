import java.io.*;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String upWord = br.readLine().toUpperCase();
        char[] upWordArray = upWord.toCharArray();

        int c = 0;
        Set<Character> set = new HashSet<>();
        for (Character word : upWordArray) {
            set.add(word);
        }
        Character[] set2Array = set.toArray(new Character[set.size()]);

        int[] counts = new int[set.size()];
        for ( int i = 0; i < set.size(); i++ ) {
            for ( int j = 0; j < upWordArray.length; j++ ) {
                if (upWordArray[j] == set2Array[i]) {
                    counts[i] += 1;
                }
            }
        }

        int max = Integer.MIN_VALUE;
        int index = 0;
        boolean doublemax = false;
        for ( int i = 0; i < counts.length; i++ ) {
            if ( counts[i] > max ) {
                max = counts[i];
                index = i;
                doublemax = false;
            } else if ( counts[i] == max ) {
                doublemax = true;
            }
        }

        if ( doublemax ) {
            System.out.println("?");
        } else {
            System.out.println(set2Array[index]);
        }
    }
}