#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node*next;
};
struct node*start;
void push()
{
int x;
struct node*ptr;
ptr=malloc(sizeof(struct node));
if(ptr==0)
{
	printf("\ncan't push element");
}
else
{
printf("\nEnter the value:");
scanf("%d",&x);
if(start==0)
{
ptr->data=x;
ptr->next=0;
start=ptr;
}
else
{
ptr->data=x;
ptr->next=start;
start=ptr;
}
}
}
void pop()
{
int x;
struct node*ptr;
if(start==0)
{
	printf("\n underflow");
}
else
{
x=start->data;
ptr=start;
start=start->next;
free(ptr);
printf("Element popped-%d",x);
}
}
void traverse()
{
struct node*temp;
if(start==0)
printf("\n List is empty\n");
else
{
temp=start;
printf("The list is\n");
while(temp!=0)
{
	printf("%d---->",temp->data);
	temp=temp->next;
}
}
}
void search()
{
int i=1,f=0,x;
struct node*ptr;
ptr=start;
if(ptr==0)
{
printf("\nstack is empty");
}
else
{
printf("\nEnter element:");
scanf("%d",&x);
while(ptr!=0)
{
	if(ptr->data==x)
	{
f=1;
break;
}
i++;
ptr=ptr->next;
}
if(f==0)
	printf("\nitem not found");
else
printf("\nitem found at position%d",i);
}
}
void main()
{
int ch=0;
while(ch!=5)
{
printf("\n\n1:push");
printf("\n2:pop");
printf("\n3:Linear search");
printf("\n4:Display");
printf("\n5:Exit");
printf("\nEnter your choice:");
scanf("%d",&ch);
switch(ch)
{
case 1:push();
break;
case 2:pop();
break;
case 3:search();
break;
case 4:traverse();
break;
case 5:exit(0);
break;
default:printf("\ninvalid choice");
}
}
}
