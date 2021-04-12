#include <iostream>

using namespace std;

float soma(float n1, float n2) {
    float resultado;
    resultado = n1 + n2;

    return resultado;
}

int main(void) {
    float r1, r2;

    r1 = soma(3,5);
    r2 = soma(1.2,1.5);

    cout << r1 << '\n';
    cout << r2 << '\n';

    return 0;
}