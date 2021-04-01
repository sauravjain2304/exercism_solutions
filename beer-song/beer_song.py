def recite(start, take=1):
  song = []
  end = start - take + 1
  for n in range(start, start - take, -1):
    if n > 2:
      song.append("{} bottles of beer on the wall, {} bottles of beer.".format(n, n))
      song.append("Take one down and pass it around, {} bottles of beer on the wall.".format(n - 1))
      if take > 1 and n > end:
        song.append("")
    elif n == 2:
      song.append("2 bottles of beer on the wall, 2 bottles of beer.")
      song.append("Take one down and pass it around, 1 bottle of beer on the wall.")
      if take > 1 and n > end:
        song.append("")
    elif n == 1:
      song.append("1 bottle of beer on the wall, 1 bottle of beer.")
      song.append("Take it down and pass it around, no more bottles of beer on the wall.")
      if take > 1 and n > end:
        song.append("")
    else:
      song.append("No more bottles of beer on the wall, no more bottles of beer.")
      song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
  return song
print(recite(99,1))