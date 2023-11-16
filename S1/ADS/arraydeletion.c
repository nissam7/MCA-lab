#include<stdio.h>
#define MAX_SIZE 100
int main()
{
int arr[10];
int i,size,position;
printf("Enter the size of the array:\n");
scanf("%d",&size);
printf("Enter the %d element:\n",size);
for(i=0;i<size;i++)
{
scanf("%d",&arr[i]);
}
printf("Enter the position to delete:");
scanf("%d",&position);
if(position<0||position>=size)
{
printf("invalid position for deletion:\n");
}
else
{
for(i=position;i<size-1;i++)
{
arr[i]=arr[i+1];
}
size--;
printf("array after deletion:\n");
for(i=0;i<size;i++)
{
printf("%d",arr[i]);
}
}
}
