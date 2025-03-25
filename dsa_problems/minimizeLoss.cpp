#include <bits/stdc++.h>
using namespace std;

void cntLoss(vector<int> &price) {
    int minLoss = INT_MAX;
    int buyYear = -1, sellYear = -1;
    int n = price.size();
    
    for (int buy = 0; buy < n - 1; buy++) {
        for (int sell = buy + 1; sell < n; sell++) {
            if (price[sell] < price[buy]) {
                int loss = price[buy] - price[sell];
                if (loss < minLoss) {
                    minLoss = loss;
                    buyYear = buy + 1;
                    sellYear = sell + 1;
                }
            }
        }
    }
    
    if (buyYear == -1) {
        cout << "No valid loss found" << endl;
    } else {
        cout << "Buy in year " << buyYear << " and sell in year " << sellYear << " with a loss of " << minLoss << endl;
    }
}

int main() {
    int n; 
    cout << "Enter total number of year: "; 
    cin >> n; 
    
    vector<int> price(n); 
    cout << "Enter price: "; 
    for (int i = 0; i < n; i++) {
         cin >> price[i]; 
    }
    cntLoss(price); 
    return 0;
}
