// delegating_constructor.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

class dog
{
    int m_age;
    string m_name;
    int m_weight;
    bool m_small;

public:
    void init()
    {
        m_age = 0;
        m_name = "name";
        m_weight = 0;
    }

    bool if_small(int weight)
    {
        m_weight = weight;
        if (m_weight < 5)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    dog()
    {
        init();
    }

    dog(int age): dog() 
    {
        m_age = age;
    }

    int get_age()
    {
        return m_age;
    }

    bool if_the_dog_is_small()
    {
        return m_small;
    }
};

int main()
{
    dog toby(5);
    auto is_small = toby.if_the_dog_is_small();

    if (is_small)
    {
        std::cout << "The dog is small\n";
    }
    else
    {
        std::cout << "The dog is big\n";

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
