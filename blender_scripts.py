import bpy

time_gap = 0.333
current_frame = 0
final_frame = 10
frame_offset = 0

cfs = bpy.data.collections["cf"].objects

file=open('sequences.txt', 'w')

for frame in range(current_frame, final_frame):
    bpy.data.scenes['Scene'].frame_set(frame)
    for cf in cfs:
        file.write('    (')
        file.write(str(bpy.data.scenes['Scene'].frame_current+frame_offset))
        file.write(', ')
        file.write(str(cf.name_full))
        file.write(', Goto(')
        file.write(str(round(cf.location[0],2)))
        file.write(' ,')
        file.write(str(round(cf.location[1],2)))
        file.write(' ,')
        file.write(str(round(cf.location[2],2)))
        file.write(' ,')
        file.write(str(time_gap))
        file.write(')),\n')
        
file.close()
