#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: The pointer to the list.
* @number: The given number.
*
* Return: the address of the new node, or NULL if it failed.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pos = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!pos || new_node->n < pos->n)
	{
		new_node->next = pos;
		*head = new_node;
		return (*head);
	}

	while (pos)
	{
		if (!pos->next || new_node->n < pos->next->n)
		{
			new_node->next = pos->next;
			pos->next = new_node;
			return (pos);
		}
		pos = pos->next;
	}

	return (NULL);
}
