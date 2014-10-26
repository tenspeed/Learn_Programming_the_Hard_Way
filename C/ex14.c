#include <stdio.h>
#include <ctype.h>

// forward declarations
// this is basically telling C ahead of time
// that we're going to use these functions
// which it hasn't encountered yet.
// Notice that can_print_it() and print_letters()
// don't show up in int main(), which is why they
// need to be declared ahead of time. These functions
// only show up inside of print_arguments().
int can_print_it(char ch);
void print_letters(char arg[]);

void print_arguments(int argc, char *argv[])
{
	int i = 0;

	for(i = 0; i < argc; i++)
	{
		print_letters(argv[i]);
	}
}

void print_letters(char arg[])
{
	int i = 0;

	for(i = 0; arg[i] != '\0'; i++)
	{
		char ch = arg[i];

		if(can_print_it(ch))
		{
			printf("'%c' == %d ", ch, ch);
		}
	}

	printf("\n");
}

int can_print_it(char ch)
{
	// isalpha(char) is a built-in fuction of the ctype library
	// and returns 1 if the char is a letter and 0 otherwise.
	// isblank(char) is a also a built-in function of ctype
	// and returns 1 if the char is a whitespace ' ' and
	// 0 otherwise.
	return isalpha(ch) || isblank(ch);
}

int main(int argc, char *argv[])
{
	print_arguments(argc, argv);
	return 0;
}