/**
 * @file main.c
 * @brief A simple example to demonstrate Doxygen usage.
 */

/**
 * @brief Adds two integers.
 *
 * @param a First integer.
 * @param b Second integer.
 * @return Sum of the two integers.
 */


int add(int a , int b ){
    return a+b;
}

/**
 * @brief Subtracts the second integer from the first.
 *
 * @param a First integer.
 * @param b Second integer.
 * @return Difference of the two integers.
 */
int sub(int a , int b){
    return a-b;
}
/**
 * @brief mult ttwo number
 *
 * @param a First integer.
 * @param b Second integer.
 * @return mul of the two integers.
 */
int mul(int a , int b){
    return a*b;
}
/**
 * @brief division two number
 *
 * @param a First integer.
 * @param b Second integer.
 * @return division of the two integers.
 */
int div(int a ,int b){
    return a/b;
}

int main(){
    int result_1 = add(9,3);
    int result_2 = sub(9,3);
    int result_3 = mul(9,3);
    int result_4 = div(9,3);

    return 0;

}
