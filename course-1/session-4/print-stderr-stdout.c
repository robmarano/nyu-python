#include <stdio.h>

void main() {
    printf("%s", "This is STDOUT\n");              // "Hello world" on stdout (using printf)
    fprintf(stdout, "%s", "This is STDOUT\n");     // "Hello world" on stdout (using fprintf)
    fprintf(stderr, "%s", "This is STDERR\n"); // Error message on stderr (usign fprintf)
}

