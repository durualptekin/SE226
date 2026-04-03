#include <iostream>
using namespace std;


double g(int n, double r) {
    if (n==0)
    return 1;
    
    return (r * geometric(n - 1, r)) + 1;
}

int main()
{
    int n;
    double r;

    cout << "Enter n: ";
    cin >> n;

    cout << "Enter r: ";
    cin >> r;

    double result = geometric(n, r);

    cout << "Result: " << result << endl;

    return 0;
}
