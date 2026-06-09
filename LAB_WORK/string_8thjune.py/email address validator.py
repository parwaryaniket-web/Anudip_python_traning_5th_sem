'''
6. Email Address Validator 
Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  
Sample Output 
Email: rahul.sharma2026@gmail.com 
 
Username: rahul.sharma2026 
Domain: gmail 
Extension: com 
 
Digits Found: 4 
Special Characters Found: 2 
 
Email Status: Valid
'''
# -----------------------------------------
# Email Address Validator
# -----------------------------------------

# Store the email address
email = "rahul.sharma2026@gmail.com"

# Display the email
print("Email:", email)

# -----------------------------------------
# Check if exactly one '@' is present
# -----------------------------------------

if email.count("@") == 1:

    # Split email into username and domain part
    parts = email.split("@")

    # Extract username (before @)
    username = parts[0]

    # Extract domain section (after @)
    domain_section = parts[1]

    # -----------------------------------------
    # Check if domain section contains '.'
    # Example: gmail.com
    # -----------------------------------------

    if "." in domain_section:

        # Split domain section into domain and extension
        domain_parts = domain_section.split(".")

        # Extract domain name
        domain = domain_parts[0]

        # Extract extension
        extension = domain_parts[-1]

        # -----------------------------------------
        # Count digits in username
        # -----------------------------------------

        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # -----------------------------------------
        # Count special characters in email
        # Special characters are characters
        # that are not letters or digits
        # -----------------------------------------

        special_count = 0

        for ch in email:
            if not ch.isalnum():
                special_count += 1

        # -----------------------------------------
        # Email is valid
        # -----------------------------------------

        status = "Valid"

    else:
        status = "Invalid"

else:
    status = "Invalid"

# -----------------------------------------
# Display Results
# -----------------------------------------

if status == "Valid":

    print("\nUsername:", username)

    print("Domain:", domain)

    print("Extension:", extension)

    print("\nDigits Found:", digit_count)

    print("Special Characters Found:", special_count)

    print("\nEmail Status:", status)

else:
    print("\nEmail Status:", status)