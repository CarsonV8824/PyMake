#include <iostream>

using namespace std;

int input;
int output;
int place;
int base;


int main()
{
    
    cout << "Enter a number between 0 and 31: ";
    cin >> input;
    const int orginal = input;
    cout << "Enter a base between 2 and 9: ";
    cin >> base;

    cout << "In binary, your number is: ";
    output = 0;
    place = 1;
    while (input > 0)
    {
        for (int i = (base-1); i > 0; i--)
        {
            if (input % base == i)
            {
                output += (i * place);
                break;
            }
        }

        input /= base;
        place *= 10;
        
    }
    if (output < 10)
    {
        cout << "0000" << output << "\n";
        return 0;
    } else if (output < 100)
    {
        cout << "000" << output << "\n";
        return 0;
    } else if (output < 1000)
    {
        cout << "00" << output << "\n";
        return 0;
    } else if (output < 10000)
    {
        cout << "0" << output << "\n";
        return 0;
    }
}