
import java.io.*;
import java.util.*;

public class Validator {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<HashSet<Integer>> g = new ArrayList<>();
        for (int k = 0; k < n; k++) {
            g.add(new HashSet(0));
        }

        for (int j = 0; j < m; j++) {
            line = br.readLine();
            st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            int d = Integer.parseInt(st.nextToken());

            if(g.get(x).contains(y)){
                System.exit(1);
            }
            g.get(x).add(y);
            g.get(y).add(x);
        }

        System.exit(42);
    }
}
