#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head);
void reverse(listint_t **ref);
int compare(listint_t *first_head, listint_t *second_head);

/**
 * reverse - counts the number of nodes of the list
 * @ref: points to the pointer of the first node of the list
 *
 * Return: nothing
 */
void reverse(listint_t **ref)
{
	listint_t *prev = NULL;
	listint_t *cur = *ref;
	listint_t *next;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*ref = prev;
}

/**
 * compare - compares two linked lists
 * @first_head: points to the head of the first list
 * @second_head: points to the head of the second list
 *
 * Return: 1 if content is equal, else 0
 */
int compare(listint_t *first_head, listint_t *second_head)
{
	listint_t *first_temp = first_head;
	listint_t *second_temp = second_head;

	while (first_temp && second_temp)
	{
		if (first_temp->n == second_temp->n)
		{
			first_temp = first_temp->next;
			second_temp = second_temp->next;
		}
		else
			return (0);
	}

	if (first_temp == NULL && second_temp == NULL)
		return (1);

	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is
 * palindrome
 * @head: points to the first node of the list
 *
 * Return: 0 if not palindromic, 1 else
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev_of_slow = *head;
	/* To handle odd size */
	listint_t *min_node = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		/* Get the middle of the list */
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}
		/* Checks for even or odd elements in list */
		if (fast != NULL)
		{
			min_node = slow;
			slow = slow->next;
		}

		second_half = slow;
		/* NULL terminate first half */
		prev_of_slow->next = NULL;
		reverse(&second_half);
		res = compare(*head, second_half);
		/* Construct the original list back */
		reverse(&second_half);

		if (min_node != NULL)
		{
			prev_of_slow->next = min_node;
			min_node->next = second_half;
		}
		else
			prev_of_slow->next = second_half;
	}
	return (res);
}
