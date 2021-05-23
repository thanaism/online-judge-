#include <iostream>
using namespace std;

long long N,L,K;
long long A[110000];

bool ok(long long x) {
    long long cnt = 0, pre = 0;
    for (int i=0;i<N;++i) {
        if (A[i]-pre >= x && L-A[i] >=x) {
            cnt++;
            pre = A[i];
        }
    }
    if (cnt >= K) return true;
    else return false;
}

int main() {
    cin >> N >> L >> K;
    for (int i=0;i<N;++i){
        cin >> A[i];
    }

    long long left = -1;
    long long right = L+1;
    while (abs(left-right)>1) {
        long long mid = (left + right)/2;
        if (ok(mid)) left = mid;
        else right = mid;
    }
    cout << left << endl;
    return 0;
}