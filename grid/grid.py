from tkinter import*
tunn=Tk()
#Päevad
Label(text="           ").grid(row=0,column=0)
Label(text="Esmaspäev").grid(row=1,column=0)
Label(text="Teisipäev").grid(row=2,column=0)
Label(text="Kolmapäev").grid(row=3,column=0)
Label(text="Neljapäev").grid(row=4,column=0)
Label(text="Reede").grid(row=5,column=0)
#Tunnid
Label(text="0").grid(row=0,column=1)
Label(text="1").grid(row=0,column=2)
Label(text="2").grid(row=0,column=3)
Label(text="3").grid(row=0,column=4)
Label(text="4").grid(row=0,column=5)
Label(text="5").grid(row=0,column=6)
Label(text="6").grid(row=0,column=7)
Label(text="7").grid(row=0,column=8)
Label(text="8").grid(row=0,column=9)
Label(text="9").grid(row=0,column=10)
Label(text="10").grid(row=0,column=11)
#Esmaspäev
Label(text="Eesti keel\n Tugiõpe",bg="Grey").grid(row=1,column=2)
Label(text="Logistikateenused",bg="green").grid(row=1,column=3,columnspan=2)
Label(text="Matemaatika",bg="pink").grid(row=1,column=5)
Label(text="Matemaatika",bg="pink").grid(row=1,column=6)
Label(text="           ").grid(row=1,column=7)
Label(text="Keel ja kirjandus",bg="Lightgreen").grid(row=1,column=8)
Label(text="Keel ja kirjandus",bg="Lightgreen").grid(row=1,column=9)
Label(text="Matemaatika\n Tugiõpe",bg="pink").grid(row=1,column=10)
#Teisipäev
Label(text="Keemia\n Tugiõpe",bg="purple").grid(row=2,column=2)
Label(text="Programmeerimise\n alused",bg="Lightblue").grid(row=2,column=3,columnspan=3)
Label(text="           ").grid(row=2,column=6)
Label(text="Füüsika",bg="pink").grid(row=2,column=7,columnspan=2)
#Kolmapäev
Label(text="Inglise keel\n Tugiõpe",bg="pink").grid(row=3,column=2)
Label(text="Kunstained",bg="purple").grid(row=3,column=3,columnspan=2)
Label(text="           ").grid(row=3,column=5)
Label(text="Kehaline kasvatus",bg="purple").grid(row=3,column=6,columnspan=2)
#Neljapäev
Label(text="Logistikateenused",bg="green").grid(row=4,column=2,columnspan=2)
Label(text="           ").grid(row=4,column=4)
Label(text="Programmeerimise\n alused",bg="Lightblue").grid(row=4,column=5,columnspan=2)
Label(text="Arenduskeskkonna",bg="red").grid(row=4,column=7,columnspan=2)
Label(text="Eesti keel",bg="grey").grid(row=4,column=9)
Label(text="Eesti keel",bg="grey").grid(row=4,column=10)
#Reede
Label(text="Arenduskeskkonna",bg="red").grid(row=5,column=2,columnspan=2)
Label(text="Programmeerimise alused",bg="Lightblue").grid(row=5,column=4,columnspan=5)

Label(text="Inglise keel",bg="lightgreen").grid(row=5,column=9)
Label(text="Inglise keel",bg="Lightgreen").grid(row=5,column=10)




















tunn.mainloop()
