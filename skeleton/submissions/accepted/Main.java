import java.io.*;
import java.util.*;

public class Main {

    public static final double INF = 1000000000.0;
    public static class Pair<Integer> { // custom pair (vertex, distance) that compares based on distance
        int x;
        double d;

        public Pair(int x, double d) {
            this.x = x;
            this.d = d;
        }
    }

    public static class PairWithDelays<Integer> { // custom pair (vertex, distance) that compares based on distance
        int x;
        int d;

        public PairWithDelays(int x, int d) {
            this.x = x;
            this.d = d;
        }
    }

    //Comparator anonymous class implementation
    public static Comparator<Pair> idComparator = new Comparator<Pair>(){

        @Override
        public int compare(Pair c1, Pair c2) {
            return Double.compare(c1.d, c2.d);
        }
    };

    public static boolean dijkstra(int[] targets, int n, ArrayList<ArrayList<PairWithDelays>> tree, int t, double speed) {

        PriorityQueue<Pair> pq = new PriorityQueue<>(idComparator);
        double timePerSeg = 1/speed;
        pq.add(new Pair(0, 0));
        double[] dist = new double[n];
        for (int x = 0; x < n; x++) {
            dist[x] = INF;
        }

        dist[0] = 0;
        while (!pq.isEmpty()) {
            Pair cur = pq.poll();

            if (cur.d > dist[cur.x]) continue; // ignore out-of-date pair
            for (PairWithDelays e : tree.get(cur.x)) {
                int x = cur.x;
                int y = e.x;

                if (dist[x] + timePerSeg < dist[y] && (e.d >= dist[x] + timePerSeg || e.d == -1)) {
                    dist[y] = dist[x] + timePerSeg;
                    pq.add(new Pair(y, dist[y]));
                }
            }
        }

        boolean works = true;
        for (int i = 0; i < targets.length; i++) {
            if(dist[targets[i]] > t) {
                works = false;
            }
        }
        // dist[x] now stores the weighted SP for every x
        return works;
    }

    public static double binarySearchSpeed(double l, double r, int n, ArrayList<ArrayList<PairWithDelays>> g, int[] targets, int t){
        int times = 100;
        while(times > 0) {
            double m = (l+r)/2;
            if(dijkstra(targets, n, g, t, m)) r = m;
            else l = m;
            times--;
        }

        return r;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<PairWithDelays>> g = new ArrayList<>();
        for (int k = 0; k < n; k++) {
            g.add(new ArrayList(0));
        }

        for (int j = 0; j < m; j++) {
            line = br.readLine();
            st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            int d = Integer.parseInt(st.nextToken());

            g.get(x).add(new PairWithDelays(y, d));
            g.get(y).add(new PairWithDelays(x, d));
        }

        line = br.readLine();
        st = new StringTokenizer(line);
        int k = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int[] targets = new int[k];
        line = br.readLine();
        st = new StringTokenizer(line);
        for (int i = 0; i < k; i++) {
            targets[i] = Integer.parseInt(st.nextToken())-1;
        }

        double speed = binarySearchSpeed(0, 1000000000, n, g, targets, t);
        if(dijkstra(targets, n, g, t, speed)) {
            System.out.print(speed*60);
        } else {
            System.out.print("impossible");
        }
    }
}

