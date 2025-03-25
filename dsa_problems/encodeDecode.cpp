#include <bits/stdc++.h>
using namespace std;

void caesarCipher(string msg, int shift, bool encode = true) {
    shift %= 26;
    if (!encode) shift = -shift;
    
    for (int i=0;i<msg.size();i++) {
        if (isalpha(msg[i])) { 
            char base = isupper(msg[i]) ? 'A' : 'a';
            msg[i] = (msg[i] - base + shift + 26) % 26 + base; 
        }
    }
    if(encode) cout<<"Encoded message: ";
    else cout<<"Decoded message: ";
    cout<<msg<<endl;
}

int main() {
    string msg;
    int shift;
    char choice;
    
    cout << "Enter message: ";
    getline(cin, msg);
    cout << "Enter the shift value: ";
    cin >> shift;
    cout << "Encode (E) or Decode (D)? ";
    cin >> choice;
    
    bool encode = (choice == 'E' || choice == 'e');
    caesarCipher(msg, shift, encode);
    return 0;
}
