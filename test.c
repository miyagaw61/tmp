/* test.c */
#include <stdio.h>
#include <string.h>

void succeeded()
{
    puts("auth succeeded!");
}

void failed()
{
    puts("auth failed.");
}

int main(int argc, char *argv[])
{
    char username[256];
    char password[256];
    printf("Enter username: ");
    scanf("%s", username);
    printf("Enter password: ");
    scanf("%s", password);
    if (strcmp(username, "admin") == 0 && strcmp(password, "letmein") == 0) {
        succeeded();
    } else {
        failed();
    }
    return 0;
}
