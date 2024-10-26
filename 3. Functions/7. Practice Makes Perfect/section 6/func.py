def hide(card_number: str):
  firstPiece = card_number[:2]
  blurred = "XXXXXXXXXXX"
  secondPiece = card_number[-4:]

  return firstPiece + blurred + secondPiece