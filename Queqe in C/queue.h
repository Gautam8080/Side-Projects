
typedef struct queueRecord
{
    int a; 
    struct queueRecord *next; 
} queue_rect;

typedef struct queue_list
{
    queue_rect *head, *tail;
    int number_elements;
} queue_t;

extern void enqueuefront (queue_t *, int);
extern void enqueueend (queue_t *, int);
extern int queue_empty (queue_t);
extern void dequeuefront (queue_t *, int *);
extern void dequeueend (queue_t *, int *);
extern void queqeprint(queue_t *);
extern void reversequeue(queue_t, int);
int element;
int arr[7];