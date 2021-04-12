Skip to content
Why GitHub? 
Team
Enterprise
Explore 
Marketplace
Pricing 
Search

Sign in
Sign up
orlandosaraivajr
/
ioo
63
Code
Issues
Pull requests
Actions
Projects
Security
Insights
ioo/01/C++/Passagem.cpp
@orlandosaraivajr
orlandosaraivajr first commit
Latest commit f857acb on 29 Jan 2017
 History
 1 contributor
42 lines (35 sloc)  1.13 KB
 
/*
Programa:   Passagem
Arquivo:    Passagem.cpp
*/
#include <iostream>

using namespace std;

void por_valor(float parametro1,int parametro2) 
{
    cout << " Alterando-se valores na função por_valor. ";
    parametro1 = parametro1 + 10;
    parametro2 = parametro2 + 5;
    cout << " parametro1 = "<< parametro1 ;
    cout <<" parametro2 = "<<parametro2 << endl;
}

void por_referencia(float &parametro1,int &parametro2) 
{
    cout << " Alterando-se valores na função por_referencia. ";
    parametro1 = parametro1 + 10;
    parametro2 = parametro2 + 5;
    cout << " parametro1 = "<< parametro1 ;
    cout <<" parametro2 = "<<parametro2 << endl;
}

int main() {
    float numero_float = 5.3;
    int numero_inteiro = 4;
    cout << "numero_float = "<< numero_float ;
    cout <<" numero_inteiro = "<< numero_inteiro << endl;
    por_valor(numero_float,numero_inteiro);

    cout << "numero_float = "<< numero_float ;
    cout <<" numero_inteiro = "<< numero_inteiro << endl;
    por_referencia(numero_float,numero_inteiro);

    cout << "numero_float = "<< numero_float ;
    cout <<" numero_inteiro = "<< numero_inteiro << endl;
    return 0;
}

© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete