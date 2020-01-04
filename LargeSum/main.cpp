# include <iostream>
# include <string>
# include <climits>
# include <vector>
# include <cmath>

// 37107287533902102798797998220837590246510135740250 
// + 37107287533902102798797998220837590246510135740250
// = 74214575067804205597595996441675180493020271480500

class BigNum
{
public:
    BigNum(const std::string& num)
    {   
        int numBits = std::max((int) log2(num.length()) + 1, 0); //approximate number of bits going to be used
        int numBytes = numBits >> 3; // divide by 8
        std::cout << numBytes << std::endl;
        buff.reserve(numBytes);
        
        /*
        int digit = num % 256;
        num = num / 256
        */
        
        /*
        unsigned int index = num.length() - 1;
        while (index >= 0)
        {
            unsigned int i = index;
            unsigned int val = 0;
            unsigned int stride = 0;
            while (i >= 0 && val < UCHAR_MAX)
            {
                val = val * 10 + num[i];
                i--;
                stride++;
            }
            // use val

            index = i;
        }

        for (int i = num.length() - 1;i >= 0;i++)
        {
            val
        }
        */
    }

    BigNum add(const BigNum& num)
    {
        // int sum = buff[] + num.buff[];
        int sum = 0;
        if (sum > UCHAR_MAX)
        {

        }
        return BigNum("");
    }
private:
    std::vector<unsigned char> buff;

};

int main()
{
    BigNum big1 = BigNum("20");
    BigNum big2 = BigNum("34");
    BigNum res = big1.add(big2);

    int num1 = 20;
    int num2 = INT_MAX;

    std::cout << "num1:" << num1 << std::endl;
    std::cout << "num2:" << num2 << std::endl;

    unsigned int sum = num1 + num2;
    
    std::cout << sizeof(int) << std::endl;
    std::cout << sum << std::endl;

    if(sum > INT_MAX)
    {
        std::cout << "overflow" << std::endl;
    }
    else
        std::cout << "no overflow" << std::endl;

    //BigNum big1 = BigNum("37107287533902102798797998220837590246510135740250")
    //BigNum big2 = BigNum("37107287533902102798797998220837590246510135740250")
    //BigNum res = big1.add(big2)

    return 0;
}