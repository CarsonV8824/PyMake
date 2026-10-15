#include <iostream>

int main()
{
    unsigned age;
    std::cout << "hello world, how old are you? ";
    std::cin >> age;
    if (age < 18)
    {
        std::cout << "Your a kid\n";
    } else 
    {
        std::cout << "Your an adult\n";
    }
    return 0;
}