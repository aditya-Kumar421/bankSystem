#include <bits/stdc++.h>
using namespace std;

int main(){
    double n;
    cout<<"Enter the amount in dollars: ";
    cin>>n;

    string str = to_string(n);
    bool isDecimal = false;
    string lastPart = "";
    string firstPart = "";


    for(int i=0;i<str.size();i++){
        if(str[i] == '.' || isDecimal){
            lastPart += str[i];
            isDecimal = true;
        }
        else{
            firstPart += str[i];
        }
    }

    if(firstPart.size() > 3){
        reverse(firstPart.begin(), firstPart.end());
        string temp = "";
        for(int i=0;i<firstPart.size();i++){
            temp += firstPart[i];
            if(i%2 == 0 && i != 0 && i != firstPart.size()-1){
                temp += ',';
            }
        }
        reverse(temp.begin(), temp.end());
        firstPart = temp;
    }

    firstPart += lastPart;
    cout<<"Amount in Indian currency: Rs. "<<firstPart<<endl;
    return 0;
}