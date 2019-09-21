//Name Rohit Gurnani
// Lab Section 501

#include <stdio.h>     //Libraries
#include <stdlib.h>
#include "queue.h"

int main(int argc, char **argv)
{
	int i, num;
    queue_t q;
    q.head = q.tail = NULL;
    q.number_elements = 0;
    printf("Beginning - queue is empty %d\n",queue_empty(q));

    printf("\nAdding new elements (1,2,3,4,5) from front(TOP) in queue linked list\n");
    enqueuefront(&q,1); //Adding from front
    enqueuefront(&q,2);
    enqueuefront(&q,3);
    enqueuefront(&q,4);
    enqueuefront(&q,5);

    printf("On the queue linked list\n");
    queqeprint(&q);  //priting queue

    printf("\nAdding new elements (6,7,8,9,10) from back(BOTTOM) in queue linked list\n");
    enqueueend(&q,6);  //Adding from back
    enqueueend(&q,7);
    enqueueend(&q,8);
    enqueueend(&q,9);
    enqueueend(&q,10);

    printf("On the queue linked list\n");
    queqeprint(&q);  //priting queue

    printf("\nDequeuing 2 elements (4,5) from the front of queue(top)\n");
    dequeuefront(&q, &num);
    dequeuefront(&q, &num);
    printf("On the queue linked list\n");
    queqeprint(&q);  //priting queue

    printf("\nDequeuing 1 element (10) from the back of queue(bottom)\n");
    dequeueend(&q, &num);
    printf("On the queue linked list\n");
    queqeprint(&q);  //priting queue

    reversequeue(q, 0); //empties the queue and fills in array
    for (i = 6; i > 0; i--)
      enqueuefront(&q,arr[i]); // filling the queue with array elements in reverse

    printf("\nOn the REVERSE queue linked list\n");
    queqeprint(&q);  //priting reverse queue

    printf("\nEnd\n");
	return 0;
}
