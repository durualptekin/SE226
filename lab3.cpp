#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2){
    int temp= *p1;
    *p1 =*p2;
    *p2=temp;
}

void printArray(int* arr, int size){
    
    for(int i=0; i<size ; i++ ){
        
        cout<< *(arr+i) << " ";
    }
    cout<< endl;
}

int findMax(int* arr, int size){
    
    if(size<=0){
        return 0;
    }
    
    int maxValue= *arr;
    
    for(int i =1; i < size; i++){
        
        if( *(arr+i) > maxValue){
            maxValue= *(arr+i);
        }
        
    }
    
    return maxValue;
}

void reverseArray(int* arr, int size){
    
    int* left= arr;
    int* right= arr+ (size - 1);
    
    while(left<right){
        
        swapValues(left, right);
        left++;
        right--;
    }
}

int* createArray(int size){
    
    return new int[size];
    
}

void deleteArray(int* arr){
    
    delete[] arr;
    cout<< "Memory released successfully."<< endl;
    
}


int main(){
    
    int size;
    cout<< "Creating dynamic array..."<< endl;
    cout<< "Enter array size: ";
    cin>> size;
    
    
    int* newArr= createArray(size);
    cout<< "Enter values: ";
    for(int i=0; i<size ; i++ ){
        
        cin>> *(newArr+i);
        
    }
    
    cout<< "Array elements: " <<endl;
    printArray(newArr, size);
    
    cout<< "Maximum element: "<< findMax(newArr, size)<<endl;
    
    cout<< "----------------------------------"<< endl;
    
    int a=5;
    int b =3;
    cout << "Swapping two numbers \nBefore swap: \na = "<< a<< "\nb = "<< b << endl;
    swapValues(&a, &b);
        cout<< "After swap: \na = "<< a<< "\nb = "<< b <<endl;
        
     cout<< "----------------------------------"<< endl;
     
     cout<< "Reversing array..."<< endl;
     reverseArray(newArr, size );
     cout<< "Array after reverseArray:"<< endl;
     printArray(newArr, size);
     
     cout<< "----------------------------------"<< endl;
     cout<< "Deleting array..."<< endl;
     deleteArray(newArr);
     
     
     return 0;
     
}
