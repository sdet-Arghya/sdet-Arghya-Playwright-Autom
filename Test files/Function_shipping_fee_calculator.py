def shipping_fee(is_prime):
   if is_prime == 'yes':
       message = "shipping is free"
   elif is_prime == 'no':
       message = 'fee is 5 $'
   else:
       message = 'Give valid input as yes or no'
   return message
prime_status = input('Is the customer prime?\n')
result = shipping_fee(prime_status)
print(result)