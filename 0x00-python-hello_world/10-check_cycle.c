#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: pointer to linked list.
 * Return: 0 or 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *second, *first;

	second = list;
	first = list;

	while (second && first && first->next)
	{
		first = first->next->next;
		second = second->next;

		if (second == first)
			return (1);
	}

	return (0);
}
