# *** Prog 52a ***
.data 
prompt1: .asciiz "enter length: "
prompt2: .asciiz "enter Width: "
out1: .asciiz "area: "
out2: .asciiz "\nPerimeter: "

 .text
 main:
 	# === intput length ===
 	la $a0, prompt1 # print_str(a0)
 	li $v0, 4
 	syscall 
 	li $v0,5
 	syscall
 	move $t0,$v0
 	la $a0, prompt2 # a0 = prompt2)
 	li $v0, 4       # print_str(a0)
 	syscall 
 	li $v0,5  # v0 = read_int()
 	syscall
 	move $t1,$v0 # t1 = v0
 	# === Calculate ===
 	#mul 
 	mult $t0, $t1 # area lo = length t0 * width t1
 	mflo $t4  # t4 = lo
 	li $s2, 2
 	mul $t8,$t0,$s2
 	mul $t9, $t1,$s2
 	add $t5,$t8,$t9
 	# === output ===
 	la $a0, out1 #a0 = out1 area message
 	li $v0,4 # print_str a0
 	syscall
 	move $a0, $t4
 	li $v0,1
 	syscall
 	la $a0, out2 #a0 = out1 area message
 	li $v0,4 # print_str a0
 	syscall
 	move $a0, $t5
 	li $v0,1
 	syscall
 exit:
 	li $v0,10
 	syscall