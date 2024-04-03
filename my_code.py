def fix_phone_num(phone_num_to_fix):
  # given "5125558823". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:2] # 512 (first three digits)
  three_part = phone_num_to_fix[3:5] # 555 (next three digits)
  four_part = phone_num_to_fix[6:9] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert test_fix_phone_num("5125558823") == '(512) 555 8823'
