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
    BIGNUM *M = BN_new(); 
    BIGNUM *d = BN_new();
    BIGNUM *S1 = BN_new();
    BIGNUM *S2 = BN_new();
    BIGNUM *res1 = BN_new(); 
    BIGNUM *res2 = BN_new();     
    
    BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&S1, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F");
    BN_hex2bn(&S2, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6803F");
    BN_hex2bn(&M, "4c61756e63682061206d697373696c652e");
    
    BN_mod_exp(res1, S1, e, n, ctx);
    BN_mod_exp(res2, S2, e, n, ctx);
    
    printBN("Message = ", M);
    printBN("Verified message 1 = ", res1);
    printBN("Verified message 2 = ", res2);
    if (BN_cmp(res1, M) == 0)
    {
        printf("Signature 1 is Alice's!\n");
    }
    else
    {
        printf("Signature 1 is not Alice's!\n");
    }
    if (BN_cmp(res2, M) == 0)
    {
        printf("Signature 2 is Alice's!\n");
    }
    else
    {
        printf("Signature 2 is not Alice's!\n");
    }  

    return 0;
}

