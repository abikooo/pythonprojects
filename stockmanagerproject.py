from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Stock_Management_Systems:

    def __init__(self, root):
        self.root = root
        self.root.title("Stock Management Systems")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        #Frame

        MainFrame = Frame(self.root, bd = 20, width = 1350, height = 700, bg = 'white', padx = 200, relief = RIDGE)
        MainFrame.grid()
        WidgetFrame = Frame(MainFrame, bd = 10, width = 800, height = 600, bg = 'blue',pady = 2, padx = 10, relief = RIDGE)
        WidgetFrame.pack(side = LEFT)

        #Subframes

        WidgetFrame0 = Frame(WidgetFrame, bd = 5, width = 700, height = 155, bg = 'blue', padx = 5, relief = RIDGE)
        WidgetFrame0.grid(row = 0, column = 0)
        WidgetFrame1 = Frame(WidgetFrame, bd = 5, width = 700, height = 155, bg = 'blue', padx = 5, relief = RIDGE)
        WidgetFrame1.grid(row = 1, column = 0)
        WidgetFrame2 = Frame(WidgetFrame, bd = 5, width = 700, height = 155, bg = 'blue', padx = 5, relief = RIDGE)
        WidgetFrame2.grid(row = 2, column = 0)
        WidgetFrame3 = Frame(WidgetFrame, bd = 5, width = 700, height = 155, bg = 'blue', padx = 5, relief = RIDGE)
        WidgetFrame3.grid(row = 3, column = 0)

        #Variables

        self.ProdCode = StringVar()
        self.ProdType = StringVar()
        self.NoDays = StringVar()
        self.CostPDay = StringVar()
        self.CreLimit = StringVar()
        self.CreCheck = StringVar()
        self.SettDueDay = StringVar()
        self.PaymentD = StringVar()
        self.Discount = StringVar()
        self.Deposit = StringVar()
        self.PayDueDate = StringVar()
        self.PaymentM = StringVar()

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.Tax = StringVar()
        self.SubTotal = StringVar()
        self.Total = StringVar()
        self.Receipt_Ref = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Stock Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.ProdCode.set("")
            self.ProdType.set("")
            self.NoDays.set("0")
            self.CostPDay.set("")
            self.CreLimit.set("")
            self.CreCheck.set("")
            self.SettDueDay.set("")
            self.PaymentD.set("")
            self.Discount.set("")
            self.Deposit.set("")
            self.PayDueDate.set("")
            self.PaymentM.  set("")
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.Tax.set("")
            self.SubTotal.set("")
            self.Total.set("")

            self.txtInfo0.delete("1.0", END)
            self.txtInfo1.delete("1.0", END)
            self.txtInfo2.delete("1.0", END)
            self.txtInfo3.delete("1.0", END)
            return



        def checkCredit():
            if self.var1.get() == 1:
                self.txtInfo0.insert(END, "Customer's Check Credit Approved")
            elif self.var1.get() == 0:
                self.txtInfo0.delete("1.0", END)

        def TermAgreed():
            if (self.var2.get() == 1):
                self.txtInfo1.insert(END, "Terms Agreed ")
            elif self.var2.get() == 0:
                self.txtInfo1.delete("1.0", END)

        def AcctOnHold():
            if (self.var3.get() == 1):
                self.txtInfo2.insert(END, "Customer's Account On Hold")
            elif self.var3.get() == 0:
                self.txtInfo2.delete("1.0", END)

        def RestrictedMails():
            if (self.var4.get() == 1):
                self.txtInfo3.insert(END, "Restricted Mails for Customer")
            elif self.var4.get() == 0:
                self.txtInfo3.delete("1.0", END)

        def Product(evt):
            values = str(self.cboProdType.get())
            pType = values

            if pType == "Car":
                self.ProdCode.set("CAR5436")
                self.CostPDay.set("£12")
                self.CreCheck.set("No")
                self.SettDueDay.set("12")
                self.PaymentD.set("No")
                self.Deposit.set("No")
                self.PayDueDate.set("12")
                self.PaymentM.set("Cash")

            elif pType == "Van":
                self.ProdCode.set("VAN775")
                self.CostPDay.set("£19")
                self.CreCheck.set("No")
                self.SettDueDay.set("19")
                self.PaymentD.set("No")
                self.Deposit.set("No")
                self.PayDueDate.set("19")
                self.PaymentM.set("Cash")

            elif pType == "Minibus":
                self.ProdCode.set("MINI007")
                self.CostPDay.set("£21")
                self.CreCheck.set("No")
                self.SettDueDay.set("21")
                self.PaymentD.set("No")
                self.Deposit.set("No")
                self.PayDueDate.set("21")
                self.PaymentM.set("Cash")

            elif pType == "Truck":
                self.ProdCode.set("TRK7483")
                self.CostPDay.set("£15")
                self.CreCheck.set("No")
                self.SettDueDay.set("15")
                self.PaymentD.set("No")
                self.Deposit.set("No")
                self.PayDueDate.set("25")
                self.PaymentM.set("Cash")

        def NoofDays(evt):
            values = str(self.cboNoDays.get())
            NDays = values
            if NDays == "1-30":
                self.SettDueDay.set(30)
                self.CreLimit.set("£150")
                self.Discount.set("5%")

            elif (NDays == "31-90"):
                self.SettDueDay.set(90)
                self.CreLimit.set("£200")
                self.Discount.set("10%")

            elif (NDays == "91-270"):
                self.SettDueDay.set(270)
                self.CreLimit.set("£250")
                self.Discount.set("15%")

            elif (NDays == "271-365"):
                self.SettDueDay.set(365)
                self.CreLimit.set("£300")
                self.Discount.set("20%")

            elif(NDays == "0" or NDays == ""):
                messagebox.showinfo("Zero Selected", "You choose zero?")
                Reset()

        def TotalCost():
            n = float(self.PayDueDate.get())
            s = float(self.SettDueDay.get())
            price = (n * s)
            ST = "£" + str('%.2f' % price)
            iTax = "£", str('%.2f'%((price) * 0.15))
            self.Tax.set(iTax)
            self.SubTotal.set(ST)
            TC = "£",str('%.2f' % (((price) * 0.15) +price))
            self.Total.set(TC)

        #WidgetFrame0

        self.lblProdType = Label(WidgetFrame0, font = ('arial', 18, 'bold'), text = "Product Type:",padx = 2,pady = 16, bg = 'gainsboro')
        self.lblProdType.grid(row = 0, column = 0, sticky = W)

        self.cboProdType = ttk.Combobox(WidgetFrame0,textvariable = self.ProdType, state = 'readonly',
                                        font = ('arial',18,'bold'),width =19)
        self.cboProdType.bind("<<ComboboxSelected>>", Product)
        self.cboProdType['value'] = ('','Car','Van','Minibus','Truck')
        self.cboProdType.current(0)
        self.cboProdType.grid(row = 0,column = 1)

        self.lblNoDays = Label(WidgetFrame0, font=('arial',18,'bold'),text = 'No of Days:', padx = 2, pady = 2, bg = 'gainsboro')
        self.lblNoDays.grid(row = 0, column = 2,sticky = W)

        self.cboNoDays = ttk.Combobox(WidgetFrame0 ,textvariable = self.NoDays, state = 'readonly',
                                      font = ('arial',18,'bold'),width = 19)
        self.cboNoDays.bind("<<ComboboxSelected>>", NoofDays)
        self.cboNoDays['value'] = ('0','1-30','31-90', '91-270','271-365')
        self.cboNoDays.current(0)
        self.cboNoDays.grid(row = 0, column = 3)

        self.lblProdCode = Label(WidgetFrame0, font=('arial',16,'bold'),text = 'Product Code: ',padx = 5,pady = 16, bg = 'gainsboro')
        self.lblProdCode.grid(row = 1,column = 0, sticky = W)

        self.txtProdCode = Entry(WidgetFrame0,textvariable = self.ProdCode,font=('arial',16,'bold'),bd = 8,
        fg = 'black',width=22,justify=LEFT).grid(row=1,column=1)

        self.lblProdCode = Label(WidgetFrame0,font=('arial',16,'bold'),text='Product Price:',padx=1,pady=2,bg='gainsboro')
        self.lblProdCode.grid(row=1,column=2,sticky=W)

        self.txtCostPDay = Entry(WidgetFrame0,textvariable=self.CostPDay,font=('arial',16,'bold'),bd=10,fg='black',width=21,justify=LEFT).grid(row=1,column=3)

        #Widget Frame1
        self.lblCreLimit = Label(WidgetFrame1,font=('arial',18,'bold'),text = "CreditLimit:",padx=2,pady=2,bg="gainsboro")
        self.lblCreLimit .grid(row=0,column=0,sticky=W)

        self.cboCreLimit=ttk.Combobox(WidgetFrame1,textvariable=self.CreLimit,state='readonly',font=('arial',18,'bold'),width=18)
        self.cboCreLimit ['value']=('','Select an option','$150','$200','$250','$300')
        self.cboCreLimit.current(0)
        self.cboCreLimit.grid(row=0,column=1,pady=2)

        self.lblCreCheck=Label(WidgetFrame1,font=('arial',18,'bold'),text="Credit Check:",padx=2,pady=2,bg="gainsboro")
        self.lblCreCheck.grid(row=0,column=2,sticky=W)

        self.cboCreCheck=ttk.Combobox(WidgetFrame1,textvariable=self.CreCheck,state='readonly',font=('arial',18,'bold'),width=18)

        self.cboCreCheck['value']=('','Select an option','Yes','No')
        self.cboCreCheck.current(0)
        self.cboCreCheck.grid(row=0,column=3,pady=2)

        self.lblSettDueDay = Label(WidgetFrame1,font=('arial',18,'bold'),text="Sett.Due:",padx=2,pady=2,bg='gainsboro')
        self.lblSettDueDay.grid(row=1,column=0,sticky=W)

        self.txtSettDueDay=Entry(WidgetFrame1,textvariable=self.SettDueDay,font=('arial',16,'bold'),bd=2,fg="black",width=20,justify=LEFT).grid(row=1,column=1)

        self.lblPaymentD=Label(WidgetFrame1,font=('arial',18,'bold'),text='Payment Due:',padx=1,pady=2,bg="gainsboro")
        self.lblPaymentD.grid(row=1,column=2,sticky=W)
        self.cboPaymentD=ttk.Combobox(WidgetFrame1,textvariable=self.PaymentD,state='readonly',font=('arial',18,'bold'),width=18)
        self.cboPaymentD['value']=('','Select an option','Yes','No')
        self.cboPaymentD.current(0)
        self.cboPaymentD.grid(row=1,column=3,pady=2)

        self.lblDiscount=Label(WidgetFrame1,font=('arial',18,'bold'),text="Discount:",padx=1,pady=2,bg="gainsboro")
        self.lblDiscount.grid(row=2,column=0,sticky=W)

        self.cboDiscount=ttk.Combobox(WidgetFrame1,textvariable=self.Discount,state='readonly',font=('arial',18,'bold'),width=18)
        self.cboDiscount['value']=('0%','5%','10%','15%','20%')
        self.cboDiscount.current(0)
        self.cboDiscount.grid(row=2,column=1,pady=2)

        self.lblDeposit=Label(WidgetFrame1,font=('arial',18,'bold'),text='Deposit:',padx=1,pady=2,bg='gainsboro')
        self.lblDeposit.grid(row=2,column=2,sticky=W)

        self.cboDeposit=ttk.Combobox(WidgetFrame1,textvariable=self.Deposit,state='readonly',font=('arial',18,'bold'),width=18)
        self.cboDeposit['value']=('', 'Select an option','Yes','No')
        self.cboDeposit.current(0)
        self.cboDeposit.grid(row=2,column=3,pady=2)


        self.lblPayDueDate=Label(WidgetFrame1,font=('arial',18,'bold'),text="Pay Day Due:",padx=1,pady=2,bg="gainsboro")
        self.lblPayDueDate.grid(row=3,column=0,sticky=W)

        self.txtPayDueDate = Entry(WidgetFrame1,textvariable=self.PayDueDate,font=('arial',16,'bold'),bd=2,fg='black',width=20,justify=LEFT).grid(row=3,column=1)

        self.lblPaymentM = Label(WidgetFrame1,font=('arial',18,'bold'),text="Payment Method:",padx=0,pady=4,bg='gainsboro')
        self.lblPaymentM.grid(row=3,column=2,sticky=W)

        self.cboPaymentM=ttk.Combobox(WidgetFrame1,textvariable=self.PaymentM,state='readonly',font=('arial',18,'bold'),width=18)
        self.cboPaymentM['value']=('','Select an option','Cash','Visa Card','MasterCard')
        self.cboPaymentM.current(0)
        self.cboPaymentM.grid(row=3,column=3,pady=2)

        #Widget Frame 2

        WidgetFrame2L = Frame(WidgetFrame2,bd=5,width=300,height=160,padx=5,bg='gainsboro',relief=RIDGE)
        WidgetFrame2L.grid(row=0,column=0)
        WidgetFrame2R = Frame(WidgetFrame2,bd=5,width=300,height=160,padx=5,pady=10,bg='gainsboro',relief=RIDGE)
        WidgetFrame2R.grid(row=0,column=1)

        #Widget Frame 2L

        self.chkCheckCredit = Checkbutton(WidgetFrame2L,text="Check Credit ",variable=self.var1,onvalue=1,offvalue=0,
        font=('arial',16,'bold'),bg='gainsboro', command=checkCredit).grid(row=0,column=0,sticky=W)

        self.chkTermAgreed = Checkbutton(WidgetFrame2L,text='Term Agreed',variable=self.var2,onvalue=1,offvalue=0,
        font=('arial',16,'bold'),bg='gainsboro', command=TermAgreed).grid(row=1,column=0,sticky=W)

        self.chkAccountOnHold = Checkbutton(WidgetFrame2L,text='Account On Hold',variable=self.var3,onvalue=1,offvalue=0,
        font=('arial',16,'bold'),bg='gainsboro', command=AcctOnHold).grid(row=2,column=0,sticky=W)

        self.chkRestrictMailing = Checkbutton(WidgetFrame2L,text='Restrict Mailing',variable=self.var4,onvalue=1,offvalue=0,
        font=('arial',16,'bold'),bg='gainsboro', command=RestrictedMails).grid(row=3,column=0,sticky=W)

        self.txtInfo0 = Text(WidgetFrame2L,height=2,width=26,font=('arial',9,'bold'))
        self.txtInfo0.grid(row=0,column=1,pady=2)

        self.txtInfo1=Text(WidgetFrame2L,height=2,width=26,font=('arial',9,'bold'))
        self.txtInfo1.grid(row=1,column=1,pady=2)

        self.txtInfo2=Text(WidgetFrame2L,height=2,width=26,font=('arial',9,'bold'))
        self.txtInfo2.grid(row=2,column=1,pady=2)

        self.txtInfo3=Text(WidgetFrame2L,height=2,width=26,font=('arial',9,'bold'))
        self.txtInfo3.grid(row=3,column=1,pady=2)

        #Widget Frame 2R

        self.lblTax = Label(WidgetFrame2R,font=('arial',18,'bold'),text='Tax',padx=4,pady=1,fg='black',bg='gainsboro')
        self.lblTax.grid(row=0,column=0,sticky=W)
        self.txtTax=Entry(WidgetFrame2R,textvariable=self.Tax,font=('arial',16,'bold'),bd=8,
        fg='black',width=24,justify=LEFT).grid(row=0,column=1,pady=1,padx=1,sticky=W)

        self.lblSubTotal=Label(WidgetFrame2R,font=('arial',18,'bold'),text='Sub Total',padx=4,pady=1,fg="black",bg='gainsboro')
        self.lblSubTotal.grid(row=1,column=0,sticky=W)
        self.txtSubTotal=Entry(WidgetFrame2R,textvariable=self.SubTotal,font=('arial',18,'bold'),bd=8,
        fg="black",width=24,justify=LEFT).grid(row=1,column=1,padx=4)

        self.lblTotal=Label(WidgetFrame2R,font=('arial',18,'bold'),text="Total",padx=4,pady=1,fg="black",bg="gainsboro")
        self.lblTotal.grid(row=2,column=0,sticky=W)
        self.txtSubTotal=Entry(WidgetFrame2R,textvariable=self.Total,font=('arial',16,'bold'),bd=8,
        fg="black",width=24,justify=LEFT).grid(row=2,column=1,pady=1,padx=4)

        #Widget Frame 3, Buttons

        self.btnTotal  = Button(WidgetFrame3, padx=36, pady=2, bd=4, fg="black", font=('arial',20,'bold'), width=12, height=2,
                                bg="gainsboro", text="Total", command = TotalCost).grid(row=0,column=0)

        self.btnReset = Button(WidgetFrame3, padx=33, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=13, height=2,
                                bg="gainsboro", text="Reset", command = Reset).grid(row=0, column=1)

        self.btnExit = Button(WidgetFrame3, padx=36, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=12, height=2,
                                bg="gainsboro", text="Exit", command = iExit).grid(row=0, column=2)


if __name__ == '__main__':
    root = Tk()
    application = Stock_Management_Systems(root)
    root.mainloop()


