# Regex CheatSheet
Cheat Sheet for Regular expression syntax, created by someone_todo.
Modified by Christian Toderascu.

**last update: 20231017**

last update available on [GitHub - Regex CheatSheet.md](https://github.com/Todochris/CheatSheets/blob/main/Regex%20CheatSheet.md)  
[link of the source](todo)


## Anchors
| command       | description   |
| :------------ | :------------ |
| ^	            | Start of string or line
| \A	        | Start of string
| $	            | End of string or line
| \Z	        | End of string
| \b	        | Word boundary
| \B	        | Not word boundary
| `\<`	        | Start of word
| `\>`	        | End of word


## Character Classes
| command       | description   |
| :------------ | :------------ |
| .	            | Any character except newline (\n)
| \w	        | Word [A-Za-z0-9_]
| \W	        | Not Word [^A-Za-z0-9_]
| \s	        | Whitespace [ \t\r\n\v\f]
| \S	        | Not Whitespace [^ \t\r\n\v\f]
| \d	        | Digit [0-9]
| \D	        | Not digit [^0-9]
| \x	        | Hexadecimal digit [A-Fa-f0-9]
| \O	        | Octal Digit [0-7]
| \c	        | Control character

## POSIX Classes
| command       | description   |
| :------------ | :------------ |
| [:upper:]	    | Uppercase letters [A-Z]
| [:lower:]	    | Lowercase letters [a-z]
| [:alpha:]	    | All letters [A-Za-z]
| [:alnum:]	    | Digits and letters [A-Za-z0-9]
| [:digit:]	    | Digits [0-9]
| [:xdigit:]	| Hexadecimal digits [0-9a-f]
| [:punct:]	    | Punctuation
| [:blank:]	    | Space and tab [ \t]
| [:space:]	    | Blank characters [ \t\r\n\v\f]
| [:cntrl:]	    | Control characters [\x00-\x1F\x7F]
| [:graph:]	    | Printed characters [\x21-\x7E]
| [:print:]	    | Printed characters and spaces [\x20-\x7E]
| [:word:]	    | Digits, letters and underscore [A-Za-z0-9_]


## Pattern Modifiers
| command       | description   |
| :------------ | :------------ |
| //g	        | Global match (all occurrences)
| //i	        | Case-insensitive
| //m	        | Multiple line
| //s	        | Treat string as single line
| //x	        | Allow comments and whitespace
| //e	        | Evaluate replacement
| //U	        | Ungreedy pattern



## Escape Sequences
| command       | description   |
| :------------ | :------------ |
| \	            | Escape following character
| \Q	        | Begin literal sequence
| \E	        | End literal sequence


## Quantifiers
| command       | description   |
| :------------ | :------------ |
| *	            | 0 or more
| +	            | 1 or more
| ?	            | 0 or 1 (optional)
| {3}	        | Exactly 3
| {3,}	        | 3 or more
| {2,5}	        | 2, 3, 4 or 5


quantifiers comes after the character or group they affect.

## Groups and Ranges
| command       | description   |
| :------------ | :------------ |
| (a|b)	        | a or b
| (...)	        | Group
| (?:...)	    | Passive (non-capturing) group
| [abc]	        | Single character (a or b or c)
| `[^abc]`	    | Single character (not a or b or c)
| [a-q]	        | Single character range (a or b ... or q)
| [A-Z]	        | Single character range (A or B ... or Z)
| [0-9]	        | Single digit from 0 to 9


## Assertions
| command       | description   |
| :------------ | :------------ |
| ?=	        | Lookahead assertion (put after character, as it is normal)
| ?!	        | Negative lookahead (put after character, as it is normal)
| ?<=	        | Lookbehind assertion (put before character)
| `?!= / ?<!`	| Negative lookbehind (put before character)
| ?>	        | Once-only Subexpression
| ?()	        | Condition [if then]
| ?()|	        | Condition [if then else]
| ?#	        | Comment


## Special Characters
| command       | description   |
| :------------ | :------------ |
| \n	        | New line
| \r	        | Carriage return
| \t	        | Tab
| \v	        | Vertical tab
| \f	        | Form feed
| \ooo	        | Octal character ooo
| \xhh	        | Hex character hh


## String Replacement

| command       | description   |
| :------------ | :------------ |
| $n	        | n-th non-passive group
| $2	        | "xyz" in /^(abc(xyz))$/
| $1	        | "xyz" in /^(?:abc)(xyz)$/
| $`	        | Before matched string
| $'	        | After matched string
| $+	        | Last matched string
| $&	        | Entire matched string
