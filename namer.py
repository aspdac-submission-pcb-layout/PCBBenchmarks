

for i in range(1, 100):

	filename = 'bm' + str(i) + '/bm' + str(i) + '.routed.kicad_pcb'
	new_file = ''

	with open(filename, 'r') as f:
		print()
		print()
		print(filename)
		component_count = 1
		for line in f.readlines():
			new_line = line
			if '(fp_text reference ""' in line:
				new_line = line.replace('(fp_text reference ""', '(fp_text reference "U' + str(component_count) + '"', 1)
				component_count += 1
				print(new_line[:-1])
			new_file += new_line

	with open(filename, 'w') as f:
		f.write(new_file)
