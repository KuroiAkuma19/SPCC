%option noyywrap
%{
 #include<stdio.h>
%}

%%
[A-Z,a-z]+abb {printf("Your string ends in abb");}
[^A-Z,a-z]+abb {printf("Your string does not end in abb");}
%%

int main()
{yylex();
return 0;
}