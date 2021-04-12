/*
Segundo Programa em C++
02.cpp

Recebe o nome do usuário e o imprime na tela.
*/

#include <iostream>

using namespace std;

void nome(void) {
    string nome;
    cout << "Digite seu nome: \n";
    cin >> nome;
    cout << "Olá, " << nome << ". Tudo bem?\n";
}

int main(void) {
    nome();
    return 0;
}