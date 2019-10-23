

#Place all the code from the previous steps here

import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#findall function to search for non-alphanumeric values
#Wildcard search Range 0-9, A-Z, a-z
results=re.findall("[^a-zA-Z0-9]",lorem_ipsum)

##len function to output to console
print(len(results))

#findall function to get instances of 'sit-amet' or 'sit:amet' 
#literal character search:
occurrance_sit_amet=re.findall (r"sit[:|-]amet",lorem_ipsum)
#len function to putput to console 
print(len(occurrance_sit_amet))

#Replace sit:amet and sit-amet with sit amet using global find-and-replace operation
#Assign the outcome to a variable named 'replace_results'
replace_results=re.sub(r"sit[:|-]amet",'sit amet',lorem_ipsum)

#Using the findall function, get all of the instances of 'sit amet' in the string assigned to 'replace_results'
occurrance_sit_amet=re.findall("sit amet",replace_results)

#Output to the console, the number of sit amet occurrances.
print(len(occurrance_sit_amet))
