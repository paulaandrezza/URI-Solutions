#include <stdio.h>
 
int main() {
 
	int NUMBER, HORAS;
	float VALOR, SALARY;
 	
	scanf("%d", &NUMBER);
	scanf("%d", &HORAS);
	scanf("%f", &VALOR);
	
	SALARY=VALOR*HORAS;
	
	printf("NUMBER = %d\n", NUMBER);
	printf("SALARY = U$ %.2f\n", SALARY);
 
    return 0;
}
