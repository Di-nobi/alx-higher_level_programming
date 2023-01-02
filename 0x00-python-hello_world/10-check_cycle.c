#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked list has a cycle
 * @list: head
 * Return: 0 if there is no cycly, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *T = list;
	listint_t *H = list;

	if (list == NULL)
{
	return (0);
}
	while (T != NULL && H != NULL && H->next != NULL)
{
	H =  list->next->next;
	T = list->next;

	if (H == T)
{
	return (1);
}
}
return (0);
}
