A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to if/else conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.

The compile() function from the re module compiles the string passed as the argument into a regular expression object that can be used by other re methods.

Character classes also allow you to indicate a range of characters to match. You need to specify the starting and the ending characters separated by an hyphen, -. Characters follow the Unicode order.

Since the underscore character is a valid character for variable names, it is included in the \w character class (equivalent to [a-zA-Z0-9_]), which can be conveniently used to match variable names.

Therefore, the \W character class is equivalent to [^a-zA-Z0-9_] with the underscore character that is not matched. For this reason you cannot use it to match all your special characters.
