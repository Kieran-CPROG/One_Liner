#Kieran U
#9/23/24
#One Line, must not fail

# ONE LINE - NO MORE, NO LESS


table =  [(x+1) * (y+1) for x in range(10) for y in range(10)]


########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################