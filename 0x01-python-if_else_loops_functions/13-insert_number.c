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
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;
	return (newNode);
}
