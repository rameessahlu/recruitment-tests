$_input = Read-Host 'Please enter a input text: '

$AlphabetCount = @{}

Function Get-MostCommonlyOccuringAlphabet
{
	for ($i = 0; $i -lt $_input.length; $i++)
	{
		if($_input[$i] -ne "")
		{
			$character = $_input[$i] -join ""
			if($AlphabetCount.ContainsKey($character))
			{
				$AlphabetCount.Set_Item($character, $AlphabetCount[$character] + 1)
			}
			else
			{
				$AlphabetCount.Add($character, 1)
			}
		}
	}
	$MostCommonlyOccuringAlphabet = ""
	$LargestCount = 0
	$AlphabetCount.keys | ForEach-Object {
		if($($AlphabetCount[$_]) -gt $LargestCount){
			$MostCommonlyOccuringAlphabet = $_
			$LargestCount = $($AlphabetCount[$_])
		}
	}
	Write-Output $LargestCount
}


#Output the number of readable characters in the input text.
Write-Output 'Number of readable characters in the input text: '$_input.length

#Output the number of words in the input text.
Write-Output 'Number of words in the input text: '$_input.split(' ').length

#Output the number of alphabets in the input text.
$alphabets_count = $_input | Measure-Object -Character -IgnoreWhiteSpace
Write-Output 'Number of words in the input text: ' $alphabets_count

#No of times the most commonly occurring alphabet occurs
Write-Output 'No of times the most commonly occurring alphabet occurs :'
Get-MostCommonlyOccuringAlphabet