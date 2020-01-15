#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>
#define MILLI_SEC 1000000
#include "arduino.h"
#include "request.h"

void request_set_runmode(run_state_t state, int speed, int dist){
	command_data_t command_data;
	
	command_data.val[0] = ((state == STR) ? 2 : (state == ROT) ? 3 : 1);
	command_data.val[1] = speed;
	command_data.val[2] = dist;
	
	arduino_send(command_data);
}

int request_get_runmode(run_state_t *state, int *speed, int *dist){
	command_data_t command_data;
	
	command_data.val[0] = 10;
	command_data.val[1] = 0;
	command_data.val[2] = 0;
	
	arduino_clear();
	arduino_send(command_data);
	usleep(50 * 1000);
	
	if(arduino_receive(&command_data) == 0){
		*state = ((command_data.val[0] == 2) ? STR : (command_data.val[0] == 3) ? ROT : STP);
		*speed = command_data.val[1];
		*dist  = command_data.val[1];
		return 0;
	}else{
		return -1;
	}
}

int request_get_dist(int *dist_l, int *dist_r){
	command_data_t command_data;
	
	command_data.val[0] = 11;
	command_data.val[1] = 0;
	command_data.val[2] = 0;
	
	arduino_clear();
	arduino_send(command_data);
	usleep(50 * 1000);
	
	if(arduino_receive(&command_data) == 0){
		*dist_l = command_data.val[0];
		*dist_r = command_data.val[1];
		return 0;
	}else{
		return -1;
	}
}

int request_get_batt(double *volt){
	command_data_t command_data;
	
	command_data.val[0] = 12;
	command_data.val[1] = 0;
	command_data.val[2] = 0;
	
	arduino_clear();
	arduino_send(command_data);
	usleep(50 * 1000);
	
	if(arduino_receive(&command_data) == 0){
		*volt = command_data.val[0] / 100.0;
		return 0;
	}else{
		return -1;
	}
}

int request_set_board(int board_mode){
	command_data_t command_data;
	
	command_data.val[0] = 20;
	command_data.val[1] = board_mode;
	
	arduino_send(command_data);
}

void request_line_trace(){
	command_data_t command_data;
	
	command_data.val[0] = 13;
	
	arduino_send(command_data);
}

int start_set(){
	request_get_runmode(ROT,50,60);
	request_get_runmode(STR,50,100);
	request_get_runmode(ROT,50,90);
}


int phase_run() {
	int finish = 0;
	int state,speed,dist;
	command_data_t command_data;
	
	if (uss_get_l() < 100 && uss_get_r() < 100) {
		request_set_runmode(STP, 0, 0);
		printf("stop\n");
		sleep(1);
	}
	else {
	while(1){
		request_line_trace();
	}
	return finish;
	}
}

/*
void sigfunc(int num){
	if (num == SIGALRM){
		printf("「sigfunc関数」を処理中\n");
		request_set_board_p();
	}else{
		exit(1);
	}
}

void dofunc(void){
  printf("「dofunc関数」を処理中\n");
  request_set_board_s();
  }

int timer_3(void){
  
  struct itimerval timer;
  
  signal(SIGALRM , sigfunc);
  
  memset(&timer , 0 , sizeof(timer));
  timer.it_value.tv_sec  = 5;
  timer.it_value.tv_usec = 0;
  
  for(int i; i < 1; i++){
    setitimer(ITIMER_REAL , &timer , NULL);
    pause( );
  
    dofunc( );
    i++;
  }
  return 0;
  
}*/




/*int timer_2(void){
	for (int i = 1; i <= 5; i++){
		clock_t t = clock();
			while ((clock() - t) < CLOCKS_PER_SEC);
				if(t ==5){
					request_set_board_s();
				}else{
					request_set_board_p();
				}
			printf("%d\n", i);
			fflush(stdout);
	}
}*/


/*--- xミリ秒経過するのを待つ ---*/
/*int sleep_1(unsigned long x)
{
    clock_t  s = clock();
    clock_t  c;

    do {
        if ((c = clock()) == (clock_t)-1)       /* エラー 
            return (0);
    } while (1000UL * (c - s) / CLOCKS_PER_SEC <= x); 
    return (1);
}

int timer_4(void)
{
    int  code;

    printf("開始\n");
    request_set_board_p();
    
    code = sleep_1(4000);                        /* 10秒停止 

    printf("終了(%d)\n", code);
    //request_set_board_s();

    return (0);
}*/

int timer_5(){
int cnt;
struct timespec req = {0,5000*MILLI_SEC};
	request_set_board(1);
	for(cnt = 0; cnt < 9; cnt++){
		
		if(nanosleep(&req, NULL)  == -1){
			perror(NULL);
		}
	}
	request_set_board(0);
	printf("STOP!\n");
		
		return 0;
}
