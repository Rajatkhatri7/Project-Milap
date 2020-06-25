/*
 There are diff type of integers in cpp

 short int              unsigned short int
 int                    unsigned int
 long int               unsigned long int
 long long int          unsigned long long int


 they differ in size

 hexadeciaml 0x
 binary      0b


*/

#include <iostream>
#include <cstdint>


using namespace std;

int main(){
    // 1 byte = 8 bits

    printf("Size of this datatpye is : %ld bytes\n ",sizeof(int));
    printf("Size of this datatpye is : %ld bytes \n ",sizeof(short int));
    printf("Size of this datatpye is : %ld bytes \n ",sizeof(long int));
    printf("Size of this datatpye is : %ld bytes \n ",sizeof(long long int));


     printf("Size of this datatpye is : %ld bytes\n ",sizeof(uint32_t));
    
    return 0 ;





}