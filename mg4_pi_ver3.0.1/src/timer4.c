#include  <stdio.h>
#include  <time.h>

/*--- xミリ秒経過するのを待つ ---*/
int sleep(unsigned long x)
{
    clock_t  s = clock();
    clock_t  c;

    do {
        if ((c = clock()) == (clock_t)-1)       /* エラー */
            return (0);
    } while (1000UL * (c - s) / CLOCKS_PER_SEC <= x); 
    return (1);
}

int timer_4(void)
{
    int  code;

    printf("開始\n");
    request_set_board_p();
    
    code = sleep(4000);                        /* 10秒停止 */

    printf("終了(%d)\n", code);
    request_set_board_s();

    return (0);
}
