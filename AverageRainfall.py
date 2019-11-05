Years=int(input('How many years of worth of rainfall are you checking? '))
MONTHS=Years*12
for time in range(Years):
	TotalRainfall=0.0
	TotalMonths=0.0
	print('This is the result for the', time + 1, 'year')
	for month in range(MONTHS):
		print('This is for', month +1)
		MonthlyRainfall=float(input(''))
		TotalRainfall+=MonthlyRainfall
		TotalMonths+=month
	AverageRainfall= TotalRainfall/ TotalMonths
	print(MONTHS)
	print('The total amount of rainfall for {0} is {}: ',Years,TotalRainfall)
	print('The average rainfall per month is', AverageRainfall)
	print()


