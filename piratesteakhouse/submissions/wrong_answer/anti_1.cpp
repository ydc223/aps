#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 100005
#define MAXM 200005
#define INF 1000000005

/*
 * This is a wrong answer solution. It will get wrong answer because it calculates the shortest past only once
 * and ignores the fact that certain paths get cut off over time.
 */

long long dist[MAXN];
struct Pair {
    int x;
    long long d;
    Pair(int _x, long long _d): x(_x), d(_d) {}
    bool operator < (const Pair &another) const { return d > another.d; }
};

void dijkstra(int s, vector<pair<int, int>> graph[MAXN]) {
    priority_queue<Pair> pq;
    pq.push(Pair(s, 0));
    for (int x = 0; x < MAXN; x++) dist[x] = INF;
    dist[s] = 0;
    while (!pq.empty()) {
        Pair cur = pq.top();
        pq.pop();
        if (cur.d > dist[cur.x]) continue;
        for (auto e: graph[cur.x]) {
            if ((long long) dist[cur.x] + 1 < dist[e.first]) {
                dist[e.first] = (long long) dist[cur.x] + 1;
                pq.push(Pair(e.first, dist[e.first]));
            }
        }
    }
}

void pirate(){
    int n, m, k, t;
    cin >> n >> m;
    vector<pair<int, int>> graph[MAXN];
    vector<int> delivery_locations;
    for (int i = 0; i < m; ++i) {
        int n1, n2, d;
        cin >> n1 >> n2 >> d;
        graph[n1].emplace_back(n2, d);
        graph[n2].emplace_back(n1, d);
    }

    cin >> k >> t;
    for (int j = 0; j < k; ++j) {
        int l;
        cin >> l;
        delivery_locations.push_back(l);
    }

    dijkstra(1, graph);
    long long furthest_deliv_dist = 0;
    for (int i = 0; i < k; ++i) {
        if(dist[delivery_locations[i]] > furthest_deliv_dist) furthest_deliv_dist = dist[delivery_locations[i]];
    }

    double min_speed = ((double)furthest_deliv_dist/t)*60;
    cout << min_speed;
}

int main() {
    //freopen("in.txt", "r", stdin);
    pirate();
    return 0;
}