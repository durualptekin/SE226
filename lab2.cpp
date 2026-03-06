#include <iostream>
using namespace std;

int main(){

    // ---Task 1 (Digital Root Sequence)---

    int value;
    cout << "Please enter a positive integer greater than 9: ";
    cin >> value;

    while (value <= 9 ) {
        cout<< "Please enter a positive integer greater than 9: ";
        cin >> value;

    }

    int stepCount = 0;
    cout << value;

    while (value>9) {
         
        int temp = value;
        int sum =0;

        while (temp>0) {
            sum = sum + temp%10;
            temp =temp/10;

        }
        
        value = sum;
        stepCount = stepCount+1;

        cout<< " -> " << value;

    }
    

    cout<< endl;
    cout<< "Final value: " << value << endl;
    cout<< "Total steps: " << stepCount << endl;
    
    
    
    // ---Task 2 (FizzBuzz Counter)---
    
    int n;
    cout <<"Please enter a number between 10 and 100: ";
    cin >> n;
    
    
    while (n<10|| n>100){
        cout << "Invalid input. Please enter a number between 10 and 100:" << endl;
        cin >> n;
    }
    
    int fizz =0, buzz=0, fizzbuzz=0;
    
    for(int i=1; i<=n; i++){
        
        
            
            if(i%7== 0){
                cout << "(" <<i<< " is skipped)" << endl;
                continue;
            }
            
            if(i%3== 0 && i%5 == 0){
                cout << "FizzBuzz" << endl;
                fizzbuzz++;
            }else if( i%3== 0){
                cout << "Fizz" << endl;
                fizz++;
            }else if( i%5== 0){
                cout << "Buzz" << endl;
                buzz++;
            }else{
                cout <<i<< endl;
                
            }
    
    }
    
    cout << "--- Summary ---" << endl;
    cout << "Fizz count :" << fizz<< endl;
    cout << "Buzz count :" << buzz<< endl;
    cout << "FizzBuzz count:" << fizzbuzz<< endl;
    
    
    
    // ---Task 3 ---
    
    int m;
    cout << "Please enter a number between 3 and 9:";
    cin >> m;
    
    while ( m<3 || m>9){
        cout << "Please enter a number between 3 and 9:";
        cin >> m;
        
    }
    
    for ( int j=1; j<2*m; j++){
        int k = m-abs(m-j);
        
        for (int t=1; t<=k; t++){
            cout<< t;
            
        }
        cout<< endl;
    }
    


    return 0;
     
}
