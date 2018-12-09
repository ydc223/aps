//
// Created by Robert Gordon on 12/8/18.
//

#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <queue> //priority_queue
#include <string>
#include <stack>
#include <utility> //move, pair
#include <vector>

using namespace std;

#define rep(i,s,t) for(int i=s;i<t;i++)
#define for_in(el, collection) for(auto el : collection)
#define INF (int) 2e9-1
#define MAXN (int) 1e5+10

struct Triple{
    int x, delay, dist;
    Triple(int _x, int _del, int _dist) : x(_x), delay(_del), dist(_dist) {}
    bool operator<(const Triple &other) const { return dist > other.dist; }
};

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef vector<ll> vll;

typedef vector<Triple> vT;
typedef vector<vT> vvT;

int dist[MAXN];
vi delivery_locations;
vvT edges;

bool dijkstra(int s, double speed, int T){
    priority_queue<Triple> pq;

    int n = (int) edges.size();
    fill_n(dist, n, INF);
    dist[s] = 0;
    pq.emplace(s, 0, 0);

    while(!pq.empty()){
        Triple curr = pq.top();
        pq.pop();

        if(curr.dist > dist[curr.x]) continue;

        int x = curr.x;
        for_in(neighbor, edges[x]) {
            double curr_time = (dist[x]+1)/speed;
            if(dist[x]+1 < dist[neighbor.x] && neighbor.delay >= curr_time) {
                dist[neighbor.x] = dist[x]+1;
                pq.emplace(neighbor.x, neighbor.delay, dist[neighbor.x]);
            }
        }
    }

    for_in(loc, delivery_locations){
        if (dist[loc] >= INF || dist[loc]/speed > T) return false;
    }
    return true;
}

double get_speed(double l, double r, int t){
    double eps = 1e-6;
    while(r-l > eps){
        double mid = (l+r)/2;
        if(dijkstra(0, mid, t)) r = mid;
        else l = mid;
    }
    return r;
}

void binary_solution() {
    int n, m, k, t;
    scanf("%d%d\n", &n, &m);

    edges = vvT(n);

    rep(i, 0, m) {
        int x, y, d;
        scanf("%d%d%d\n", &x, &y, &d);
        edges[x - 1].emplace_back(y - 1, d == -1 ? INF : d, INF);
        edges[y - 1].emplace_back(x - 1, d == -1 ? INF : d, INF);
    }

    scanf("%d%d\n", &k, &t);

    delivery_locations = vi(k);
    rep(i, 0, k) {
        scanf("%d ", &delivery_locations[i]);
        delivery_locations[i]--;
    }

    double s = get_speed(0,1e9,t);
    if(dijkstra(0,s,t)) printf("%.6f\n", s*60);
    else printf("impossible\n");
}

int main(){
    binary_solution();
    return 0;
}
