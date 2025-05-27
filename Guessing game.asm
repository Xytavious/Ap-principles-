#***lp4-9***
.data
prompt: .asciiz "enter a # betwwn 1 and 20: "
prtcpu: .asciiz "\nCPUs #: "
prtusr: .asciiz "\nYour #: "
prtwin: .asciiz "\nYou win!"
prtlos: .asciiz "\nYou lose. "

.text
main:
	# generate number between 1-20 using syscall 42
	la $a1,20
	li $v0, 42
	syscall
	add $s0, $a0, 1 # s0 = a0 +1(min)
	# user intput
	la $a0, prompt
	li $v0,4
	syscall
	li $v0, 5
	syscall
	move $t0,$v0
	#show cpu number
	la $a0, prtcpu
	li $v0,4
	syscall
	move $a0,$s0
	li $v0,1
	syscall
	#show user number
	la $a0, prtusr
	li $v0,4
	syscall
	move $a0,$t0
	li $v0,1
	syscall
	# if (t0 != s0 ) goto lose
	bne $t0,$s0,do_lose
do_win:
	la $a0,prtwin
	li $v0,4
	syscall
	j exit
do_lose:
	la $a0,prtlos
	li $v0,4
	syscall
exit:
	li $v0,10
	syscall
	
	