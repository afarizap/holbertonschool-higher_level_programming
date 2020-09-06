#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - pointer to the node
 * @head: head of the node
 * @number: number to insert in node
 * Return: pointer to the node with the new number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new; return (new);
	if (aux->n < number)
		*head = new; return (new);
	while (aux->next != NULL)
	{
		if (aux->next->n < number)
			new->next = aux->next; aux->next = new; return (new);
	}
	aux->next = new; return (new);
}
