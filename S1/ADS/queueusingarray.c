#include<stdio.h>
#include<stdlib.h>
#define size 100
void enqueue();
void dequeue();
void show();
int inp_arr[10];
int rear=-1;
int front=-1;
void main()
{
int ch;
while(1)
{
printf("1.Enqueue operation\n");
printf("2.Dequeue operation\n");
printf("3.Display the queue\n");
printf("4.Exit\n");
printf("Enter yout choice of operation:");
scanf("%d",&ch);
switch(ch)
{
	case 1:
	enqueue();
	break;
	case 2:
	dequeue();
	break;
	case 3:
	show();
	break;
	case 4:
	exit(0);
	default :
	printf("incorrect choice\n");
	}
}
}
void enqueue()
{
int insert_item;
if(rear==size-1)
printf("overflow\n");
else
{
if(front==-1)
front=0;
printf("Element to be inserted in the queue:\n");
scanf("%d",&insert_item);
rear=rear+1;
inp_arr[rear]=insert_item;
}
}
void dequeue()
{
if(front==-1||front>rear)
{
printf("underflow\n");
return;
}
else
{
printf("element deleted from the queue:%d\n",inp_arr[front]);
front=front+1;
}
}

void show()
{
if(front==-1)
printf("Empty queue\n");
else
{
printf("queue:\n");
for(int i=front;i<=rear;i++)
printf("%d",inp_arr[i]);
printf("\n");
}
}
