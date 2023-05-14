"# About" 
Python project which aimed for comparing two CSV files according to the instructions below:
Input -
  1. Path to the first csv file to compare
  2. Path to the second csv file to compare
Output -
String in json format of:
  ● “added” record IDs - records which are found in the first file but not in the second file.
  ● “deleted” record IDs- records which are found in the second csv file and not found in the first csv file.
  ● “changed” record IDs - records which appeared in both csv files but at least one of the values is different.
