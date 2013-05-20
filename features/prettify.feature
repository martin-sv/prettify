Feature: Truncate and prettify numbers

Scenario Outline: Truncate and prettify
		Given we choose "<number>" as an input number
		When we simplify it
		Then we should get the "<answer>" as result
	
	Examples: 
	| number          | answer |
	| 185687231.1525  | 185.6M |
	| 1000000         | 1M     |
	| 2500000.34      | 2.5M   |
	| 532             | 532    |
	| 1123456789      | 1.1B   |
	| 2000020.1       | 2.0M   |
    | 2000000.00001   | 2.0M   |
    | 2000000         | 2M     |
    | 1234567891234   | 1.2T   |
    | 1000000010000   | 1.0T   |
    | 15532.1         | 1|
