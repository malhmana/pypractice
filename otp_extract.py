def extract_otp(message):
  
  """
  takes a message and extracts a six digit OTP out of it.
  """
  otp= ""
  for i in range(len(message)):
      prob_otp= name[i : i + 6]
      print(prob_otp)
      if prob_otp.isdigit() and len(prob_otp) == 6:
          otp+= prob_otp
  return otp
