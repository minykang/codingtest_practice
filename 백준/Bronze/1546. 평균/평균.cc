#include <iostream>
using namespace std;

int main(){
   int n;
   cin >> n;
   double a[n];
   for(int i =0; i<n; i++){
      
      cin >>a[i];
      
   }
   int max = 0;
   double avg = 0;
   for(int i = 0; i < n; i++){
      if(a[i] > max)
      max = a[i];
      
      
   }
   for(int i = 0; i < n; i++){
   avg +=((a[i]/max)*100);
   }
   cout << avg/n;
   
   
   
   
   

}