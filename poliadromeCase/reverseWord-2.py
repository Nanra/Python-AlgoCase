def reverse(word):
  wordReverse = ""
  frame = '*' * 30
  for i in word: 
    wordReverse = i + wordReverse
    # print wordReverse
    # print '\n'

  if word.lower() == wordReverse.lower():
      print frame
      note = 'Wordnya Sama'
      print 'Palindrome : True'
      print 'Plain Word : ' + word
      print 'Word Reversed : ' + wordReverse
      print frame
  else:
      print frame
      note = 'Word Tidak Sama'
      print 'Palindrome : False'
      print 'Plain Word : ' + word
      print 'Word Reversed : ' + wordReverse
      print frame
  return 'Finished'

reverse('OPO')
