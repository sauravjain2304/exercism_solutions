def rebase(input_base, digits, output_base):
  if input_base < 2 or output_base < 2:
    raise ValueError("error")
  s = 0
  for d in digits:
    print(d)
    if d >= input_base or d < 0:
      raise ValueError("error")
    s = s * input_base + d
    print(s)
  r = []
  if not s:
    return [0]
  while s:
    d = s % output_base
    r.append(d)
    s //= output_base
    print(r)
  return r[::-1]
print(rebase(97, [3, 46, 60], 73))