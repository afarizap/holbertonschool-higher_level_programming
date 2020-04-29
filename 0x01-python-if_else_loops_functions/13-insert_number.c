#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linkedlist
 * @number: number to add
 * Return: adress of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
