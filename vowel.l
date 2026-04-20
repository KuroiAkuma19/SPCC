%option noyywrap
%{
 #include<stdio.h>
 int countV=0, countC=0; 
%}
vowel[Aa,Ee,Ii,Oo,Uu]
const[A-Z,a-z]

%%
{vowel} {countV++;}
{const} {countC++;}
\n {return 0;}
%%
int main()
{yylex();
printf("Vowel count=%d\n",countV);
printf("const count=%d",countC);
return 0;
}