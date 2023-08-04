total_brinq = int(input())
total_Teresa = int(input())
total_Carla = int(input())

total_Joaquim = total_brinq - total_Teresa - total_Carla

print(f'Teresa vendeu {total_Teresa} (de {total_brinq}) brinquedos. ({(total_Teresa/total_brinq)*100:.2f}%)')
print(f'Joaquim vendeu {total_Joaquim} (de {total_brinq}) brinquedos. ({(total_Joaquim/total_brinq)*100:.2f}%)')
print(f'Carla vendeu {total_Carla} (de {total_brinq}) brinquedos. ({(total_Carla/total_brinq)*100:.2f}%)')

