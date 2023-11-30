%{
#include<stdio.h>
int line=1,slno=1;
%}
ws[\t]
LETTER[a-zA-Z]
DIGIT[0-9]
DQ["]
%%
{ws}+ {}
"\n" {line++;}}
"void"|"main"|"for"|"if"|"else" {printf("\n%d\t%s\tkeyword\t%d",slno,yytext,line);slno++;}
{LETTER}({LETTER}|{DIGIT})* {printf("\n%d\t%s\tidentifier\t%d",slno,yytext,line);slno++;}
{DIGIT}+"."{DIGIT}+  {printf("\n%d\t%s\tfloat_point\t%d",slno,yytext,line);slno++;}
{DIGIT}+  {printf("\n%d\t%s\tnumber\t%d",slno,yytext,line);slno++;}
"("|"{"|"["  {printf("\n%d\t%s\topen_bracket\t%d",slno,yytext,line);slno++;}
"+"|"-"|"*"|"/"  {printf("\n%d\t%s\tARITH-OP\t%d",slno,yytext,line);slno++;}
"<"|"<="|">"|">="  {printf("\n%d\t%s\tREL_OP\t%d",slno,yytext,line);slno++;}
";"  {printf("\n%d\t%s\tsemicolon\t%d",slno,yytext,line);slno++;}
{DQ}  {printf("\n%d\t%s\tdouble_quates\t%d",slno,yytext,line);slno++;}
","|"#"  {printf("\n%d\t%s\tspecial_symbol\t%d",slno,yytext,line);slno++;}
. {printf("\n%d\t%s\tunrecognized\t%d",slno,yytext,line);slno++;}
%% 
main()
{
 printf("slno\tlexemes\ttoken\tlineno");
 yyin=fopen("input.c","r");
yylex();
}
int yywrap()
{
 return 1;
}
