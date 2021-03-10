# from num2words import num2words
# def say(number):
#   if number < 0:
#     raise ValueError("error")
#   if number > 999_999_999_999:
#     raise ValueError("error")
#   return num2words(number).replace(" and","").replace(",","")
# print(num2words(14))


def say(number):
  word = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight',
         9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 
         16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 
         50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
  words = None
  if -1 <number <= 999:
    if number < 100:
      if number < 21 or number % 10 == 0:
        return word[number]
      elif number / 10 != 0:
        return word[number // 10 * 10] + '-' + word[number % 10]
    else:
      if number % 100 == 0:
        return word[number // 100] + ' hundred'
      else:
        return word[number // 100] + ' hundred ' + say(number % 100)

  elif 999 < number <= 999999:
    if number % 1000 == 0:
      words = say(number // 1000) + ' thousand'
    else:
      # print(say(number // 1000), "thousand" ,say(number % 1000))
      words = say(number // 1000) + ' thousand ' + say(number % 1000) 

  elif 999999 < number <= 999999999:
    if number % 1000000 == 0:
      words = say(number // 1000000) + ' million'
    else:
      # print(say(number // 1000000), "million" ,say(number % 1000000))
      words = say(number // 1000000) + ' million ' + say(number % 1000000) 

  elif 999999999 < number <= 999999999999:
    if number % 1000000000 == 0:
      words = say(number // 1000000000) + ' billion'
    else:
      # print(say(number // 1000000000), "billion" ,say(number % 1000000000))
      words = say(number // 1000000000) + ' billion ' + say(number % 1000000000)          

  else:    
    raise ValueError("error")
  return words
        
print(say(987654321123))

