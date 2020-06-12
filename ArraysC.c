#include <stdio.h>
int main()
{int n,i;
scanf("%d",&n);
if(n>=1 && n<=1000)
{
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=n-1;i>=0;i--)
    {
        printf("%d ",arr[i]);
    }
}
else 
    exit(0);
return 0;}
