#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/time.h>
#include <signal.h>
#include "arduino.h"
#include "io.h"
#include "request.h"
#include "uss.h"

int main(){
	double volt;
	
	if(io_open() != 0) return -1;
	if(arduino_open() != 0) return -1;
	//if(uss_open_l() != 0) return -1;
	//if(uss_open_r() != 0) return -1;
	int millisecond = 5*1000;
	printf("press enter to start\n");
	getchar();
	
	/*void mySleep(int second) {
    time_t now = second * CLOCKS_PER_SEC + clock();
 
    while (now > clock()) ;
	}
	int second = 5;
	
	while(1){
		request_line_trace();
			if(request_line_trace() == 1){
				request_set_board_s();
			}else if(request_line_trace() == 0){
				request_set_board_p();
				mySleep(second);
				request_set_board_s();
			}
		}*/
	while(1){
		timer_5();
		break;
	}
	
//	arduino_close();
	return 0;
}
