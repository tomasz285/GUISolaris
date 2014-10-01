def addlayer(picturename, text="ICON"):
	my_file = open(picturename, "r+w")
	lines_of_file = my_file.read()
	lll=str(lines_of_file)
	lista=lll.split("<svg ")
		#for i in lista:
		#	print i, "     ##########     " 
	x=  ' <svg xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
	y= '<g inkscape:groupmode="layer"  id="001" visiblity="visible">    <rect x="60" y="10" width="650" height="300" style="fill:rgb(255,255,0);" > </rect>    <text x="70" y="280" style=" fill: #00000; font-size: 200px; ">'+text+'</text> </g></svg>'
	lista[1]=lista[1].replace("</svg>", y)
	l2=lista[0]+ x +lista[1]
		#print l2
	name2=picturename.split(".")[0]
	file3=open(name2+"v2.svg", "w+r")
	file3.write(l2)
	file3.close()
