#include<stdio.h>
#include<stdlib.h>
struct node
{
int info;
struct node*link;
};
struct node*start;
void traverse()
{
	struct node*temp;
	if(start==0)
	printf("\n List is empty\n");
else
{
	temp=start;
	printf("the list is\n");
	while(temp!=0)
{
	printf("%d--->",temp->info);
	temp=temp->link;
}
}
}
void insertAtfront()
{
	int data;
	struct node*temp;
	temp=malloc(sizeof(struct node));
	printf("\n Enter number to be inserted:");
	scanf("%d",&data);
	temp->info=data;
	temp->link=start;
	start=temp;
}
void insertAtend()
{
	int data;
	struct node*temp,*head;
	temp=malloc(sizeof(struct node));
	printf("\n Enter number to be inserted:");
	scanf("%d",&data);
	temp->link=0;
	temp->info=data;
	head=start;
	while(head->link!=0)
{
	head=head->link;
}
	head->link=temp;
}
void insertAtposition()
{
	struct node*temp,*newnode;
	int pos,data,i=1;
	newnode=malloc(sizeof(struct node));
	printf("\nenter postion and data:");
	scanf("%d%d",&pos,&data);
	temp=start;
	newnode->info=data;
	newnode->link=0;
	while(i<pos-1)
{
	temp=temp->link;
	i++;
}
	newnode->link=temp->link;
	temp->link=newnode;
}
void deletefirst()
{
	struct node*temp;
	if(start==0)
	printf("\n list is empty\n");
else
{
	temp=start;
	start=start->link;
	free(temp);
}
}
void deleteEND()
{
	struct node *temp,*prevnode;
	if(start==0)
	printf("\nlist is empty\n");
else
{
	temp=start;
	while(temp->link!=0)
{
	prevnode=temp;
	temp=temp->link;
}
	free(temp);
	prevnode->link=0;
}
}
void deleteposition()
{
	struct node *temp,*position;
	int i=1,pos;
	if(start==0)
	printf("\n list is empty\n");
else
{
	printf("\n enter postion:");
	scanf("%d",&pos);
	position=malloc(sizeof(struct node));
	temp=start;
	while(i<pos-1)
{
	temp=temp->link;
	i++;
}
	position=temp->link;
	temp->link=position->link;
	free(position);
}
}
int main()
{
int choice;
while(1)
{
printf("\n\t1 to see list\n");
printf("\t2 for inserton at starting\n");
printf("\t3 for insertion at end\n");
printf("\t4 for insertion at any position\n");
printf("\t5 for deletion at first element\n");
printf("\t6 for deletion at last element\n");
printf("\t7 for deletion of element at any position\n");
printf("\t8 to exit\n");
printf("\nEnter choice:\n");
scanf("%d",&choice);

switch(choice)
{
case 1:
traverse();
break;
case 2:
insertAtfront();
break;
case 3:
insertAtend();
break;
case 4:
insertAtposition();
break;
case 5:
deletefirst();
break;
case 6:
deleteEND();
break;
case 7:
deleteposition();
break;
case 8:
exit(1);
break;
default:
printf("incorrect choice\n");
}
}
return 0;
}


