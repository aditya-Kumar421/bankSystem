#include <bits/stdc++.h>
using namespace std;

void mergeLists(vector<vector<int>> &list1, vector<vector<int>> &list2) {
    vector<vector<int>> mergedList = list1;
    mergedList.insert(mergedList.end(), list2.begin(), list2.end());
    
    sort(mergedList.begin(), mergedList.end(), [](const vector<int> &a, const vector<int> &b) {
        return a[0] < b[0];
    });
    
    vector<vector<int>> result;
    for (auto &elem : mergedList) {
        if (!result.empty()) {
            auto &last = result.back();
            int leftA = last[0], rightA = last[1];
            int leftB = elem[0], rightB = elem[1];
            
            int overlap = min(rightA, rightB) - max(leftA, leftB);
            int lengthA = rightA - leftA;
            int lengthB = rightB - leftB;
            
            if (overlap > lengthA / 2 || overlap > lengthB / 2) {
                last.insert(last.end(), elem.begin() + 2, elem.end());
                continue;
            }
        }
        result.push_back(elem);
    }

    for (auto &elem : result) {
        cout << "{ Positions: [" << elem[0] << ", " << elem[1] << "], Values: [";
        for (size_t i = 2; i < elem.size(); i++) {
            cout << elem[i] << (i < elem.size() - 1 ? ", " : "");
        }
        cout << "] }\n";
    }
}

int main() {
    int n, m;
    cout << "Enter number of elements in first list: ";
    cin >> n;
    vector<vector<int>> list1(n);
    cout << "Enter elements (left_position right_position followed by values):\n";
    for (int i = 0; i < n; i++) {
        int left, right, valueCount;
        cin >> left >> right >> valueCount;
        list1[i] = {left, right};
        for (int j = 0; j < valueCount; j++) {
            int val;
            cin >> val;
            list1[i].push_back(val);
        }
    }
    
    cout << "Enter number of elements in second list: ";
    cin >> m;
    vector<vector<int>> list2(m);
    cout << "Enter elements (left_position right_position followed by values):\n";
    for (int i = 0; i < m; i++) {
        int left, right, valueCount;
        cin >> left >> right >> valueCount;
        list2[i] = {left, right};
        for (int j = 0; j < valueCount; j++) {
            int val;
            cin >> val;
            list2[i].push_back(val);
        }
    }
    
    cout << "Merged List:\n";
    mergeLists(list1, list2);
    return 0;
}
