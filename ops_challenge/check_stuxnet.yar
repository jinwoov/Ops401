// Rule that will check for the Stuxnet virus

rule Check_Stuxnet_virus
{
	meta: 
		Author = "Jin Kim"
		Description = "Checking for infamouse Stuxnet source code snippet, if present this will catch it."
	
	// Referencing the source code to see if the keywords are in the code
	strings: 
		$word1 = "Infected"
		$word2 = "PLT"
		$word3 = "plt"
		$word4 = "network*"
	
	/*
	if the infected is in the source code it will check for additional keywords, however if there is plt, 
	then we can assume that this code relates to Stuxnet
	*/
	condition:
		2 of ($word*) or
		$word2 or
		$word3
}