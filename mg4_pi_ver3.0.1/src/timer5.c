#include <stdio.h>
#include <sys/time.h>
#define MILLI_SEC 1000000

int main(){
int cnt;
struct timespec req = {0,5000*MILLI_SEC};
	printf("モータ開始\n");
	
	for(cnt = 0; cnt < 5; cnt++){
		
		if(nanosleep(&req, NULL)  == -1){
			perror(NULL);
		}
	}
	printf("STOP!\n");
		
		return 0;
}
