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
	while (aux)
	{
		if (aux->next == NULL)
			aux->next = new; break;
		if (aux->next->n < number)
			new->next = aux->next; aux->next = new; break;
		aux = aux->next;
	}
	return (new);
}
