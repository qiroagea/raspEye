#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>

void sigfunc(void){
    printf("｢dofunc関数」を処理中\n");
}

void dofunc(int num){
  if(num == SIGALRM){
    printf("｢sigfunc関数」を処理中\n");
  }else{
    exit(1);
  }
}

int main(void){
  
  struct itimerval timer;
  
  signal(SIGALRM , dofunc);
  
  memset(&timer , 0 , sizeof(timer));
  timer.it_value.tv_sec  = 3;
  timer.it_value.tv_usec = 0;
  
  for(int i; i < 1; i++){
    setitimer(ITIMER_REAL , &timer , NULL);
    pause( );
  
    sigfunc();
    //dofunc();
    i++;
  }
  return 0;
  
}
