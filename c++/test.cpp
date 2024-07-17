#include <iostream>
using namespace std;

 int num1, num2;
 void max(int  , int );    // declaration fun
 int main()
 {
   cout << "enter two  numbers" << endl;
   cin >> num1 ;
   cin >> num2 ;
   max(num1 , num2);     //   call fun
   return 0;

 }

 void max(int num1 , int num2){        //   defination fun
   if(num1 > num2){
      cout << "num1 is greater " <<endl;
   }
   else if(num1 < num2){
      cout << "num2 is greater" << endl;
   }
   else{
      cout << "two number is equal" << endl;
   }
 }

 