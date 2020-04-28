#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list->next;
	listint_t *hare = list->next;

	if (!list || !list->next)
		return (0);
	hare = list->next;
	while (turtle && hare)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next; hare = hare->next; hare = hare->next;
	}
	return (0);
}
