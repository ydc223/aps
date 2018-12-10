import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class TLE_WA {
    public static final int INF_INT = 2000000000;
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
        int y;
        int d;

        public PairWithDelays(int x, int y, int d) {
            this.x = x;
            this.y = y;
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

    public static int dijkstra(int[] targets, int n, ArrayList<ArrayList<PairWithDelays>> tree, int t) {

        PriorityQueue<Pair> pq = new PriorityQueue<>(idComparator);
        pq.add(new Pair(0, 0));
        int[] dist = new int[n];
        for (int x = 0; x < n; x++) {
            dist[x] = INF_INT;
        }

        dist[0] = 0;
        while (!pq.isEmpty()) {
            Pair cur = pq.poll();

            if (cur.d > dist[cur.x]) continue; // ignore out-of-date pair
            for (PairWithDelays e : tree.get(cur.x)) {
                int x = cur.x;
                int y = e.x;

                if (dist[x] + 1 < dist[y]) {
                    dist[y] = dist[x] + 1;
                    pq.add(new Pair(y, dist[y]));
                }
            }
        }

        int max = 0;
        for (int i = 0; i < targets.length; i++) {
            if(dist[targets[i]] == INF_INT) {
                max = -1;
                break;
            }
            if(dist[targets[i]] > max){
                max = dist[targets[i]];
            }
        }
        // dist[x] now stores the weighted SP for every x
        return max;
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
        ArrayList<PairWithDelays> edges = new ArrayList<>();

        for (int j = 0; j < m; j++) {
            line = br.readLine();
            st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            int d = Integer.parseInt(st.nextToken());
            if(d == -1){
                d = INF_INT;
            }

            edges.add(new PairWithDelays(x, y, d));
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

        Collections.sort(edges, (o1, o2) -> -Integer.compare(o1.d, o2.d));

        int prev = edges.get(0).d;
        PairWithDelays edge = edges.get(0);
        int i = 0;
        boolean finished = false;

        while (i < edges.size()) {
            while(i < edges.size() && edge.d == prev) {
                g.get(edge.x).add(new PairWithDelays(edge.y, edge.x, edge.d));
                g.get(edge.y).add(new PairWithDelays(edge.x, edge.y, edge.d));
                prev = edge.d;
                i++;
                if(i < edges.size())
                    edge = edges.get(i);
            }

            int resD = dijkstra(targets, n, g, t);
            if(resD != -1) {
                int delay = prev;
                if(delay == INF_INT) delay = t;
                double ans = (double)resD/delay*60;
                System.out.println(ans);
                finished = true;
                break;
            }
            if(i< edges.size())
                prev = edges.get(i).d;
        }
        if(!finished){
            System.out.print("impossible");
        }
    }
}
