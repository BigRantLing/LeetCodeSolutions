#include <stdio.h>


int main(void)
{
    int n;
    int f[30]={0};
    for (int i = 0; i<30; i++)
    scanf("%d", &n);
    f[0] = 1;f[1]  = 1;
    
    for(int i = 2; i <= n; i++)
    {
        for(int j = 0; j < i; j++) 
        {   
            printf("i=%d   j=%d \n", i, j);
            printf("f[%d]:%d   f[%d]:%d \n", j, f[j], i-j-1, f[i-j-1]);
            printf("BEFOR: f[%d] is %d\n", i, f[i]);
            f[i] += f[j] * f[i-j-1];
            printf("AFTER: f[%d] is %d\n", i, f[i]);
        }
    }  
    
    printf("\n");
    printf("%d", f[n]);
    return 0;
}

// i = 3   
// i = 2
//     j = 0
//         f[2] = f[2]+f[0]+f[1] = 2
//     j = 1
//         f[2] = f[2]+f[1]+f[0] = 3

// i = 3
//     j = 0
//     f[3] =  f[3]+f[0]+f[2]=4
//     j = 1
//     f[3] = f[3]+f[1]+f[1]=6
//     j = 2
//     f[3] =f[3]+f[2]+f[0]=10