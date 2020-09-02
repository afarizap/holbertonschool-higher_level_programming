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

	if (aux == NULL)
	{
		add_nodeint_end(head, number);
		return (aux);
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (aux->n > new->n)
		new->next = aux;
	else
	{
		while (aux->next->n < number)
			aux = aux->next;
		new->next = aux->next;
		aux->next = new;
	}
	return (new);
}
