import qrcode

UpiId = input("Enter your Upi Id : ")

phonepe_Url = f"upi://pay?pa={UpiId}&pn=Recipient%20Name&mc=1234"
paytm_Url = f"upi://pay?pa={UpiId}&pn=Recipient%20Name&mc=1234"
googlepay_Url = f"upi://pay?pa={UpiId}&pn=Recipient%20Name&mc=1234"


phonepe_qr = qrcode.make(phonepe_Url)
paytm_qr = qrcode.make(paytm_Url)
googlepay_qr = qrcode.make(googlepay_Url)


phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")


phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()