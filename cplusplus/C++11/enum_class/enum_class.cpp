// enum_class.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

enum orange { big_o, small_o };
enum apple { red_a, green_a };

enum class orange_c { big, small};
enum apple_c { red, green };


int main()
{
    apple apple_a = red_a;
    orange or_o = big_o;

    if (or_o == apple_a)
    {
        std::cout << "Apples and oranges are the same\n";
    }

    orange_c o_c = orange_c::big;
    apple_c a_c = apple_c::green

    if (o_c == a_c)
    {
        std::cout << "Apples and oranges are the same\n";
    }
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
