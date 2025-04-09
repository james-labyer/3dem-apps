filepath = ""
cores = 16

run("Bio-Formats Macro Extensions");
for (m = 0; m < cores + 1; m++){
	run("Bio-Formats Importer", "open=[" + filepath + "]");
	print(m);
}

print("Opened all files")

for (n = 0; n < cores + 1; n++){
	close();
}