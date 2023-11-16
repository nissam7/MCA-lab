#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node*prev;
	struct node*next;
};
struct node *start;
void beginsert()
{
struct node*ptr;
int x;
ptr=(struct node*)malloc(sizeof(struct node*));
if(ptr==NULL)
{
	printf("\nOverflow");
}
else
{
printf("\nEnter value:");
scanf("%d",&x);
if(start==NULL)
{
ptr->data=x;
ptr->prev=NULL;
ptr->next=NULL;
start=ptr;
}
else
{
ptr->data=x;
ptr->prev=NULL;
ptr->next=start;
start->prev=ptr;
start=ptr;
}
}
}
void lastinsert()
{
struct node *ptr,*temp;

