#include <stdio.h>
#include <math.h>
 
int numDigits(long x) {
	int c = 0;
	
	while (x != 0) {
		x /= 10;
		c++;
	}
	return c;
} 

int main() {
 
    int n, i;
    long int a, b, c, valor;
    
    scanf("%d", &n);
    
    for(i=0 ; i<n ; i++) {
	    scanf("%ld%ld", &a, &b);
	 
	 	c = numDigits(b);
	 	c = pow(10, c);
	 	
	 	valor = a % c;
	 	
	 	if(b == valor) printf("encaixa\n");
	 	else printf("nao encaixa\n");
	}
    	
    return 0;
}
