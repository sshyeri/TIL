# #include <iostream>
# using namespace std;
#
# int main(){
#     int t, a, b, c;
#     cin>>t;
#     if (t%10) cout<<-1;
#     else{
#         a = t/300;
#         t %= 300;
#         b = t/60;
#         t %= 60;
#         c = t/10;
#         cout<<a<<" "<<b<<" "<<c;
#     }
#     return 0;
# }
T = int(input())
if T%10: print(-1)
else:
    A = T//300
    T%=300
    B = T//60
    T%=60
    C = T//10
    T%=10
    print(A, B, C)