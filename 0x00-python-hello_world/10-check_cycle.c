#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	if (!list || !list->next)
		return (0);

	turtle = turtle->next;
	hare = hare->next;
	hare = hare->next;

	while (turtle && hare)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next;
		hare = hare->next;
		hare = hare->next;
	}
	return (0);
}
