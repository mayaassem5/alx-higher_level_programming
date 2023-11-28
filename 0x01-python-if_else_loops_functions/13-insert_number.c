#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 ** insert_node - adds a new node to listint_t list
 ** @head: pointer to pointer of first node of listint_t list
 ** @number: integer to be included in new node
 ** Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NUll)
		return (NULL);
	
	new->n = number;
	new->next = NULL;
	while (current != NULL)
	{
		if (new->n > current->n)
		{
			current->next = new;
			current = current->next;
		}

		else
			new->next = current;
	}
	return (new);
}
