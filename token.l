%option noyywrap
%{
 #include<stdio.h>
 int keyC = 0 , literalC = 0, punC = 0 , optC = 0 , identC = 0;
%}
key "int"|"float"|"printf"|"scanf"|"if"
literal[0-9]+
opt "/"|"*"|"-"|"="|"+"
ident[a-z,A-Z]
pun","|"("|")"|":"|";"|["]

%%
{ident} {identC++;}
{key} {keyC++;}
{literal} {literalC++;}
{pun} {punC++;}
{opt} {optC++;}

\n {return 0;}
%%
int main()
{yylex();
printf("Key count=%d\n",keyC);
printf("literal count=%d\n",literalC);
printf("opt count=%d\n",optC);
printf("Pun count=%d\n",punC);
printf("Identifier count=%d\n",identC);
return 0;
}