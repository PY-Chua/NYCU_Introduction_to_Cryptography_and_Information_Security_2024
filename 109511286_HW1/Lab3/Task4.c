#include <stdio.h>
#include <openssl/bn.h>

#define NBITS 128

void printBN(char *msg, BIGNUM * a)
{
    /* Use BN_bn2hex(a) for hex string
    * Use BN_bn2dec(a) for decimal string */
    char * number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main ()
{
    BN_CTX *ctx = BN_CTX_new();

    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    //python3 -c 'print("I owe you $2000.".encode("utf-8").hex())'
    BIGNUM *M1 = BN_new(); //2000
    BIGNUM *M2 = BN_new(); //3000
    BIGNUM *d = BN_new();
    BIGNUM *S1 = BN_new();
    BIGNUM *S2 = BN_new();
    
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&M1, "49206f776520796f752024323030302e");
    BN_hex2bn(&M2, "49206f776520796f752024333030302e");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    
    BN_mod_exp(S1, M1, d, n, ctx);
    BN_mod_exp(S2, M2, d, n, ctx);
    printf("M = I owe you $2000.\n");
    printBN("Sign = ", S1);
    printf("M = I owe you $3000.\n");
    printBN("Sign = ", S2);    

    return 0;
}

