Script is  $0
Script directory is $(dirname “$0”)
$1, $2, $3 are arguments passed to the script
$@ treats all arguments as a single string
“$@“ treats each argument as a separate string
“$*” treats all arguments as a single string
Shift moves all arguments to the left, effectively discarding the first argument. 
Break is used to exit a for, while, or until loop prematurely


2>&1 sends stderr to stdout


Exit 0 is success, 1 is failure, 2 is special failure
/dev/null is a void/black hole/pit of despair
A bang ! is a logical NOT
A vertical line | passes the output of one command to the input of another. Two vertical lines || acts as a logical OR, running a second command only if the first fails

An ampersand & runs a command in the background, not waiting for it to finish before initiating the next command. Two ampersand && acts as a logical AND, running a second command only if the first succeeds

A chevron > is used to write the output of a command to a file. Two chevrons >> appends the output of a command to the end of a file

-e checks if a file exists
-f checks if a file is a regular file
-d checks if a file is a directory
-r checks if a file is readable
-w checks if a file is writable
-x checks if a file is executable
-s checks if a file is not empty
-t checks if a file descriptor is associated with a terminal
-p checks if a file is a named pipe (FIFO)
-L checks if a file is a symbolic link
-h is an alias of -L
-c checks if a file is a character device (/dev/tty)
-b checks if a file is a block device.

-n checks if a string is not empty.
-z checks if a string is empty.
= checks if two strings are equal.
!= checks if two strings are not equal.

-eq checks is two numbers are equal
-ne checks if two numbers are not equal 
-lt checks if a number is less than another
-le checks if a number is less than or equal to another
-gt checks if a number is greater than another
-ge checks if a number is greater than or equal to another

# Example Loops
numbers='7 15 32'
for number in $numbers
do
  echo $number
done

counter=1
while [ $counter -lt 10 ]
do
  echo $counter
  ((counter++))
done

until [ $counter -gt 10 ]
do
  echo $counter
  ((counter++))
done

# Example case statement

read country
echo -n "The official language of $country is "

case $country in

  Lithuania)
    echo -n "Lithuanian"
    ;;

  Romania | Moldova)
    echo -n "Romanian"
    ;;

  *)
    echo -n "unknown"
    ;;
esac
