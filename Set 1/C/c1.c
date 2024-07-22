#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* hex_to_base64(char *hex, char *base64) {
    unsigned long len = strlen(hex);
    unsigned long res_len = (len + len%2) * 3 / 2;
    char *bytes = malloc(res_len+1);

    char base64_table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    // char hex_table[] = "0123456789abcdef";

    int index = 0;
    for (unsigned long i = 0; i < len; i++) {
        char cur_hex = hex[i];
        if (cur_hex >= '0' && cur_hex <= '9') {
            cur_hex -= '0';
        } else if (cur_hex >= 'a' && cur_hex <= 'f') {
            cur_hex -= 'a' - 10;
        } else {
            printf("Invalid hex character: %c\n", cur_hex);
            exit(1);
        }

        // might be a more efficient way to do this,
        // but there seems to be a pattern of 3s, where the cur
        // hex is the upper 4, lower 2 and upper 2 of the next,
        // and then the lower 4. I'll try a different approach next time
        if (i % 3 == 0) {
            bytes[index] = cur_hex << 2;
        } else if (i % 3 == 1) {
            bytes[index] |= cur_hex >> 2;
            bytes[index] = base64_table[bytes[index]];
            index++;
            bytes[index] = (cur_hex & 0x3) << 4;
        } else { // i % 3 == 2
            bytes[index] |= cur_hex;
            bytes[index] = base64_table[bytes[index]];
            index++;
        }
    }
    bytes[res_len+1] = '\0';

    return bytes;
}

// 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
// SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

// 1 hex = 4 bits
// 1 base64 = 6 bits

int main() {
    char hex[] = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    char answer[] = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
    char base64[1000];
    char* result = hex_to_base64(hex, base64);
    printf("%s\n", result);
    if (strncmp(answer, result, strlen(answer)) != 0) {
        printf("strings do not match");
    } else {
        printf("passed\n");
    }
    free(result);
    return 0;
}