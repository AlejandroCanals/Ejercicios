"""
1.
Pregunta 1
The check_web_address function checks if the text passed qualifies as a top-level web address, 
meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores),
 as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com",
   ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, 
beginning and end-of-line characters, and character classes.

"""


import re
def check_web_address(text):
  pattern = r"\w\.[A-Za-z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True



"""
Pregunta 2
The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, 
with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, 
in upper or lower case. Fill in the regular expression to do that.
 How many of the concepts that you just learned can you use here?
"""

import re
def check_time(text):
  pattern = r'^(1[0-2]|[1-9]):([0-5][0-9])\s?(AM|PM|am|pm)$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

"""
The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. 
For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication"
 should return True since (IM) satisfies the match conditions." 
Fill in the regular expression in this function: 
"""

import re
def contains_acronym(text):
  pattern = r'\(([A-Z0-9][A-Za-z0-9]*)\)'

  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

"""
6.
Pregunta 6
An intern implemented a zip code checker, but it works only with five-digit zip codes. Your task is to update the checker 
so that it includes all nine digits of the zip code; the leading five digits and the optional four after the hyphen. The zip code needs to be preceded by at least one space, and cannot be at the start of the text. 
Update the regular expression.
"""

import re

def correct_function(text):
  result = re.search(r'\s\d{5}(?:-\d{4})?\b', text)
  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False


"""
Pregunta 1
You’re working with a CSV file that contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains
 U.S. phone numbers and needs to be modified to the international format, with "+1-" in front of the phone number. The rest of the phone number should not change
 Fill in the regular expression, using groups, to use the transform_record function to do that.
"""


"""
Pregunta 2

The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
"""

import re
def multi_vowel_words(text):
  pattern = r'\b\w*[aeiou]{3,}\w*\b'
  result = re.findall(pattern, text, re.IGNORECASE)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

"""
4.
Pregunta 4
The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) 
and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark
 embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single
   comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 

"""

import re
def transform_comments(line_of_code):
    
  result = re.sub(r'\s*#+', ' //', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


"""
The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), 
and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.


"""

import re
def convert_phone_number(phone):

  result = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', phone)

  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))


"""
3.
Pregunta 3
You are reading an article that contains website urls in the format https://www.website-domain.com. You’d like to extract the complete urls from the text automatically,
 instead of copying and pasting them by hand. 

Complete the function find_url to extract all encrypted websites that begin with https:// and end with any top level domain, such as .org, .com, or .co from the text.


"""

def find_url(website):
 pattern = r'https://[^\s/$.?#].[^\s]*[a-zA-Z0-9]' #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. Then, visit https://www.python.org/ to learn more about Python. ")) # Should return ['https://www.coursera.com', 'https://www.python.org']
print(find_url("You can find anything on https://www.google.com!")) # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!")) # Should return []
print(find_url("Check out python.org!")) # Should return []

"""
Pregunta 4
You’re working with a dataset on capital cities around the world. This dataset includes a field that contains information on both city and country.
 You’d like to separate this field into two fields, a city field and a country field. In the current field, city and country are separated by either a comma or a period. 
Complete the function parse_city_country to split city and country into two strings and return only the city.
"""
def parse_city_country(text):
  pattern = r'[,.]\s*' #enter the regex pattern here
  result = re.split(pattern, text) #enter the re method  here
  if len(result) != 2:
    return ""
  return result[0]#return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank
"""
Pregunta 5
A company uses Product ID numbers to identify each product line it makes. Each product ID starts with 4 digits, followed by a hyphen (-), followed by two capital letters, 
followed by a hyphen (-), followed by two more digits, in the format 1234-AB-12. The manufacturing team records information about the production of each product line daily. 

You want to extract the product ID numbers of one of these product lines, which begins with a 1. The other characters in the product ID can be any digit or variable,
 as long as they follow the product ID format described above. Complete the following code so the find_productID function returns all product ID numbers that match the product of interest. 
"""
def find_productID(report):
  pattern = r'\b1\d{3}-[A-Z]{2}-\d{2}\b' #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result
  
print(find_productID("Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30")) # Should return ['1234-AB-30']
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29.")) # Should return ['1234-AB-30', '1678-XZ-11', '1561-CD-57']
