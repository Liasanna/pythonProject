import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Solution {

    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
             FileReader fileReader = new FileReader(reader.readLine());
             BufferedReader secondReader = new BufferedReader(fileReader)) {
            List<Integer> list = new ArrayList<>();
            String line;
            while ((line = secondReader.readLine()) != null) {
                int x = Integer.parseInt(line);
                if ((x % 2) == 0) {
                    list.add(x);
                }
            }
            Collections.sort(list);
            for (int x : list) {
                System.out.println(x);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
}