#include <stdio.h>
#include <stdlib.h>
#define MAX 30
#include "queue.h"
// inserting and removing elements, for displaying the dequeue, for displaying
//individual nodes, and for displaying the dequeue in reverse order.

int queue_empty (queue_t q)
{
    return (q.number_elements == 0);
}

void enqueueend (queue_t *q, int item)
{
  queue_rect *new;
  new = (queue_rect *) malloc(sizeof(queue_rect));
  new->a = item;
  new->next=NULL;

  if(q->head == NULL || q->tail == NULL)
  {
    q->head = new;
    q->tail = new;
  }
  else
  {
    q->head->next = new;
    q->head = new;
  }
}

void enqueuefront (queue_t *q, int item)
{
  queue_rect *new;
  new = (queue_rect *) malloc(sizeof(queue_rect));
  new->a = item;
  new->next=NULL;

  if(q->head == NULL || q->tail == NULL)
  {
    q->head = new;
    q->tail = new;
  }
  else
  {
    new -> next = q->tail;
    q->tail = new;
  }
}

void dequeuefront (queue_t *q, int *item)
{
  if(q->tail == NULL)
  {
    printf("Its all empty\n");
  }
  else
  {
    *item = q->head->a;
    q->tail = q->tail->next;
  }
}

void dequeueend (queue_t *q, int *item)
{
  queue_rect *new;
  if(q->head == NULL)
  {
    printf("Its all empty\n");
  }
  else
  {
    *item = q->head->a;
    if(q->head == q->tail)
    {
      q->head = NULL;
      q->tail = NULL;
    }
    else if(q->tail->next == q->head)
    {
      q->head = q->tail;
      q->tail->next = NULL;
    }
    else
    {
      new = q->tail;
      while(new->next != q->head)
      {
        new = new->next;
      }
      q->head = new;
      q->head->next = NULL;
    }
  }
}

void queqeprint(queue_t *q)
{
  queue_rect *cur;
  cur = q->tail;
  while (cur != NULL)
  {
    printf("element %d\n",cur->a);
    cur = cur->next;   /* cur = (*cur).next */
  }   
}

void reversequeue(queue_t q, int i) {
    int element;
    if (q.head == NULL) {
      return;
    }
    dequeueend(&q, &element);
    i = i+1;
    reversequeue(q, i);
    arr[i] = element;
}