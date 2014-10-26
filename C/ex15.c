/* 
   This example introduces pointers in C. Pointers point
   to a specific address in your computer's memory.
   They can be incremented or decremented to access other
   addresses in memory. In this exercies, you will see that
   you can work with pointers and arrays in many of the same
   ways, but remember: pointers are NOT arrays, and vice-versa.

   There are four primary useful things you do with pointers
   in C code:

   1) Ask the OS for a chunck of memory and use a pointer to work with
   	  it. This includes strings and something you haven't seen yet,
   	  structs.

   2) Passing large blocks of memory (like large structs) to functions
   	  with a pointer so you don't have to pass the whole thing to them.

   3) Taking the address of a function so you can use it as a
   	  dynamic callback.

   4) Complex scanning of chunks of memory such as converting bytes
   	  off a network socket into data structures or parsing files.

   For nearly everything else you see people using pointers for,
   they should be using arrays. In the eary days of C programming
   people used pointers to speed up their programs because the
   compilers were really bad at optimizing array usage. These days
   the syntax to access an array vs. a pointer are translated into
   the same machine code and optimized the same, so it's not as
   necessary. Instead, you go with arrays every time you can, and then
   only use pointers as a performance optimization if you absolutely
   have to.

   The Pointer Lexicon

   I'm now going to give you a little lexicon to use for reading and
   writing pointers. Whenever you run into a complex pointer statement,
   just refer to this and break it down bit by bit (or just doin't use
   that code since it's probably not good code):

   type *ptr
   		"a pointer of type named ptr"

   *ptr
   		"the value of whatever ptr is pointed at"

   *(ptr + i)
   		"the value of (whatever ptr is pointed at plus i)"

   *&thing
   		"the address of thing"

   type *ptr = &thing
   		"a pointer of type named ptr set to the address of thing"

   ptr++
   		"increment where ptr points"

   	We'll be using this simple lexicon to break down all of the
   	pointers we use from now on in the book.
*/

#include <stdio.h>

int main(int argc, char *argv[])
{
	// create two arrays we care about
	int ages[] = {23, 43, 12, 89, 2};
	char *names[] = {
		"Alan", "Frank",
		"Mary", "John", "Lisa"
	};

	// safely get the size of ages
	int count = sizeof(ages) / sizeof(int);
	int i = 0;

	// first way using indexing
	for(i = 0; i < count; i++)
	{
		printf("%s has %d years alive.\n",
				names[i], ages[i]);
	}

	printf("---\n");

	// setup the pointers to the start of the arrays
	int *cur_age = ages;
	char **cur_name = names;

	// second way using pointers
	for(i = 0; i < count; i++)
	{
		printf("%s is %d years old.\n",
				*(cur_name+i), *(cur_age+i));
	}

	printf("---\n");

	// third way, pointers are just arrays
	for(i = 0; i < count; i++)
	{
		printf("%s is %d years old again.\n",
				cur_name[i], cur_age[i]);
	}

	printf("---\n");

	// fourth way with pointers in a stupid complex way
	for(cur_name = names, cur_age = ages;
		(cur_age - ages) < count;
		cur_name++, cur_age++)
	{
		printf("%s lived %d years so far.\n",
			*cur_name, *cur_age);
	}	

	return 0;
}