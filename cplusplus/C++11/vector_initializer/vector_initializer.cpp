// vector_initializer.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//https://www.youtube.com/watch?v=U6mgsPqV32A&list=PLX5SDkl7TCjj4QnQTttvYpHprm8hnn7uD&index=1&ab_channel=BoQian

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v = { 3,4,1,9 };
    for (auto i : v)
        cout << i;
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
