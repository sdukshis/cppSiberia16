#include <iostream>

#include <bar.h>
#include <foo.h>

int main() {
    std::cout << "foo(): " << foo() << '\n';
    std::cout << "bar(): " << bar() << '\n';

    return 0;
}
