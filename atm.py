class ATM(object):
    def _init_(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
    def cashWithdrawal(self):
        print("withdraw")
    def BalanceEnquiry(self):
        print("enquired")

bankers = ATM(1243678251754123,3245)

print(bankers.cashWithdrawal)
print(bankers.BalanceEnquiry)
