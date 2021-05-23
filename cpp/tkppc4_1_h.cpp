#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int main(){
    long long N, M, K;
    long long t[N];
    cin >> N >> M >> K;
    for (int i=2;i<N;++i) {
        cin >> t[i];
    }
    long long l[M][4];
    for (int i=0;i<M;i++) {
        for (int j=0;j<4;++j) {
            cin >> l[i][j];
        }
    }
    priority_queue<long long,vector<long long>, greater<long long>> que;
    
    return 0;
}