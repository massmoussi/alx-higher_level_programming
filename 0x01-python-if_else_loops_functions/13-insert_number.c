#include "lists.h"

/**
 * insert_node - function insert node in sorted linked list
 * @head: pointer to pointer to head of list
 * @number: integer value to insert in the list
 * Return: NULL if it fail , Otherwise the new list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Newnode;
	listint_t *temp = *head;

	Newnode = malloc(sizeof(listint_t));
	if (Newnode == NULL)
	{
		return (NULL);
	}

	Newnode->n = number;
	Newnode->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		Newnode->next = *head;
		*head = Newnode;
		return (Newnode);
	}
	else
	{
		while (temp->next != NULL && temp->next->n < number)
		{
			temp = temp->next;
		}

		Newnode->next = temp->next;
		temp->next = Newnode;
	}
	return (*head);
}
