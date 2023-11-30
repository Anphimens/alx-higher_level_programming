#include "lists.h"


/**
 * insert_node - a function that inserts a new node
 *		into a sorted singly linkedlist
 * @head: Head of the node
 * @number: parameter as number
 *
 * Return: Address of the new_node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = NULL;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < current->n)
	{
		new_node->next = *head;
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
