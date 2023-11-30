import pandas as pd

df = pd.read_json('')  # colocar o arq entre aspas

print(df.to_string())  #  mostra todos os dados (forma de leitura dos arq)


data = {
	"TestCases" : 
		[
			{
			"DestTestcaseName" : <test name> : string,
			"SourceTestcaseName" : <test name> : string,
			"TestEndTime" : <time stamp> : string,
			"TestStartTime" : <time stamp>, : string,
			"Results" :  [ <each test result> : object]
			} ...
		],
		"IOUnitIDs" : 
			{
			<compilation unit ID> : <displayed compilation unit name> : string,
			...
			}
}

df = pd.DataFrame(data)
print(df)