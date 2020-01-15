#include <stdio.h>
#include <time.h>

int timer_2(void){
	for (int i = 1; i <= 5; i++){
		clock_t t = clock();
			while ((clock() - t) < CLOCKS_PER_SEC);
				if(i ==5){
					request_set_board_s();
				}else{
					request_set_board_p();
					printf("%d\n", i);
			fflush(stdout);
		}
}
