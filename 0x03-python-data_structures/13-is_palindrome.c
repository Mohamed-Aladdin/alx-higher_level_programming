#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int x = 0, y = 0, len = 0, arr[10000];

	if (*head == NULL)
		return (1);
	current = *head;

	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	if (len == 1)
		return (1);
	current = *head;

	while (current != NULL)
	{
		arr[x] = current->n;
		x++;
		current = current->next;
	}
	x--;
	len--;

	while (x >= len / 2)
	{
		if (arr[x] != arr[y])
			return (0);
		x--;
		y++;
	}
	return (1);
}
