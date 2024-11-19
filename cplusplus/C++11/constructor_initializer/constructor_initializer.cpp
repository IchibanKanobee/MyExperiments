// constructor_initializer.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

class dog
{
    int m_age;
    string m_name;

public:
    dog(int age, string name)
    {
        m_age = age;
        m_name = name;
    }

    int get_age()
    {
        return m_age;
    }
};
int main()
{
    dog toby{ 2, "Toby" };
    std::cout << toby.get_age();
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
