#include <stdio.h>
using namespace std;

class node{
	public:
			float threshold;
};

int main(){
		node a;
		a.threshold = 100;
		printf("node threshold: %f\n",a.threshold);

		int var1=10;
		char var2[10];

		printf("var1: %p var2: %p\n", &var1, &var2);

		int *ip;
		ip = &var1;

		printf("ip address: %p ip value: %d\n", ip, *ip);

		int int_list[100];
		printf("the sizeof(int): %lu\n", sizeof(int));

		for(int i=0; i < 100; i++){
			printf("int_list: %d Address: %p\n", i, int_list+i);
			printf("int_list: %d Address: %p\n", i, &int_list[i]);
		};

		char *p[];
		char p_arr[]="abcdef";
		p = &p_arr;
		printf("p_arr: %s p_pointer: %s", p_arr, *p);
}
