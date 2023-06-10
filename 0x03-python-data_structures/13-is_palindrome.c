#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to pointer of first node
 * Return: 1 if is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	int *data;
	listint_t *iter;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	iter = *head;
	data = malloc(sizeof(int) * 1024);
	if (data == NULL)
		exit(1);
	while (iter)
	{
		data[i] = iter->n;
		iter = iter->next;
		len++;
		i++;
		if (i == 1024)
		{
			data = realloc(data, 2 * i);
			if (data == NULL)
				exit(1);
		}
	}
	for (i = 0; i < (len / 2); i++)
	{
		if (data[i] != data[len - i - 1])
			return (0);
	}
	return (1);
}
