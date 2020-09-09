#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *new = *head, *h = *head;
	int array[3000], len = 0;

	while (new != NULL)
		array[len] = new->n, new = new->next, len++;
	len--;
	while (h != NULL)
		if (h->n == array[len])
			h = h->next, len--;
		else
			return (0);
	return(1);
}
