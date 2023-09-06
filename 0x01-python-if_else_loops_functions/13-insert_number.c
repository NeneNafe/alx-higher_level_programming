#include "lists.h"

/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list
 * @head: a double pointer
 * @number: integer variable
 * Return: the address of the new node
 *         or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (node && node->n < number)
	{
		prev = node;
		node = node->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = node;
	}

	return (new);
}
