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
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;

	if (current == NULL || number < current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && number > current->n)
	{
		prev = current;
		current = current->next;
	}

	prev->next = new_node;
	new_node->next = current;

	return (new_node);
}
