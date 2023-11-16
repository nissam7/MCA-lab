#include<stdio.h>
int main()
{
int i,arr[10];
int size,element,position;
printf("Enter the size of the array:");
scanf("%d",&size);
printf("Enter the %d element:\n",size);
for(i=0;i<size;i++)
{
scanf("%d",&arr[i]);
}
printf("Enter the element to insert:");
scanf("%d",&element);
printf("Enter the position:");
scanf("%d",&position);
if(position<=size&&position>=0)
{
for(i=size;i>position;i--)
arr[i]=arr[i-1];
arr[position]=element;
for(i=0;i<=size;i++)
printf("%d",arr[i]);
}
else
printf("invalid position\n");
return 0;
}
