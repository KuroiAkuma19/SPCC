%option noyywrap
%{
    #include <stdio.h>
%}

%%
A[a-zA-Z]{2}    { printf("Matched word: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}
