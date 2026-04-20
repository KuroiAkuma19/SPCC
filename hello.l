%option noyywrap
%{
 #include<stdio.h>
%}
number[0-9]+

%%
{number} {printf("Value entered is number");}
"greet" {printf("Whatsup Brother");}
"Hi" {printf("Hello World");}
\n {return 0;}
%%
int main()
{yylex();
return 0;
}

