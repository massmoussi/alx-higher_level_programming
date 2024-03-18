#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int size = 0, i;
	int *arr;

	if (head == NULL || *head == NULL)
		return (1);

	/* Count the number of nodes in the list */
	while (current)
	{
		size++;
		current = current->next;
	}

	/* Allocate memory for the array */
	arr = malloc(sizeof(int) * size);
	if (arr == NULL)
		return (0);

	/* Store the values of the list in the array */
	current = *head;
	for (i = 0; i < size; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}

	/* Check if the array is a palindrome */
	for (i = 0; i < size / 2; i++)
	{
		if (arr[i] != arr[size - i - 1])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}

