#include <stdio.h>
#include <cstdlib>
using namespace std;

int main(int argc, char **argv){
	FILE *pFile;
	pFile = fopen(argv[1],"r");
	FILE *oFile; 
	oFile = fopen("rand_test.dat","w");

	if(pFile != NULL){
			double a,b,c;
			while(fscanf(pFile,"%lf %lf %lf",&a,&b,&c) != EOF){
				c = (rand() % 2)-1;
				fprintf(oFile,"%lf %lf %lf\n",a,b,c);
			}
	}

}
