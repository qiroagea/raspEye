#ifndef __REQUEST__
#define __REQUEST__

typedef enum{
	STP = 0,
	STR,
	ROT
} run_state_t;

extern void request_set_runmode(run_state_t state, int speed, int dist);
extern int  request_get_runmode(run_state_t *state, int *speed, int *dist);
extern int  request_set_board_p();
extern int  request_set_board_s();
extern int 	request_set_board_d();
extern int  timer_3(void);
extern int  timer_2(void);
extern int  timer_4(void);
extern int  request_get_dist(int *dist_l, int *dist_r);
extern int  request_get_batt(double *volt);

#endif
