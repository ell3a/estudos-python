# POO

Arquivos de estudos sobre Programação Orientada a Objetos.

Os códigos desse repositório resultam do estudo do livro [Introdução à Orientação a Objetos com C++ e Python: Uma Abordagem Prática](https://www.amazon.com.br/Introdu%C3%A7%C3%A3o-Orienta%C3%A7%C3%A3o-Objetos-Python-Abordagem/dp/8575225480/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=C%2B%2B+python&qid=1618242878&sr=8-1).


## Anotações

## Introdução

Além das classes, objetos, herança e polimorfismo, POO é pensar o software como pequenas unidades que trocam dados por meio de mensagens é pensar um programa como um conjunto de células ou um computadores em uma rede, trocando informações.

A linguagem C++ foi criada por Bjarme Stroustrup em 1980 (Bell Labs), sendo chamada inicialmente de C com classes, para implementar uma versão distribuída do Unix, recebebndo 1984 recebe o nome de C++.

### Exemplos de um códigos em C++

~~~cpp
/*
Primeiro Programa em C++
01.cpp

Imprime 'Olá, mundo!' na tela
*/

#include <iostream>

using namespace std;

int main(void) {
    cout << "Olá, Mundo!\n";
    return 0;
}
~~~

* `#include <iostream>`: entrada e saída padrão;
* `cout`: essa instrução faz parte `<iostream>`;

Ao fazermos um uso de `<>` para fazermos a inclusaão de uma biblioteca C++ estamos informando ao compilador que essa biblioteca é uma bibliotec padrão da linguagem, usando `""` informamos que é uma biblioteca presente no diretório corrente.

A função `main` deve está presente em todo programa C++. O operador `<<` (colocar para), escreve o argumento na saída padrão.


~~~cpp
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
~~~

## Tipagem Estática

Em C++ o tipo de cada objeto, variável, array, matriz, etc., deve ser conhecido pelo compilador. Isso possibilita encontrar erros de tipo antes da execução e delimitar valores possíveis para uma variável. Os tipos nstivod de variáveis para C++ são: char, wchar_t; string; int; short int; long int; float; double e boll. Uma variável é armazenada na memória. O processo de criar associar uma área da memória a uma variável é chamado de alocação.

Existem quarto categorias de alocação:
* estática: alocação antes do início da execução, para definirmos uma variável estática usamos `static`;
* dinâmica da pilha: criada a partir de uma sentença de declaração, sendo alocadas e liberadas em tempo de execução na pilha (stack memory);
* dinâmica no heap explícita: as variáveis nessa categoria são alocadas e liberadas por meio de instruições em tempo de execução, alocadas com `new` e liberadas com `delete`;
* dinâmica no heap implicíta: as variáveis são alocadas quando são atribuídos valores a elas.

## Tipagem Dinâmica

Python é uma linguagem de tipagem dinâmica. O interpretador quarda informações sobre os tipos de variáveis, não sendo necessário declarar previamente seu tipo. A vantagem desse tipo de tipagem é a flexibilidade no desenvolvimento, no entanto há dificuldades em detectar erros.