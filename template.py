import os

#Joins the directories in different os like linux or windows.i.e data/raw
dirs=[
	os.path.join("data","raw"),
	os.path.join("data","processed"),
	"notebooks",
	"saved_models",
	"src" 
]

for dir in dirs:
	os.makedirs(dir,exist_ok=True)
	#Create an empty gitkeep file if it doesn't exist . Otherwise it creates one.
	with open(os.path.join(dir,".gitkeep"),"w") as f:
		pass
	
files=[
	"dvc.yaml",
	"params.yaml"
	"gitignore",
	os.path.join("src","__init__py"),
]

for file in files:
	with open(file,"w") as f:
		pass