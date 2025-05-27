.data
eqmsg: .asciiz "the numbers are eaual."
nemsg: .asciiz "the numbers are not equal."

.text
main:
	li $t0, 5
	li $t1, 5
	beq $t0,$t1, equal
not_equal:
	la $a0, nemsg
	li $v0, 4
	syscall
	j exit
equal:
	la $a0, eqmsg
	li $v0,4
	syscall
exit:
	li $v0,10
	syscall