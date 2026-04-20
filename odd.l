%option noyywrap
%{
 #include<stdio.h>
 int a; 
%}

number[0-9]+

%%
{number} { a = atoi(yytext);
            if (a % 2==0)
             printf("%d is Even\n",a);
            else
            printf("%d is odd\n",a);
             }

\n {return 0;}
%%
int main()
{yylex();
return 0;
}