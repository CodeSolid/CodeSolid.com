Something about type_traits
---------------------------

Types_traits example.

This is based on the example here:  https://en.cppreference.com/w/cpp/types/is_integral

I don't understand what the point of showing that the integer type is an integer.  I suppose this might make sense for certain user-defined types?
No -- added that code and it still doesn't make any sense.

For more information on the SHOW macro variadic argument
behavior, see https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html

.. literalinclude:: ../../src/snippets/type_traits.cpp
	:language: c++