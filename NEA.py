import sqlite3
import json
from tkinter import *
from tkinter import messagebox
import datetime
from tkinter import ttk
import ast
import textwrap
from fractions import Fraction




class Display:
    def __init__(self):
        self.choice = 4
        self.window = Tk()
        self.window.geometry("1500x1500")      # this is the size of the window.
        self.window.title("Physics quiz")    #this is the title that will be displayed at the top of the window.
        self.window.configure(bg ="deep sky blue") 

        
             
        while self.choice != 5:
           # self.Header = Label (self.window, text = "Welcome to Alevel Physics Quiz", font =("Helvetica", 24, "bold"),  padx=10,pady=10,fg="black", bg ="deep sky blue")
           # self.Header.pack(pady =5) 
           self.signin()
           self.Tables()
           self.Class2    = Attempt()
           self.window.mainloop()
    def signin (self):
       
        self.frame1            = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
        self.frame1.pack (pady = 20,padx = 100, fill=BOTH,expand=True)
        self.Photo_logo        = PhotoImage(file="shared image (2).png")
        self.logo              = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.frame             = Frame( self.frame1, borderwidth=10,width=0, height=0,bg ="DodgerBlue",pady = 10,padx = 10)  
        self.frame.pack (pady  = 20,padx = 20)         
        self.Username_Label    = Label(self.frame, text = "USERNAME", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")       
        self.Password_Label    = Label(self.frame, text = "PASSWORD", font=("Verdana", 12),width = 12, pady = 10,bg = "orange")      
        self.Username_Entry    = Entry(self.frame,borderwidth=8,font=("Verdana", 14))        
        self.Password_Entry    = Entry(self.frame,borderwidth=8,font=("Verdana", 14) , show = "*") 
        self.ButtonLogin       = Button(self.frame1, text = 'LogIn',borderwidth=8, width = 10, bg = "orange", font = ("Verdana", 12),command =lambda : self.HomePage(self.frame1,self.logo))
        self.ButtonLogin.pack( pady =5, padx = 5)
        self.Username_Label.grid(row = 0, column = 0, pady = 10)
        self.Password_Label .grid(row = 1, column = 0, pady = 10)
        self.Username_Entry.grid(row = 0, column = 1,pady =10)
        self.Password_Entry.grid(row = 1, column = 1,pady = 10)

    def Tables (self):
         self.List_Energy_Questions = [
                                       ["An object of weight 7N is raised from a height of 2m to a height of 8m The change \n in gravitational potential energy is?", "42J. ", "56J. ", "412J.", "549J."],
                                       ["A body of constant mass falls freely due to gravity. The rate of change of momentum \n of the body is equal to its?", "kInetic energy.","Mass.          ", "GPE.           ", "Weight.        "],
                                       ["A suitcase weighing 200N is placed on a weighing scale in a lift. The scale reads \n 180N when the lift is moving.The lift is?"," moving down at a constant velocity.    ", " moving down with a decreasing velocity."," moving up at a constant velocity.      "," moving up with a decreasing velocity.  "],
                                       ["Which of the following is a scalar quantity?", "Velocity.", "Kinetic Energy.", "Force.", "Momentum."],
                                       ["An electric motor of input power 100 W raises a mass of 10 kg vertically at a steady speed\n of 0.5ms^-1. What is the efficiency of the system?", "5%.  ", "12%. ", "50%. ","100%."],
                                       ["The rate of workdone is equal to...",     "Power.   ", "Energy.  ", "Strength.", "Pressure."],
                                       ["The energy of an object due to its position in a gravitational field is?","Kinetic Energy.","Sound Energy.  ","GPE.           ","Gravity.       "],
                                       ["The energy an object possesses due to its motion is?","Kinetic energy.","Work.          ","GPE.           ","Acceleration.  "],
                                       ["The energy transfer when a force moves an object over a distance is?","Power.     ","Work Done. ","Efficiency.","weight.    "],
                                       ["The useful output of a system divided by the total output?","Efficiency.","Upthrust.  ","Force.     ","Tension.   "]
                                       ]
         self.List_Material_Question = [["Which one of the following shows very little strain before reaching its breaking stress?","Brittle.","hard.   ","light.  ","Ductile."],
                                        ["Which law state that the extension of an elastic object will be directly proportional \nto the force applied to it up to the object's limit of proportionality","Newton laws.","Hooke's Law.","Pascal Law. ","Ohm's law.  "],
                                        ["The ratio of stress to strain for a given material is?","Momentum.     ", "power.        ", "stress.      ","Young Modulus."],
                                        ["What is the ratio of an object's extention to its original length. it is\n a rotio of two length and so has no unit","stress.         ","strain.         ","sprint Constant.","Pressure.       "],
                                        ["The changing of an object's shape due to tensile force is?", "Tensil Deformation.","Applied Force.     ","Tension.           ","Workdone.          "],
                                        ["A materail made from polymers is called?","Nylon.    ","polythen. ","Ethylene. ","Polymeric."],
                                        ["If a material can undergo very large extensions without failure it said to be?","Ductile.       ","Extension free.","Flexible.      ","Free.          "],
                                        ["What is the amount of force acting per unit area. its unit is pascal(pa)?","Strain.  ","Pressure.","Stress.  ","Force.   "],
                                        ["The result of two coplanar force acting into an object is?","Compression.","Diffraction.","Joining.    ","Attachment. "],
                                        ["The constant proportionality for the extension of a spring under a force is called?","Elastic constant. ","Spring constant.  ","Force constant.  ","Extensive constant"]
                                       ]
         self.List_Momentum_Question = [["The change of momentum of an object when a force acts on\n it is known as?","Momentum.","Impulse. ","Force.   ","Moment.  "],
                                        ["A collision in which the total kinetic energy before the collision is equal to the\n total kinetic energy after the collision is?","Plastic collision.","Workdone.         ","Elastic collision.","Friction.         "],
                                        ["The product of an object's mass and linear velocity is?","Linear Momentum.","Friction.       ","Acceleration.   ","Mass.           "],
                                        ["The sum of the force acting on an object is equal to\n the rate of change of momentum of the object.","Newton's first law. ","Newton's second law.","Newton's third law  ","Ohm's law           "],
                                        ["An object will remain in it current state of motion,\n unless acted on by a resultant","Newton's first law. ","Newton's second law.","Newton's third law  ","Ohm's law           "],
                                        ["Which law states that every action as an equal\n and opposite reaction?","Newton's first law. ","Newton's second law.","Newton's third law  ","Ohm's law           "],
                                        ["A collision in which the total kinetic energy before the collision is not\n equal the kinetic energy after the collsion is an?","Elastic collision.  ","Linear Momentum.    ","Impulse.            ","Inelastic collision."],
                                        ["Which quantity have the same units as impulse?","Energy.  ","Momentum.","Power.   ","Force.   "],
                                        ["A force of 20N acts on a body for 1 seconds.\n What is the impulse?","20. ","5.  ","10. ","0.5."],
                                        ["The SI unit of momentum is?","joule. ","Newton.","kg.m/s ","Watt  "]
                                       ]
         self.List_Waves_Question = [["Which quantity is conserved when a wave enters a different medium?","Speed     ","Wavelength","Frequency ","Amplitude "],
                                     ["The energy carried by a wave is proportional to ?","Amplitude ","Amplitude²","Frequency ","Frequency²"],
                                     ["In refraction, which quantity remains constant?","Speed     ","Wavelength","Frequency ","Intensity "],
                                     ["When a wave slows on entering a denser medium, wavelength:","Increases   ","Decreases   ","Remains same","Fluctuates  "],
                                     ["Sound is a:","Electromagnetic wave","Transverse wave     ","Longitudinal wave   ","Surface wave       "],
                                     ["A stationary wave has:","Energy transfer      ","Nodes and antinodes ","Constant phase travel","Progressive pattern  "],
                                     ["First harmonic on string means:","Two antinodes","One node     ","One antinode ","No nodes    "],
                                     ["Stationary waves in pipe open at both ends: first harmonic λ =:","2L ","4L ","L/2","L  "],
                                     ["For light, polarization occurs in:","Longitudinal waves","Transverse waves  ","Both              ","Neither           "],
                                     ["Standing waves on a string dissipate energy when:","No damping      ","With damping    ","Amplitude is max","Always          "]
                                    ]
         str_Energy_Question       = json.dumps(self.List_Energy_Questions )
         self.List_Waves_Answer    = ["Frequency ","Amplitude²","Frequency ","Decreases   ","Longitudinal wave   ","Nodes and antinodes ","One antinode ","2L ","Transverse waves  ","With damping    "]
         self.List_Answers         = [ "42J. ","Weight.        "," moving up with a decreasing velocity.  ", "Kinetic Energy.","50%. ","Power.   ","GPE.           ","Kinetic energy.","Work Done. ","Efficiency."]
         self.List_Material_Answer = ["Brittle.","Hooke's Law.","Young Modulus.","strain.         ","Tensil Deformation.","Polymeric.","Ductile.       ","Stress.  ","Compression.","Spring constant.  "]
         self.List_Momentum_Answer = ["Impulse. ","Elastic collision.","Linear Momentum.","Newton's second law.","Newton's first law. ","Newton's third law  ","Inelastic collision.","Momentum.","20. ","kg.m/s "]
         conn                      = sqlite3.connect('Table.db')
         str_List_Answers          = json.dumps(self.List_Answers)
         try:
                 conn.execute("""CREATE TABLE Student
                 (StudentID      INT PRIMARY KEY,
                  StudentFurname  text(20),
                  StudentSurname  text(20),
                  Username        text(20),
                  Password        text(20) )""")
         except:
             pass
         try:
                 conn.execute("INSERT INTO Student VALUES(:StudentID,:StudentFurname,:StudentSurname,:Username,:Password)", {
                     'StudentID'     :  1,
                     'StudentFurname': "mine",
                     'StudentSurname': "Olagoke",
                     'Username'      : "mine",
                     'Password'      : "12"   })
                 conn.commit()
         except:
             pass
         
         try:
                conn.execute("""CREATE TABLE Topic
                (TopicID    INT PRIMARY KEY, 
                TopicName   text(20),
                Questions   text,
                Answer      text
                )""")
         except:
             pass
         try:
                 conn.execute("""CREATE TABLE Completed_Quiz
                 (Quiz_ID     INT PRIMARY KEY,
                  StudentID     text(20),
                  StudentFurname text(20),
                  TopicID        text(20),
                  TopicName      text(20),
                  TotalMark      text(20),
                  Date           DATE
                               )""")
         except:
             pass
         
         try:
                Topic_Name = "Energy"        
                TopicID = 1
                conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                   'TopicID'     :  TopicID,
                   'TopicName'   :  Topic_Name,
                   'Questions'   :  str_Energy_Question ,
                   'Answer'      :  str_List_Answers
               })
         except:
            pass
         try:
               conn.execute("""CREATE TABLE History
                         (HistoryID      INTEGER PRIMARY KEY AUTOINCREMENT,
                         StudentID       text(20),                  
                         TopicID         text(20),
                         TopicName       text(20),
                         TotalMark       text(20),
                         PercentageMark  text(20),
                         Date            DATE
                                        )""")
         except:
              pass
        

         self.str_List_Materail_Question  = json.dumps( self.List_Material_Question)
         self.str_List_Materail_Answer    = json.dumps(  self.List_Material_Answer)
         try:
                conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                            'TopicID'     :  2,
                            'TopicName'   :  "Material" ,
                            'Questions'   :   self.str_List_Materail_Question ,
                            'Answer'      :  self.str_List_Materail_Answer
                        })
         except:
              pass
         self.str_List_Momentum_Question  = json.dumps( self.List_Momentum_Question)
         self.str_List_Momentum_Answer    =json.dumps(self.List_Momentum_Answer)
         try:
                conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                            'TopicID'     :  3,
                            'TopicName'   :  "Momentum" ,
                            'Questions'   :   self.str_List_Momentum_Question ,
                            'Answer'      : self.str_List_Momentum_Answer
                        })
         except:
              pass
         self.str_List_Waves_Question   = json.dumps( self.List_Waves_Question)
         self.str_List_Waves_Answer     =json.dumps(self.List_Waves_Answer)
         try:
                conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                            'TopicID'     :  4,
                            'TopicName'   :  "Waves" ,
                            'Questions'   :   self.str_List_Waves_Question ,
                            'Answer'      : self.str_List_Waves_Answer
                        })
         except:
              pass

         conn.commit()
         conn.close()

     
    
    

        
       
       

    def show_info(self):
         
          #messagebox.showinfo("Information", "Incorrect username or password please try again")
          messagebox.showwarning("Warning", "Incorrect username or password please try again")
 
            

    def HomePage (self, Destroy_current_window,Image):
        self.Username = self.Username_Entry.get()
        self.Password = self.Password_Entry.get()
        self.image    = Image
        conn          = sqlite3.connect("Table.db")
        self.cursor   = conn.execute("SELECT * from Student")
        self.list     = []
        for words in self.cursor:
             for word in words:
                self.list.append(word)
        if self.Username  in self.list:
            if self.Password in self.list:
                Destroy_current_window.destroy()
                self.OptionalMenu()
            else:
                self.image.destroy()
                Destroy_current_window.destroy()
                self.signin()
                self.show_info()
            
        else:
            Destroy_current_window.destroy()
            self.signin()
            self.show_info()    
    def OptionalMenu (self):
       
        self.class3  = Update()
        self.class4 = History()
        self.frame1           = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.frame1.pack(pady = 30,padx = 20, fill=BOTH, expand= True) 
        self.Photo_logo       = PhotoImage(file="shared image (2).png")
        self.logo             = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack   (padx=5,pady=0)
        self.frame2           = Frame(self.frame1,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )       
        self.Button_Update    = Button (self.frame2, text = "Update Questions", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 15 ,command =lambda: self.class3. sign_in_plus( self.window, self.frame1 ))        
        self.Button_History   = Button(self.frame2, text = "history", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 15, command =lambda: self.class4.History_options( self.frame1,self.window))      
        self.Button_Take_Quiz = Button (self.frame2, text = "Take Quiz", borderwidth=8,bg = "orange",font = ("Verdana", 12), command =lambda: self.listbox(self.frame2, self.frame1, self.window),width = 15 )         
        self.button_End       = Button(self.window,text="❌ End",font=("Arial", 9),bg = "orange",command=lambda:self.End(self.window))
        self.button_Home      = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: self.Home(self.frame1,self.window))
        self.frame2.pack (pady = 20,padx = 20)  
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.button_End.place(x=75, y=5, anchor="nw")
        self.Button_Update.pack(pady = 5, padx = 5)
        self.Button_History.pack(pady = 5, padx = 5)
        self.Button_Take_Quiz.pack(pady = 5, padx = 5)


               
        
    def Home (self,old_frame,window):
        self.class3 = Update()
        self.class4 = History()
        self.window2 = window
        self.Old_Frame = old_frame
        self.Old_Frame.destroy()
        
        self.button_Home = Button(self.window2,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: self.Home(self.frame3,self.window2))
        self.button_Home.place(x=5, y=5, anchor="nw")


        self.frame3 = Frame(self.window2, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.frame3.pack (pady = 30,padx = 20, fill=BOTH, expand= True) 
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.frame3,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
   
        self.frame4 = Frame(self.frame3,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
        self.frame4.pack (pady = 20,padx = 20) 
        self.Button_Update = Button (self.frame4, text = "Update Questions", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 15 ,command =lambda: self.class3. sign_in_plus(self.window2,self.frame3))  
        self.Button_Update.pack(pady = 5, padx = 5)
        self.Button_History= Button(self.frame4, text = "history", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 15,command =lambda: self.class4.History_options( self.frame3,self.window2))
        self.Button_History.pack(pady = 5, padx = 5)
        self.Button_Take_Quiz = Button (self.frame4, text = "Take Quiz", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 15 , command =lambda: self.listbox2( self.frame3))  
        self.Button_Take_Quiz.pack(pady = 5, padx = 5)
       
    


        
        
    def listbox (self, current_Frame, outer_frame, window):
        self.window = window
        self.current_Frame = current_Frame
        self.current_Frame.forget()
        self.old_frame= outer_frame
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: self.Home(self.old_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.new_frame= Frame(self.old_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.new_frame.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
        self.listbox = Listbox(self.new_frame, height= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row=1, column= 0,padx=5,pady= 5)
      
        self.topic_label = Label(self.new_frame, text = "Select a Topic and click on the enter button to proceed.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row=0, column= 0,padx=5,pady= 5)
        self.Button_Enter = Button(self.new_frame, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Class2.Display_Question1(self.old_frame, self.new_frame, self.listbox, self.window)) 
        self.Button_Enter.grid(row=2, column= 0,padx=5,pady= 5)
     
    def listbox2 (self,frame):
         self.old_Frame = frame
         self.old_Frame.destroy()
         self.outer_frame = Frame(self.window, borderwidth=10,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
         self.outer_frame.pack (pady = 30,padx = 20, fill=BOTH, expand= True) 
         self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: self.Home( self.outer_frame,self.window))
         self.button_Home.place(x=5, y=5, anchor="nw")
         self.Photo_logo = PhotoImage(file="shared image (2).png")
         self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
         self.logo.pack(padx=5,pady=0)
         self.innerframe = Frame(self.outer_frame , borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
         self.innerframe.pack(pady = 20,padx = 20)
         self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
         self.listbox = Listbox( self.innerframe, height= 5)
         for Words in self.List_of_Topics:
             self.listbox.insert(END, Words)
         self.listbox.grid(row=1, column= 0,padx=5,pady= 5)
         #self.new_frame.pack(padx= 5, pady= 5,expand=True, fill= BOTH)
         self.topic_label = Label( self.innerframe, text = "Select a Topic and click on the enter button to proceed.", font = ("verdana", 9), background = "orange")
         self.topic_label.grid(row=0, column= 0,padx=5,pady= 5)
         self.Button_Enter = Button( self.innerframe, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Class2.Display_Question1( self.outer_frame,  self.innerframe, self.listbox, self.window)) 
         self.Button_Enter.grid(row=2, column= 0,padx=5,pady= 5)
    def End (self,window):
         try:
               self.window = window
               self.window.destroy()
         except:
              pass

    
        

class Attempt:

   
   def listbox2 (self,frame):
         self.old_Frame = frame
         self.old_Frame.destroy()
         self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
         self.outer_frame.pack (pady = 30,padx = 20, fill=BOTH, expand= True) 
         self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self, self.outer_frame,self.window))
         self.button_Home.place(x=5, y=5, anchor="nw")
         self.Photo_logo = PhotoImage(file="shared image (2).png")
         self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
         self.logo.pack(padx=5,pady=0)
         self.innerframe = Frame(self.outer_frame , borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
         self.innerframe.pack(pady = 20,padx = 20)
         self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
         self.listbox = Listbox( self.innerframe, height= 5)
         for Words in self.List_of_Topics:
             self.listbox.insert(END, Words)
         self.listbox.grid(row=1, column= 0,padx=5,pady= 5)
       
         self.topic_label = Label( self.innerframe, text = "Select a Topic and click on the enter button to proceed.", font = ("verdana", 9), background = "orange")
         self.topic_label.grid(row=0, column= 0,padx=5,pady= 5)
         self.Button_Enter = Button( self.innerframe, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Display_Question1( self.outer_frame,  self.innerframe, self.listbox, self.window)) 
         self.Button_Enter.grid(row=2, column= 0,padx=5,pady= 5)

         
   def Display_Question1(self, Current_Frame, Old_Frame, listbox , window):
        self.window =window
        self.selected_indeces = listbox.curselection()
        self.index = self.selected_indeces [0]
        self.value = listbox.get(self.index)
        self.Old_Frame = Old_Frame
        self.selected_Topic = self.value
        self.Background_Frame = Current_Frame
        if self.selected_Topic :
            self.Old_Frame.destroy()
          
            self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self,self.Background_Frame,self.window))
            self.button_Home.place(x=5, y=5, anchor="nw")
            self.New_Frame = Frame(self.Background_Frame,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
            self.New_Frame.pack(padx=10, pady= 5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            conn = sqlite3.connect("Table.db")
            self.TABLE = conn.execute("SELECT * FROM Topic")
            self.Tuple_Table = []
            self.List_Table = []
            self.List_Topic_Answers = []
            self.List_Question = []
            self.List_Selected_Answer = []
            self.counter = 0
            self.Question_and_Answer = []
            for words in self.TABLE:
                self.Tuple_Table.append(words)
            for words in self.Tuple_Table:
                 for words_2 in words:
                       self.List_Table.append(words_2)
            for words in self.List_Table:
                 self.counter = self.counter + 1  
                 if words ==  self.selected_Topic:
                      self.str_Question = self.List_Table[self.counter]
                      self.srt_answer = self.List_Table[self.counter + 1]
            self.List_Topic_Answers = json.loads(self.srt_answer)          
            self.List_Question = json.loads(self.str_Question)
            self.counter2 = 0
            self.Question_and_Answer = self.List_Question[self.counter2]
            self.answer =  self.List_Topic_Answers[self.counter2]
            self.var = StringVar()
            self.var.set(None)
            self.Label_Question = Label(self.New_Frame,bg = "wheat", width= 80, height= 3, font = ("Verdana", 12),text =self.Question_and_Answer[0],padx = 5, pady= 5 )
            self.Label_Question.grid(row= 0, column= 0, columnspan=3, padx= 5, pady= 5,sticky="nsew")
            self.Option_A = Radiobutton(self.New_Frame , bd=10,cursor = "target", width= 35 ,bg = "orange",font = ("Verdana", 12), text=self.Question_and_Answer[1], variable= self.var, value =self.Question_and_Answer[1],padx = 5, pady= 5  )
            self.Option_A.grid(row= 1, column= 1, padx= 20,pady= 5,sticky="nsew")
            self.Option_B = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[2],variable= self.var, value =self.Question_and_Answer[2],padx = 5, pady= 5  )
            self.Option_B.grid(row= 2, column= 1, padx= 20,pady= 5,sticky="nsew")
            self.Option_c = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[3], variable= self.var, value =self.Question_and_Answer[3],padx = 5, pady= 5  )
            self.Option_c.grid(row= 3, column= 1, padx= 20,pady= 5,sticky="nsew")
            self.Option_D = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange", cursor = "target",font = ("Verdana", 12),text=self.Question_and_Answer[4],variable= self.var, value =self.Question_and_Answer[4],padx = 5, pady= 5  )
            self.Option_D.grid(row= 4, column=1, padx= 20,pady= 5,sticky="nsew")
            self.counter2 = 1
            self.button_next = Button(self.New_Frame,width= 7, borderwidth= 7, text= "next", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Dispaly_Question2( self.var,self.counter2,self.List_Selected_Answer,self.Background_Frame))
            self.button_next.grid(row = 5, column= 2, padx=5, pady=5,sticky="nsew")
            self.button_submit = Button(self.New_Frame,width= 7, borderwidth= 7, text= "Submit", bg= "orange", cursor = "target", font = ("Verdana", 12),command= lambda:self.Submit_quiz( self.counter2,self.var, self.List_Selected_Answer,self.answer,self.Background_Frame))
            self.button_submit.grid(row = 5, column= 0, padx=5, pady=5,sticky="nsew")
   def Dispaly_Question2 (self, selected,counter_2, List_Selected_Answer,Old_frame):
        self.class3  = Update()
        self.class4 = History()
        self.Old_Frame = Old_frame
        self.counter= counter_2
        self.List_Selected_Answer = List_Selected_Answer
        self.selected = selected
        self.selected1 = self.selected.get()
        self.List_Selected_Answer.append(self.selected1)
        self.var = StringVar()
        self.var.set(None)
        self.Old_Frame.destroy()
        
        self.outer_frame = Frame(self.window, borderwidth=10,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 30,padx = 20, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self,self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label( self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=0)
        self.New_Frame = Frame(self.outer_frame,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
        self.New_Frame.pack(padx=10, pady= 5)  
        self.answer =  self.List_Topic_Answers[self.counter2]
        self.Question_and_Answer = self.List_Question[self.counter]
        self.Label_Question = Label(self.New_Frame,bg = "wheat", width= 80, height= 3, font = ("Verdana", 12),text =self.Question_and_Answer[0],padx = 5, pady= 5 )
        self.Label_Question.grid(row= 0, column= 0, columnspan=3, padx= 5, pady= 5,sticky="nsew")
        self.Option_A = Radiobutton(self.New_Frame , bd=10,cursor = "target", width= 35 ,bg = "orange",font = ("Verdana", 12), text=self.Question_and_Answer[1], variable= self.var, value =self.Question_and_Answer[1],padx = 5, pady= 5  )
        self.Option_A.grid(row= 1, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_B = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[2],variable= self.var, value =self.Question_and_Answer[2],padx = 5, pady= 5  )
        self.Option_B.grid(row= 2, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_c = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[3], variable= self.var, value =self.Question_and_Answer[3],padx = 5, pady= 5  )
        self.Option_c.grid(row= 3, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_D = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange", cursor = "target",font = ("Verdana", 12),text=self.Question_and_Answer[4],variable= self.var, value =self.Question_and_Answer[4],padx = 5, pady= 5  )
        self.Option_D.grid(row= 4, column=1, padx= 20,pady= 5,sticky="nsew")
        self.counter2 = self.counter + 1
        self.button_next = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Next", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Dispaly_Question2( self.var,self.counter2,self.List_Selected_Answer,self.outer_frame))
        self.button_next.grid(row = 5, column= 2, padx=5, pady=5,sticky="nsew")   
        self.button_submit = Button(self.New_Frame,width= 7, borderwidth= 7, text= "Submit", bg= "orange", cursor = "target", font = ("Verdana", 12),command= lambda:self.Submit_quiz( self.counter2,self.var, self.List_Selected_Answer,self.answer,self.outer_frame))
        self.button_submit.grid(row = 5, column= 0, padx=5, pady=5,sticky="nsew")
        self.Button_finish = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Finish", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Finish_Quiz( self.List_Selected_Answer ,self.var,self.outer_frame ))
        if self.counter2 == len(self.List_Question):
             self.button_next.grid_forget()
             self.Button_finish.grid(row = 5, column= 2, padx=5, pady=5,sticky="nsew")
   def Dispaly_Question3 (self, selected,counter_2, List_Selected_Answer,Old_frame,Button_next):
       
        self.button_next = Button_next
        self.button_next.grid_forget()
        self.Old_Frame = Old_frame
        self.counter= counter_2
        self.List_Selected_Answer = List_Selected_Answer
        self.selected = selected
        self.selected1 = self.selected.get()
        self.List_Selected_Answer.append(self.selected1)
        
        self.var = StringVar()
        self.var.set(None)
        self.answer =  self.List_Topic_Answers[self.counter2]
        self.Question_and_Answer = self.List_Question[self.counter]
        self.Label_Question = Label(self.New_Frame,bg = "wheat", width= 80, height= 3, font = ("Verdana", 12),text =self.Question_and_Answer[0],padx = 5, pady= 5 )
        self.Label_Question.grid(row= 0, column= 0, columnspan=3, padx= 5, pady= 5,sticky="nsew")
        self.Option_A = Radiobutton(self.New_Frame , bd=10,cursor = "target", width= 35 ,bg = "orange",font = ("Verdana", 12), text=self.Question_and_Answer[1], variable= self.var, value =self.Question_and_Answer[1],padx = 5, pady= 5  )
        self.Option_A.grid(row= 1, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_B = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[2],variable= self.var, value =self.Question_and_Answer[2],padx = 5, pady= 5  )
        self.Option_B.grid(row= 2, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_c = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text=self.Question_and_Answer[3], variable= self.var, value =self.Question_and_Answer[3],padx = 5, pady= 5  )
        self.Option_c.grid(row= 3, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_D = Radiobutton(self.New_Frame,width= 35,bd=10,bg = "orange", cursor = "target",font = ("Verdana", 12),text=self.Question_and_Answer[4],variable= self.var, value =self.Question_and_Answer[4],padx = 5, pady= 5  )
        self.Option_D.grid(row= 4, column=1, padx= 20,pady= 5,sticky="nsew")
        self.counter2 = self.counter + 1
        self.button_next = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Next", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Dispaly_Question2( self.var,self.counter2,self.List_Selected_Answer,self.Old_Frame))
        self.button_next.grid(row = 5, column= 2, padx=5, pady=5,sticky="nsew")   
        self.button_submit = Button(self.New_Frame,width= 7, borderwidth= 7, text= "Submit", bg= "orange", cursor = "target", font = ("Verdana", 12),command= lambda:self.Submit_quiz( self.counter2,self.var, self.List_Selected_Answer,self.answer,self.Old_Frame))
        self.button_submit.grid(row = 5, column= 0, padx=5, pady=5,sticky="nsew")
        self.Button_finish = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Finish", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Finish_Quiz( self.List_Selected_Answer ,self.var,self.Old_Frame))
        if self.counter2 == len(self.List_Question):
             self.button_next.grid_forget()
             self.Button_finish.grid(row = 5, column= 2, padx=5, pady=5,sticky="nsew")
             
   def Submit_quiz (self,counter,var,list_answer,answer,frame):
     
        self.old_frame1 = frame
        self.List_Selected_Answer = list_answer
        self.var = var
        self.selected1 = self.var.get()
      
        self.counter = counter - 1
        self.answer =  answer
        self.Question_and_Answer = self.List_Question[self.counter]
        self.Option_A =self.Question_and_Answer[1]
        self.Option_B =self.Question_and_Answer[2]
        self.Option_C =self.Question_and_Answer[3]
        self.Option_D =self.Question_and_Answer[4]
        self.option_A_color = "red"
        self.option_B_color = "red"
        self.option_C_color = "red"
        self.option_D_color = "red"
        if self.Option_A ==  self.answer:
             self.option_A_color = "greenyellow"
        elif self.Option_B ==  self.answer:
             self.option_B_color = "greenyellow"
        elif self.Option_C ==  self.answer:
             self.option_C_color = "greenyellow"
        else:
             self.option_D_color= "greenyellow"
        self.Label_Question = Label(self.New_Frame,bg = "wheat", width= 80, height= 3, font = ("Verdana", 12),text =self.Question_and_Answer[0],padx = 5, pady= 5 )
        self.Label_Question.grid(row= 0, column= 0, columnspan=3, padx= 5, pady= 5,sticky="nsew")
        self.Option_A = Label(self.New_Frame , bd=10, width= 35 ,bg = self.option_A_color,font = ("Verdana", 12), text=self.Option_A,padx = 5, pady= 5  )
        self.Option_A.grid(row= 1, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_B = Label(self.New_Frame,width= 35,bd=10,bg = self.option_B_color,font = ("Verdana", 12), text=self.Option_B,padx = 5, pady= 5  )
        self.Option_B.grid(row= 2, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_c = Label(self.New_Frame,width= 35,bd=10,bg = self.option_C_color,font = ("Verdana", 12), text=self.Option_C,padx = 5, pady= 5  )
        self.Option_c.grid(row= 3, column= 1, padx= 20,pady= 5,sticky="nsew")
        self.Option_D =Label(self.New_Frame,width= 35,bd=10,bg = self.option_D_color,font = ("Verdana", 12),text=self.Option_D,padx = 5, pady= 5  )
        self.Option_D.grid(row= 4, column=1, padx= 20,pady= 5,sticky="nsew")
        self.counter2 = self.counter + 1
        if self.counter2 == len(self.List_Question) :
           self.Button_finish.grid_forget()
           self.button_submit.grid_forget()
           self.Button_finish1 = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Finish", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Finish_Quiz_3( self.List_Selected_Answer ,self.var,self.old_frame1))
           self.Button_finish1.grid(row = 5, column= 1, padx=5, pady=5,sticky="nsew")
        else:
             self.button_submit.grid_forget()
             self.button_next.grid_forget()
             self.button_next1 = Button(self.New_Frame,width= 7, borderwidth= 7,text= "Next", bg= "orange", cursor = "target", font = ("Verdana", 12),command =lambda: self.Dispaly_Question3( self.var,self.counter2,self.List_Selected_Answer,self.old_frame1,self.button_next1))
             self.button_next1.grid(row = 5, column= 1, padx=5, pady=5,sticky="nsew") 
        if self.answer == self.selected1:
              messagebox.showwarning("Information", "Welldone!, your answer was correct ✅ "
              )
        else:
              messagebox.showwarning("Information", "The answer you selected was wrong ❌")
             
             
        
             
        
       
   def Finish_Quiz_3 (self, List_Answer,selected,Old_frame2):
        self.old_frame2 = Old_frame2
        self.old_frame2.destroy()
        self.selected =selected
        self.selected1 = self.selected.get()
        self.List_Answers = List_Answer
        self.List_Answers.append(self.selected1) 
        self.list_All_info= [] 
        self.selected.set('None')       
        self.new_frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
        self.new_frame.pack (pady = 20,padx = 150, fill=BOTH,expand=True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self, self.new_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.Instruct_label = Label( self.new_frame, text = "Enter a username and password that you can remeber",pady = 10, bg = "orange",font=("Verdana", 18   ))
        self.Instruct_label.pack()
        self.inner_frame =Frame (self.new_frame,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
        self.inner_frame.pack(padx=10, pady= 20)
        self.label_FirstName = Label(self.inner_frame,text="FirstName",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_FirstName.grid(row = 0, column = 0, pady = 10)
        self.FirstName_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14) ) 
        self.FirstName_Entry.grid(row = 0, column = 1,pady = 10)
        self.label_Surname = Label(self.inner_frame,text="Surname",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Surname.grid(row = 1, column = 0, pady = 10)
        self.Surname_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14)) 
        self.Surname_Entry.grid(row = 1, column = 1,pady = 10)
        self.label_Username = Label(self.inner_frame,text="Username",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Username.grid(row = 2, column = 0, pady = 10)
        self.Username_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Username_Entry.grid(row = 2, column = 1,pady = 10)
        self.label_Password = Label(self.inner_frame,text="Password",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Password.grid(row = 3, column = 0, pady = 10)
        self.Password_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Password_Entry.grid(row = 3, column = 1,pady = 10)
              
        self.button_continue = Button(self.new_frame,text = 'Continue',borderwidth=8, width = 12, bg = "orange",command= lambda: self.Confirm_password( self.new_frame,self.List_Answers,self.list_All_info) )
        self.button_continue.pack()

   def Finish_Quiz (self, List_Answer,selected,Old_frame2):
        self.old_frame2 = Old_frame2
        self.selected =selected
        self.selected1 = self.selected.get()
        self.List_Answers = List_Answer
        self.List_Answers.append(self.selected1) 
        self.list_All_info= [] 
        self.selected.set('None')
        self.old_frame2.destroy()
        self.new_frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
        self.new_frame.pack (pady = 20,padx = 150, fill=BOTH,expand=True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self, self.new_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.Instruct_label = Label( self.new_frame, text = "Enter a username and password that you can remeber",pady = 10, bg = "orange",font=("Verdana", 18   ))
        self.Instruct_label.pack()
        self.inner_frame =Frame (self.new_frame,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
        self.inner_frame.pack(padx=10, pady= 20)
        self.label_FirstName = Label(self.inner_frame,text="FirstName",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_FirstName.grid(row = 0, column = 0, pady = 10)
        self.FirstName_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14) ) 
        self.FirstName_Entry.grid(row = 0, column = 1,pady = 10)
        self.label_Surname = Label(self.inner_frame,text="Surname",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Surname.grid(row = 1, column = 0, pady = 10)
        self.Surname_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14)) 
        self.Surname_Entry.grid(row = 1, column = 1,pady = 10)
        self.label_Username = Label(self.inner_frame,text="Username",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Username.grid(row = 2, column = 0, pady = 10)
        self.Username_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Username_Entry.grid(row = 2, column = 1,pady = 10)
        self.label_Password = Label(self.inner_frame,text="Password",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Password.grid(row = 3, column = 0, pady = 10)
        self.Password_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Password_Entry.grid(row = 3, column = 1,pady = 10)
              
        self.button_continue = Button(self.new_frame,text = 'Continue',borderwidth=8, width = 12, bg = "orange",command= lambda: self.Confirm_password( self.new_frame,self.List_Answers,self.list_All_info) )
        self.button_continue.pack()


   def Confirm_password(self,current_frame,Answer,details) :
      self.list_details = details
      self.list_answer = Answer
      self.current_frame = current_frame
      self.FirstName2 = self.FirstName_Entry.get()
      self.Surname2 = self.Surname_Entry.get()
      self.Username2 = self.Username_Entry.get()
      self.password2 = self.Password_Entry.get()
      self.list_detail = [self.FirstName2,self.Surname2,self.Username2,self.password2]
      self.current_frame.destroy()
      self.frame1 = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10)
      self.frame1.pack(pady = 10,padx = 400, fill=BOTH, expand= True)
      self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self, self.frame1,self.window))
      self.button_Home.place(x=5, y=5, anchor="nw")
      self.Photo_logo = PhotoImage(file="shared image (2).png")
      self.logo = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
      self.logo.grid(row=0,column= 1,padx=5,pady=25)
      self.frame2 = Frame (self.frame1,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
      self.frame2.grid(row= 1,column= 1, pady= 20)         
      self.confirm_password = Label(self.frame2,text="Confirm Password",font=("Verdana", 12),width = 16, pady = 10, bg = "orange")
      self.confirm_password.grid(row = 0, column = 0, pady = 10)
      self.confirm_password_Entry = Entry(self.frame2,borderwidth=8,font=("Verdana", 14) ) 
      self.confirm_password_Entry.grid(row = 0, column = 1,pady = 10)
      self.button_back = Button(self.frame1,text = 'Back',font=("Verdana", 10),borderwidth=8, width = 12, bg = "orange",command=lambda:self.Finish_Quize_2(self.list_answer, self.frame1, self.list_details) )
      self.button_back.grid(row= 2, column= 0)
      self.button_continue2 = Button(self.frame1,text = 'Continue',font=("Verdana", 10),borderwidth=8, width = 12, bg = "orange", command=lambda:self.Show_Result(self.list_answer ,self.frame1, self.list_detail) )
      self.button_continue2.grid(row= 2, column= 2)
   def Finish_Quize_2 (self,Answer,old_frame,details2):
        self.list_details = details2
        self.list_Answer = Answer
        self.old_frame = old_frame
        self.old_frame.destroy()
        self.new_frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
        self.new_frame.pack (pady = 20,padx = 150, fill=BOTH,expand=True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self, self.new_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.Instruct_label = Label( self.new_frame, text = "Enter a username and password that you can remeber",pady = 10, bg = "orange",font=("Verdana", 18   ))
        self.Instruct_label.pack()
        self.inner_frame =Frame (self.new_frame,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
        self.inner_frame.pack(padx=10, pady= 20)
        self.label_FirstName = Label(self.inner_frame,text="FirstName",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_FirstName.grid(row = 0, column = 0, pady = 10)
        self.FirstName_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14) ) 
        self.FirstName_Entry.grid(row = 0, column = 1,pady = 10)
        self.label_Surname = Label(self.inner_frame,text="Surname",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Surname.grid(row = 1, column = 0, pady = 10)
        self.Surname_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14)) 
        self.Surname_Entry.grid(row = 1, column = 1,pady = 10)
        self.label_Username = Label(self.inner_frame,text="Username",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Username.grid(row = 2, column = 0, pady = 10)
        self.Username_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Username_Entry.grid(row = 2, column = 1,pady = 10)
        self.label_Password = Label(self.inner_frame,text="Password",font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.label_Password.grid(row = 3, column = 0, pady = 10)
        self.Password_Entry = Entry(self.inner_frame,borderwidth=8,font=("Verdana", 14))  
        self.Password_Entry.grid(row = 3, column = 1,pady = 10)
        self.button_continue = Button(self.new_frame,text = 'Continue',borderwidth=8, width = 12, bg = "orange",command= lambda: self.Confirm_password( self.new_frame,self.list_Answer,self.list_details) )
        self.button_continue.pack()
   def Show_Result(self,Answer,old_frame,details):
        self.list_details = details
        self.current_Frame = old_frame
        self.List_Answer = Answer
        counter = 0
        counter2= 0
        self.firstName= self.list_details[0]
        self.SurName= self.list_details[1]
        self.username = self.list_details[2]
        self.student_Name = f"{self.firstName}  {self.SurName}"
        self.password2 = self.list_details[3]
        self.password1 = self.confirm_password_Entry.get()

        sqlite3.register_adapter(datetime.datetime, lambda value: value.isoformat())
        sqlite3.register_adapter(datetime.date, lambda value: value.isoformat())

       # Register converters
        def Date_Time (value):
          return datetime.datetime.fromisoformat(value.decode())

        def Date (value):
           return datetime.date.fromisoformat(value.decode())

        sqlite3.register_converter("timestamp", Date_Time)
        sqlite3.register_converter("date", Date)
        if self.password1 == self.password2:
                while counter2 != len(self.List_Question):
                    counter2 = counter2 + 1
                    index = counter2 - 1
                    if self.List_Topic_Answers[index] == self.List_Answer[index]:
                        counter = counter + 1
                self.total_mark = f"{counter}/{counter2}"
                self.Percentage_mark = counter/counter2
                self.Percentage_mark1 = self.Percentage_mark * 100
                self.Percentage_mark2 = round(self.Percentage_mark1,1)
                self.Percentage_mark3 = f"{self.Percentage_mark2}%"
                self.current_Frame.destroy()
                self.new_frame1 = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
                self.new_frame1.pack (pady = 20,padx = 400, fill=BOTH,expand=True)
                self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda:Display.Home (self, self.new_frame1,self.window))
                self.button_Home.place(x=5, y=5, anchor="nw")
                self.Photo_logo = PhotoImage(file="shared image (2).png")
                self.logo = Label(self.new_frame1 ,image= self.Photo_logo,bg ="deep sky blue")
                self.logo.grid(row=0,column= 1,padx=5,pady=25)
                self.inner_frame = Frame (self.new_frame1,bg ="DodgerBlue", borderwidth= 3, padx=10, pady= 10)
                self.inner_frame.grid(row= 1, column= 1, pady= 20)
                self.label_total_mark = Label(self.inner_frame,text="Total Score",font=("Verdana", 12),width = 20, pady = 10, bg = "orange")
                self.label_total_mark.grid(row = 0, column = 0, pady = 10)
                self.label_total_mark2 = Label(self.inner_frame,text=self.total_mark,font=("Verdana", 12),width = 12, pady = 10, bg = "white")
                self.label_total_mark2.grid(row = 0, column = 1, pady = 10)
                self.label_percentage_mark = Label(self.inner_frame,text="Percentage Score",font=("Verdana", 12),width = 20, pady = 10, bg = "orange")
                self.label_percentage_mark.grid(row = 1, column = 0, pady = 10)
                self.label_percentage_mark2 = Label(self.inner_frame,text=self.Percentage_mark3,font=("Verdana", 12),width = 12, pady = 10, bg = "white")
                self.label_percentage_mark2.grid(row = 1, column = 1, pady = 10)
                self.button_end = Button(self.new_frame1,text = 'END',font=("Verdana", 12),borderwidth=8, width = 12, bg = "orange" )
                self.button_end.grid(row= 2, column= 0)
                self.button_certificate = Button(self.new_frame1,text = 'Certificate',font=("Verdana", 12),borderwidth=8, width = 12, bg = "orange",command=lambda:self.certificate( self.Percentage_mark2,self.new_frame1, self.student_Name) )
                self.button_certificate.grid(row= 2, column= 2)
                conn = sqlite3.connect("Table.db")
                self.cursor_student = conn.execute("SELECT * from Student")
                self.list_all_student = []
                self.lower_list2 =[]
                self.counter_student = 0
                self.student_ID = 0
                self.firstName2 = self.firstName.lower()
                self.Surname3 = self.SurName.lower()
                for words in  self.cursor_student:
                     self.list_all_student.append(words)
                     self.counter_student = self.counter_student + 1  
                self.Table_STUDENT_LEN = len( self.list_all_student)   
                self.Student_index = 0
                for counter1 in range ( self.Table_STUDENT_LEN):
                     self.Student_index =  self.Student_index + 1
                     self.tuple_student = self.list_all_student [counter1]
                     self.existed_firstname =  self.tuple_student[1].lower()
                     self.existed_surname =  self.tuple_student[2].lower()
                     self.firstName_lower = self.firstName.lower()
                     self.surname_lower = self.SurName.lower()
                     self.studentId = self.tuple_student[0]
                     if self.existed_firstname == self.firstName_lower :
                          if  self.existed_surname ==  self.surname_lower:
                                 self.Student_index =  self.Student_index -1
                                 conn.execute("""UPDATE Student SET 
                                                 Username = :username,
                                                 Password = :password1
                                                 WHERE StudentID = :student_ID""",
                                                  {'username':self.username,
                                                   'password1':self.password1,
                                                   'student_ID':self.studentId})
                                 conn.commit()
                
                if self.Student_index == self.Table_STUDENT_LEN :
                      firstName = self.firstName
                      SurName = self.SurName 
                      username = self.username
                      password = self.password1
                      counter2 = self.Table_STUDENT_LEN + 1
                      conn.execute("INSERT INTO Student VALUES(:StudentID,:StudentFurname,:StudentSurname,:Username,:Password)", {
                              'StudentID'     : counter2,
                              'StudentFurname': firstName,
                              'StudentSurname': SurName,
                              'Username'      : username,
                              'Password'      : password   })
                      conn.commit()
                self.list_all_student2 = []
                self.cursor_student2 = conn.execute("SELECT * from Student")
                for words in  self.cursor_student2:
                     self.list_all_student2.append(words)
                self.new_len_student = len(self.list_all_student2)
                self.student_id = 0
                for counter3 in range ( self.new_len_student ):
                     self.tuple_student = self.list_all_student2[counter3]
                     self.existed_firstname = self.tuple_student[1].lower()
                     self.existed_surname = self.tuple_student[2].lower()
                     self.lower_firstname = self.firstName.lower()
                     self.lower_surname = self.SurName.lower()
                     self.existed_username = self.tuple_student[3]
                     if self.existed_firstname ==  self.lower_firstname :
                          if self.existed_surname == self.lower_surname:
                                if  self.existed_username == self.username:
                                     self.student_id = self.tuple_student[0]
                self.cursor_Completed_quiz = conn.execute("SELECT * from Completed_Quiz")
                self.list_completed_quiz = []
                for tuples in  self.cursor_Completed_quiz:
                    self.list_completed_quiz.append(tuples)
                self.len_completed_quiz = len(self.list_completed_quiz)
                self.index_completedQuiz = 0
                for counter4 in range(self.len_completed_quiz):
                    self.index_completedQuiz = self.index_completedQuiz + 1
                    self.tuple_completedQuiz = self.list_completed_quiz[counter4]
                    self.existed_firstname =  self.tuple_completedQuiz[2].lower()
                    self.lower_firstname = self.firstName.lower()
                    self.topic = self.tuple_completedQuiz[4]
                    self.existed_studentId = self.tuple_completedQuiz[1]
                    self.existed_totalMark_1 = self.tuple_completedQuiz[5]
                    self.existed_totalMark_2 = Fraction(self.existed_totalMark_1)
                    self.existed_totalMark = round((float(self.existed_totalMark_2) *100), 1)
                    self.student_id2 = str( self.student_id)
                    self.quize_id =  self.tuple_completedQuiz[0]
                    self.date_now = datetime.datetime.now()
                    self.date = self.date_now .date()
                    self.date2= self.date.strftime('%d/%m/%Y')
                    conn = sqlite3.connect("Table.db")
                    if self.existed_totalMark  < self.Percentage_mark2:
                         if  self.existed_studentId ==  self.student_id2:
                              if self.lower_firstname == self.existed_firstname:
                    
                                   if self.topic == self.selected_Topic:                                      
                                        conn.execute("""UPDATE  Completed_Quiz SET 
                                                       TotalMark      =  :updated_mark,
                                                       Date           =  :updated_date
                                                       WHERE Quiz_ID  =  :existed_Id""",
                                                       {'updated_mark'   :self.total_mark,
                                                       'updated_date'    :self.date2,
                                                       'existed_Id'      :self.quize_id})
                                        self.index_completedQuiz= self.index_completedQuiz - 1 
                                        conn.commit()
                                       
                    if  self.existed_totalMark   == self.Percentage_mark2:
                                   if  self.existed_studentId ==  self.student_id2:
                                        if self.lower_firstname == self.existed_firstname:
                                             if self.topic == self.selected_Topic:
                                                  self.index_completedQuiz = self.index_completedQuiz - 1 
                    if  self.existed_totalMark  > self.Percentage_mark2:
                                   if  self.existed_studentId ==  self.student_id2:
                                        if self.lower_firstname == self.existed_firstname:
                                             if self.topic == self.selected_Topic:
                                                  self.index_completedQuiz = self.index_completedQuiz - 1 

                              
                Quizid         = self.len_completed_quiz + 1
                totalmark      = int(counter)          
                Studentid      = self.student_id          
                studentfurname = self.firstName               
                Topicname      = self.selected_Topic
              
                datenow = datetime.datetime.now()
                Topicid = ""
                if Topicname == "Energy":
                   Topicid = "1"
                if Topicname == "Material":
                   Topicid = "2"
                if Topicname == "Momentum":
                   Topicid = "3"
                if Topicname == "Wave":
                   Topicid = "4"
                
                self.date = datenow.date()
                self.date2= self.date.strftime('%d/%m/%Y')
                if  self.index_completedQuiz == self.len_completed_quiz:
                    conn.execute("INSERT INTO Completed_Quiz VALUES(:Quiz_ID,:StudentID,:StudentFurname,:TopicID ,:TopicName,:TotalMark,:Date )", {
                         'Quiz_ID'        :  Quizid,
                         'StudentID'      :  Studentid,
                         'StudentFurname' : studentfurname,
                         'TopicID'        : Topicid,
                         'TopicName'      : Topicname,
                         'TotalMark'      : self.total_mark,
                         'Date'           : self.date2 })
                    conn.commit()
                  
                
                
                conn.execute("INSERT INTO History (StudentID,TopicID ,TopicName,TotalMark, PercentageMark, Date ) VALUES(:StudentID,:TopicID ,:TopicName,:TotalMark, :PercentageMark, :Date )", {
                         'StudentID'      :  Studentid,
                         'TopicID'        : Topicid,
                         'TopicName'      : Topicname,
                         'TotalMark'      : self.total_mark,
                         'PercentageMark' : self.Percentage_mark3,
                         'Date'           :  self.date2})
                conn.commit()
                conn.close()
                
                     
               
               

                if self.Percentage_mark2 >= 50:
                    self.label_compliment = Label(self.new_frame1,text="welldone!",font=("Verdana", 12),width = 12, pady = 10, bg = "greenyellow")
                    self.label_compliment.grid(row = 2, column = 1, pady = 10)
                else:
                    self.label_compliment = Label(self.new_frame1,text="You can do better than this",font=("Verdana", 12),width = 23, pady = 10, bg = "red")
                    self.label_compliment.grid(row = 2, column = 1, pady = 10)
        else :
             messagebox.showinfo("Information", "The password you entered do not match. You can click Back to reset your password and username or try confirming your password again")    
   def certificate (self, score,old_windo,Student_name):
     self.student_name = Student_name
     self.window2 = old_windo
     self.score = score
     
     if self.score >= 50.0:
          self.window2.destroy()
          self.frame1 = Frame(self.window,width="300",height="300", bg= "orange")
          self.frame1.pack(padx=5,pady=20)
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home ( self, self.frame1,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.frame2 = Frame(self.frame1,width="250",height="250", bg= "brown")
          self.frame2.pack(padx=60,pady=60)
          self.frame3 = Frame(self.frame2,width="250",height="250", bg= "white")
          self.frame3.pack(padx=8,pady=8)
          if self.score >= 50.0:
             if self.score <= 69.0:
                  self.label_complement = Label(self.frame3, text = "BRONZE",font=("Times New Roman",100),fg =  "brown",bg = "white")
                  self.label_complement .pack(padx=10)
          if self.score >= 70.0:
               if self.score <= 84.0:
                    self.label_complement = Label(self.frame3, text = "SILVER",font=("Times New Roman",100),fg =  "brown",bg = "white")
                    self.label_complement.pack(padx=10)
                    
          if self.score >= 85.0:
               if self.score <= 100.0:
                    self.label_complement = Label(self.frame3, text = "GOLD",font=("Times New Roman",100),fg = "brown",bg = "white")
                    self.label_complement.pack(padx=10)
                    
          
          
          #label_bronze = Label(frame3, text = "BRONZE",font=("Times New Roman",100),fg= "#FFC300",bg = "white")
          #label_bronze.pack(padx=10)
          self.label_complement1 = Label(self.frame3, text = "PHYSICS CERTIFICATE",font=("Arial",30),fg = "black",bg = "white")
          self.label_complement1.pack(padx=10)
          self.label_complement2 = Label(self.frame3, text = "This Certificate Is Awarded To",font=("Arial",15),fg = "black",bg = "white")
          self.label_complement2.pack(padx=10,pady=20)
          self.label_complement3 = Label(self.frame3, text = self.student_name,font=("Lucida Handwriting",38),fg = "brown",bg = "white")
          self.label_complement3.pack(padx=10)
          self.label_complement4 = Label(self.frame3, text = "________________________________",font=("Arial",25),fg = "brown",bg = "white")
          self.label_complement4.pack(padx=10)
          self.label_complement5 = Label(self.frame3, text = "Awarded in acknowledgment of his/her dedication, performance, and continuous engagement\n in advanced physics learning, demonstrated through the successful\n completion of the OCR A-Level Physics Quiz.",font=("Arial",10),fg = "black",bg = "white")
          self.label_complement5.pack(padx=10)
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.frame3,image= self.Photo_logo,bg ="white")
          self.logo.pack()
          messagebox.showwarning("Information", "You can take a screenshot of your certificate for future use")

     else:
          messagebox.showwarning("Information", "You need to get a percentage score of at least 50% to generate a Certificate")
    
class Update:
     def sign_in_plus (self,window,old_frame):
        self.window = window
        self.old_frame = old_frame
        self.old_frame.destroy()
        self.frame1 = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
        self.frame1.pack (pady = 29,padx = 100, fill=BOTH,expand=True)
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame1,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.frame = Frame( self.frame1, borderwidth=10,width=0, height=0,bg ="DodgerBlue",pady = 10,padx = 10)  
        self.frame.pack (pady = 20,padx = 20)         

        self.Username_Label = Label(self.frame, text = "USERNAME", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
        self.Username_Label.grid(row = 0, column = 0, pady = 10)
        self.Password_Label = Label(self.frame, text = "PASSWORD", font=("Verdana", 12),width = 12, pady = 10,bg = "orange")
        self.Password_Label.grid(row = 1, column = 0,pady = 10)
        self.Username_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14))
        self.Username_Entry.grid(row = 0, column = 1,pady =10)
        self.Password_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14) , show = "*") 
        self.Password_Entry.grid(row = 1, column = 1,pady = 10)
        self.username= self.Username_Entry.get()
        self.password = self.Password_Entry.get()
        self.ButtonLogin = Button(self.frame1, text = 'LogIn',borderwidth=8, width = 10, bg = "orange", font = ("Verdana", 12),command =lambda : self.update_menu(self.frame1,self.window))
        self.ButtonLogin.pack( pady =5, padx = 5)
     def show_info(self): 
         messagebox.showwarning("Information", "Incorrect username or password please try again")
     def update_menu(self,old_frame,window):
        self.window2 = window
        self.Old_Frame = old_frame
        self.username= self.Username_Entry.get()
        self.password = self.Password_Entry.get()
        if self.username == "mine":
             if self.password == "1":
                self.Old_Frame.destroy()
                self.new_frame = Frame(self.window2, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
                self.new_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
                self.button_Home = Button(self.window2,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.new_frame, self.window2))
                self.button_Home.place(x=5, y=5, anchor="nw")
                
                self.Photo_logo = PhotoImage(file="shared image (2).png")
                self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
                self.logo.pack(padx=5,pady=25)
        
                self.inner_frame = Frame(self.new_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
                self.inner_frame.pack (pady = 20,padx = 20) 
                self.Button_Display = Button (self.inner_frame, text = "Display all Question", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 20 , command=lambda: self.show_TopicList(self.new_frame, self.inner_frame))  
                self.Button_Display.pack(pady = 5, padx = 5)
                self.Button_Update= Button(self.inner_frame, text = "Update Questions", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda: self.show_TopicList2(self.new_frame, self.inner_frame))
                self.Button_Update.pack(pady = 5, padx = 5)
             else:
                self.Old_Frame.destroy()
                self.sign_in_plus(self.window2,self.frame1)
                self.show_info()

        else:
                self.Old_Frame.destroy()
                self.sign_in_plus(self.window2,self.frame1)
                self.show_info()

     def show_TopicList (self,outerFrame,innerframe):
        self.outer_frame = outerFrame
        self.inner_frame = innerframe
        self.inner_frame.destroy()
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Display.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Display_Questions( self.listbox, self.outer_frame)) 
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)
    
     def show_TopicList2 (self,outerFrame,innerframe):
        self.outer_frame = outerFrame
        self.inner_frame = innerframe
        self.inner_frame.destroy()
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Update_Options( self.outer_frame,self.listbox )) 
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)

     def listbox2 (self,frame):
         self.Class2 = Attempt()
         self.old_Frame = frame
         self.old_Frame.destroy()
         self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
         self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
         self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self,self.outer_frame,self.window))
         self.button_Home.place(x=5, y=5, anchor="nw")
         self.Photo_logo = PhotoImage(file="shared image (2).png")
         self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
         self.logo.pack(padx=5,pady=25)
         self.innerframe = Frame(self.outer_frame , borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
         self.innerframe.pack(pady = 20,padx = 20)
         self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves"]
         self.listbox = Listbox( self.innerframe, height= 5)
         for Words in self.List_of_Topics:
             self.listbox.insert(END, Words)
         self.listbox.grid(row=1, column= 0,padx=5,pady= 5)
        
         self.topic_label = Label( self.innerframe, text = "Select a Topic and click on the enter button to proceed.", font = ("verdana", 9), background = "orange")
         self.topic_label.grid(row=0, column= 0,padx=5,pady= 5)
         self.Button_Enter = Button( self.innerframe, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda:  self.Class2.Display_Question1( self.outer_frame,  self.innerframe, self.listbox, self.window)) 
         self.Button_Enter.grid(row=2, column= 0,padx=5,pady= 5)

     def Update_Options(self,old_frame,listbox):
          self.old_frame = old_frame
          self.listbox = listbox
          self.selected_indeces = self.listbox.curselection()
          self.index = self.selected_indeces [0]
          self.value = self.listbox.get(self.index)
          self.old_frame.destroy()
          self.new_frame =Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
          self.new_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
          self.button_Home = Button(self.window2,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.new_frame, self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")

          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.new_frame ,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=25)

          self.inner_frame = Frame(self.new_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
          self.inner_frame.pack (pady = 20,padx = 20) 
          self.Button_AddQuestion = Button (self.inner_frame, text = "Add Question", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 20,command= lambda: self.Add_Question(self.value,self.new_frame,self.window))  
          self.Button_AddQuestion.pack(pady = 5, padx = 5)
          self.Button_DeleteQuestion= Button(self.inner_frame, text = "Delete Question", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda:self.Display_Questions_2(self.value,self.new_frame))
          self.Button_DeleteQuestion.pack(pady = 5, padx = 5)
         


     def Display_Questions_2(self,selected_topic,old_frame):
          self.old_frame = old_frame
          self.selected_topic = selected_topic
          conn = sqlite3.connect('Table.db')
          self.TABLE = conn.execute("SELECT * FROM Topic")
          self.Tuple_Table = []
          self.List_Table = []
          self.counter = 0
          self.str_Question = []
          self.srt_answer = []
          self.List_Topic_Answers =[]
          self.List_Question = []
          for words in self.TABLE:
                self.Tuple_Table.append(words)               
                for words in self.Tuple_Table:
                    for words_2 in words:
                        self.List_Table.append(words_2)
          for words in self.List_Table:
                    self.counter = self.counter + 1  
                    if words ==  self.selected_topic:
                        
                        self.str_Question = self.List_Table[self.counter]
                        self.srt_answer = self.List_Table[self.counter + 1]
                        self.List_Topic_Answers = json.loads(self.srt_answer)        
                        self.List_Question = json.loads(self.str_Question)
          self.counter2 = 0
          self.Question_and_Answer = self.List_Question[self.counter2]
          self.answer = self.List_Topic_Answers[0]
          self.columns = ("Questions", "Options", "Answer")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 10),background ="orange",fieldbackground="orange", foreground="black")
          self.style.configure("Treeview.Heading",font=("verdana", 12,"bold"))
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.tree.pack(expand=True, fill='both')
          self.tree_type_question = []
          self.tree_type_answers = ""
          self.index = 0
          self.old_frame .destroy()
          if self.selected_topic == "Energy":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=500,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=400,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")
                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic == "Material":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=480,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=460,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Momentum":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=460,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=500,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Waves":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=420,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=540,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          for lists in self.List_Question:
            self.tree_type_question.append(lists[0]) 
            self.tree_type_answers = f"{lists[1],lists[2],lists[3],lists[4]}"
            self.tree_type_question.append(self.tree_type_answers)
            self.tree_type_question.append( self.List_Topic_Answers[self.index])
            self.tree.insert("",END, values=self.tree_type_question)
            self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tag = "line2")
            self.index = self.index + 1
            self.tree_type_answers = ""
            self.tree_type_question = []
          self.button_Enter = Button(self.frame, text = "Delete Question", font = ("verdana", 12), bg = "orange", width = 15, command = lambda:  self.Delete_Question("event",self.List_Question,self.List_Topic_Answers,self.frame,self.listbox )) 
          self.button_Enter.pack(padx=5,pady= 5)

         
 
          self.selectd_question = self.tree.selection()
     def Delete_Question (self,event,list_Question,list_answer,current_frame,listbox):
          self.currrent_frame = current_frame
          self.selectd_question = self.tree.selection()
          if not self.selectd_question :
                messagebox.showwarning("Selection validation", "Please select a question before clicking the button delete.")
          self.tree_item = self.tree.item(self.selectd_question )
          self.selectd_question2 = self.tree_item ["values"]
          try:
               if "-----" in self.selectd_question2[0]:
                    if "-----" in self.selectd_question2[1]:
                         if "-----" in self.selectd_question2[2]:
                              messagebox.showwarning("Selection validation", "Please select any other row which contains quetion and not seperation lines")
                              self.selectd_question = []
          except:
               pass
          self.list_Question =list_Question
          self.list_answer = list_answer
          self.listbox = listbox
          self.counter = 0
          self.counter2 = 0
          if self.selectd_question :
               self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self, self.frame,self.window))
               self.button_Home.place(x=5, y=5, anchor="nw")
               self.tree_item = self.tree.item(self.selectd_question )
               self.selectd_question2 = self.tree_item ["values"]
          
               self.list_selected_question3 = []
               
               self.list_selected_question3.append(self.selectd_question2[0])
               self.str_options = list(ast.literal_eval(self.selectd_question2[1]))
              
               for words in self.str_options:
                   self.list_selected_question3.append(words)

               
               for Questions in self.list_Question:
                    if Questions == self.list_selected_question3:
                         break
                    self.counter = self.counter + 1
               for words in self.list_answer:
                    if words == self.selectd_question2[2]:
                         break
                    self.counter2 = self.counter2 + 1
               self.list_Question.pop(self.counter)
               self.list_answer.pop(self.counter2)
               
               conn = sqlite3.connect('Table.db')  
               self.Topic_ID = conn.execute("SELECT * FROM Topic ")
               self.Topic_ID2 = self.Topic_ID.fetchall()
               self.topic_id3 = 0
               
               for counter in range(len(self.Topic_ID2)):
                    
                    if self.Topic_ID2[counter][1] == self.selected_topic :
                         self.topic_id3 = self.Topic_ID2[counter][0]
               self.str_question = json.dumps(self.list_Question)
               self.str_Answer = json.dumps(self.list_answer)
               conn.execute("DELETE FROM Topic WHERE TopicID = %s" %(self.topic_id3)) 
               conn.commit()
               conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                    'TopicID'     :   self.topic_id3 ,
                    'TopicName'   :  self.selected_topic,
                    'Questions'   :  self.str_question  ,
                    'Answer'      :  self.str_Answer
                })
               conn.commit()
               self.comfirm_update_delete( self.selected_topic,self.currrent_frame,self.listbox )
     def comfirm_update_delete(self,selected_topic,old_frame,listbox ):
          self.listbox = listbox
          self.old_frame = old_frame
          self.selected_topic = selected_topic
          conn = sqlite3.connect('Table.db')
          self.TABLE = conn.execute("SELECT * FROM Topic")
          self.Tuple_Table = []
          self.List_Table = []
          self.counter = 0
          self.str_Question = []
          self.srt_answer = []
          self.List_Topic_Answers =[]
          self.List_Question = []
          for words in self.TABLE:
                self.Tuple_Table.append(words)               
                for words in self.Tuple_Table:
                    for words_2 in words:
                        self.List_Table.append(words_2)
          for words in self.List_Table:
                    self.counter = self.counter + 1  
                    if words ==  self.selected_topic:
                        print(self.selected_topic)
                        self.str_Question = self.List_Table[self.counter]
                        self.srt_answer = self.List_Table[self.counter + 1]
                        self.List_Topic_Answers = json.loads(self.srt_answer)        
                        self.List_Question = json.loads(self.str_Question)
          self.counter2 = 0
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.Question_and_Answer = self.List_Question[self.counter2]
          self.answer = self.List_Topic_Answers[0]
          self.columns = ("Questions", "Options", "Answer")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 10),background ="orange",fieldbackground="orange", foreground="black")
          self.style.configure("Treeview.Heading",font=("verdana", 12,"bold"))
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.tree.pack(expand=True, fill='both')
          self.tree_type_question = []
          self.tree_type_answers = ""
          self.index = 0
          self.old_frame .destroy()
          if self.selected_topic == "Energy":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=500,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=400,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")
                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic == "Material":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=480,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=460,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Momentum":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=460,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=500,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Waves":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=420,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=540,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          for lists in self.List_Question:
            self.tree_type_question.append(lists[0]) 
            self.tree_type_answers = f"{lists[1],lists[2],lists[3],lists[4]}"
            self.tree_type_question.append(self.tree_type_answers)
            self.tree_type_question.append( self.List_Topic_Answers[self.index])
            self.tree.insert("",END, values=self.tree_type_question)
            self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tag = "line2")
            self.index = self.index + 1
            self.tree_type_answers = ""
            self.tree_type_question = []
          self.button_comfirmed = Button(self.frame, text = "Comfirmed", font = ("verdana", 12), bg = "orange", width = 10, command=lambda: Display.Home(self, self.frame, self.window)) 
          self.button_comfirmed.pack(padx=5,pady= 5)           
          self.selectd_question = self.tree.selection()
          messagebox.showwarning("Information", "Comfirm if the question as been Deleted successfully✅")
             


     def Add_Question(self,Selected_topic, old_frame,window):
          self.old_frame = old_frame
          self.selected_topic = Selected_topic
          self.window = window
          self.old_frame.destroy()
          self.new_frame = Frame(self.window,border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
          self.new_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.new_frame ,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=5)
          self.inner_frame = Frame(self.new_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
          self.inner_frame.pack (pady = 5,padx = 20)
          


          self.label_Question = Label(self.inner_frame,text = "Question", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_Question.grid(row = 0, column = 0, pady = 10) 

          self.entry_Question = Text ( self.inner_frame,height=5, width=50, borderwidth=8)
          self.entry_Question.grid(row = 0, column = 1,pady =10)  

          self.label_opt_A = Label(self.inner_frame,text = "OPTION_A", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_opt_A.grid(row = 1, column = 0, pady = 10)

          self.entry_opt_A = Entry(self.inner_frame, borderwidth=8,font=("Verdana", 14))
          self.entry_opt_A.grid(row = 1, column = 1,pady =10)

          self.label_opt_B = Label(self.inner_frame,text = "OPTION_B", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_opt_B.grid(row = 2, column = 0, pady = 10)

          self.entry_opt_B = Entry(self.inner_frame, borderwidth=8,font=("Verdana", 14))
          self.entry_opt_B.grid(row = 2, column = 1,pady =10)

          self.label_opt_C = Label(self.inner_frame,text = "OPTION_C", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_opt_C.grid(row = 3, column = 0, pady = 10)  

          self.entry_opt_C = Entry(self.inner_frame, borderwidth=8,font=("Verdana", 14))
          self.entry_opt_C.grid(row = 3, column = 1,pady =10)

          self.label_opt_D = Label(self.inner_frame,text = "OPTION_D", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_opt_D.grid(row = 4, column = 0, pady = 10)

          self.entry_opt_D = Entry(self.inner_frame, borderwidth=8,font=("Verdana", 14))
          self.entry_opt_D.grid(row = 4, column = 1,pady =10)

          self.label_answer = Label(self.inner_frame,text = "ANSWER", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.label_answer.grid(row = 5, column = 0, pady = 10)

          self.entry_answer = Entry(self.inner_frame, borderwidth=8,font=("Verdana", 14))
          self.entry_answer.grid(row = 5, column = 1,pady =10)
          self.button_add = Button(self.new_frame, text = "Confirm Question", font = ("verdana", 12), bg = "orange", width = 15, command=lambda:self.format_added_question(self.new_frame,self.entry_Question,self.entry_opt_A,self.entry_opt_B,self.entry_opt_C,self.entry_opt_D,self.entry_answer,self.new_frame)) 
          self.button_add.pack(padx=5,pady= 5)
     def format_added_question(self,old_frame,Question,option_A,option_B,option_C,option_D,answer,current_frame): 
          self.current_frame = current_frame
          self.old_frame = old_frame
          self.entry_Question= Question 
          self.entry_opt_A = option_A
          self.entry_opt_B = option_B
          self.entry_opt_C = option_C
          self.entry_opt_D = option_D
          self.answer = answer
          self.grab_entry_Question2 = self.entry_Question.get("1.0", END).strip()
          self.splited_question =  self.grab_entry_Question2.split()
          self.list_question_and_answer = []  
         
          self.list_formated_question = []
          self.list_all_option = []
          self.lent_text = 0
          self.saved_counter = 0
          self.long_answer = 0
          for counter in range(len(self.splited_question)):
               self.list_formated_question.append(self.splited_question[counter])
               self.lent_text = self.lent_text + len(self.splited_question[counter]) + 1
               self.saved_counter = counter
               if self.lent_text >= 60:
                    self.list_formated_question.append("\n")
                    break
         
          for counter in range(self.saved_counter + 1, len(self.splited_question)):
               self.list_formated_question.append(self.splited_question[counter])
          print(self.list_formated_question)
          self.str_formated_question = " ".join(self.list_formated_question)
          print(self.str_formated_question)
          self.list_question_and_answer.append(self.str_formated_question)
          self.list_question_and_answer.append(self.entry_opt_A.get() )
          self.list_question_and_answer.append(self.entry_opt_B.get() )
          self.list_question_and_answer.append(self.entry_opt_C.get())
          self.list_question_and_answer.append(self.entry_opt_D.get() )
          
          for counter in range(1,5):
               self.list_all_option.append(self.list_question_and_answer[counter])
          if self.answer.get() in self.list_all_option:
                if len(self.entry_opt_A.get()) > len(self.entry_opt_B.get()) and len(self.entry_opt_C.get()) and len(self.entry_opt_D.get())  :
                    self.long_answer = len(self.entry_opt_A.get())
                if len(self.entry_opt_B.get()) > len(self.entry_opt_A.get()) and len(self.entry_opt_C.get()) and len(self.entry_opt_D.get())  :
                    self.long_answer = len(self.entry_opt_B.get())
                if len(self.entry_opt_C.get()) > len(self.entry_opt_A.get()) and len(self.entry_opt_B.get()) and len(self.entry_opt_D.get())  :
                    self.long_answer = len(self.entry_opt_C.get())
                if len(self.entry_opt_D.get()) > len(self.entry_opt_A.get()) and len(self.entry_opt_B.get()) and len(self.entry_opt_C.get())  :
                    self.long_answer = len(self.entry_opt_D.get())
                self.list_all_option = []
                self.option_A = self.entry_opt_A.get()
                self.option_B = self.entry_opt_B.get()
                self.option_C = self.entry_opt_C.get()
                self.option_D = self.entry_opt_D.get()
                self.formated_answer = self.answer.get()
                for counter in range(len(self.entry_opt_A.get()),self.long_answer):
                     self.option_A = self.option_A  + " "
                for counter in range(len(self.entry_opt_B.get()),self.long_answer):
                     self.option_B = self.option_B  + " "
                for counter in range(len(self.entry_opt_C.get()),self.long_answer):
                     self.option_C = self.option_C  + " "
                for counter in range(len(self.entry_opt_D.get()),self.long_answer):
                     self.option_D = self.option_D  + " "
                for counter in range(len(self.answer.get()),self.long_answer):
                     self.formated_answer = self.formated_answer  + " "
                self.list_question_and_answer = []
                self.list_question_and_answer.append(self.str_formated_question)
                self.list_question_and_answer.append(self.option_A)
                self.list_question_and_answer.append(self.option_B)
                self.list_question_and_answer.append(self.option_C)
                self.list_question_and_answer.append(self.option_D)
                self.selected_topic_ID = 0
                conn = sqlite3.connect('Table.db')
                self.TABLE = conn.execute("SELECT * FROM Topic")
                self.Tuple_Table = []
                self.List_Table = []
                self.counter = 0
                self.str_Question = []
                self.srt_answer = []
                self.List_Topic_Answers =[]
                self.List_Question = []
                for words in self.TABLE:
                    self.Tuple_Table.append(words)               
                    for words in self.Tuple_Table:
                         for words_2 in words:
                           self.List_Table.append(words_2)
                for words in self.List_Table:
                         self.counter = self.counter + 1  
                         if words ==  self.selected_topic:
                              self.selected_topic_ID = self.List_Table[self.counter - 2]
                              self.str_Question = self.List_Table[self.counter]
                              self.srt_answer = self.List_Table[self.counter + 1]
                              self.List_Topic_Answers = json.loads(self.srt_answer)        
                              self.List_Question = json.loads(self.str_Question)
                
                self.List_Question.append(self.list_question_and_answer)
                self.List_Topic_Answers.append(self.formated_answer)
                print(self.List_Topic_Answers)
                print(self.List_Question)
                print(self.selected_topic_ID)
                self.str_question = json.dumps(self.List_Question)
                self.str_Answer = json.dumps(self.List_Topic_Answers)
                conn.execute("DELETE FROM Topic WHERE TopicID = %s" %(self.selected_topic_ID)) 
                conn.commit()

                conn.execute("INSERT INTO Topic VALUES(:TopicID,:TopicName,:Questions,:Answer)",{
                    'TopicID'     :   self.selected_topic_ID ,
                    'TopicName'   :  self.selected_topic,
                    'Questions'   :  self.str_question  ,
                    'Answer'      :  self.str_Answer
                })
                conn.commit()
     
                self.comfirm_update_adding( self.selected_topic,self.current_frame )
          else: 
             messagebox.showwarning("Answer validation", "Please make sure the answer you entered is included an one of the options")   
     
     def comfirm_update_adding(self,selected_topic,old_frame ):
          self.old_frame = old_frame
          self.selected_topic = selected_topic
          conn = sqlite3.connect('Table.db')
          self.TABLE = conn.execute("SELECT * FROM Topic")
          self.Tuple_Table = []
          self.List_Table = []
          self.counter = 0
          self.str_Question = []
          self.srt_answer = []
          self.List_Topic_Answers =[]
          self.List_Question = []
          for words in self.TABLE:
                self.Tuple_Table.append(words)               
                for words in self.Tuple_Table:
                    for words_2 in words:
                        self.List_Table.append(words_2)
          for words in self.List_Table:
                    self.counter = self.counter + 1  
                    if words ==  self.selected_topic:
                        print(self.selected_topic)
                        self.str_Question = self.List_Table[self.counter]
                        self.srt_answer = self.List_Table[self.counter + 1]
                        self.List_Topic_Answers = json.loads(self.srt_answer)        
                        self.List_Question = json.loads(self.str_Question)
          self.counter2 = 0
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.Question_and_Answer = self.List_Question[self.counter2]
          self.answer = self.List_Topic_Answers[0]
          self.columns = ("Questions", "Options", "Answer")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 10),background ="orange",fieldbackground="orange", foreground="black")
          self.style.configure("Treeview.Heading",font=("verdana", 12,"bold"))
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.tree.pack(expand=True, fill='both')
          self.tree_type_question = []
          self.tree_type_answers = ""
          self.index = 0
          self.old_frame .destroy()
          if self.selected_topic == "Energy":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=500,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=400,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")
                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic == "Material":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=480,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=460,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Momentum":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=460,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=500,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          if self.selected_topic =="Waves":
                self.tree.heading("Questions", text = "Questions")
                self.tree.column("Questions",width=420,anchor = "w")

                self.tree.heading("Options", text = "Options")
                self.tree.column("Options",width=540,anchor = "w")

                self.tree.heading("Answer", text = "Answer")
                self.tree.column("Answer",width=120,anchor = "w")

                self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
          for lists in self.List_Question:
            self.tree_type_question.append(lists[0]) 
            self.tree_type_answers = f"{lists[1],lists[2],lists[3],lists[4]}"
            self.tree_type_question.append(self.tree_type_answers)
            self.tree_type_question.append( self.List_Topic_Answers[self.index])
            self.tree.insert("",END, values=self.tree_type_question)
            self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tag = "line2")
            self.index = self.index + 1
            self.tree_type_answers = ""
            self.tree_type_question = []
          self.button_comfirmed = Button(self.frame, text = "Comfirmed", font = ("verdana", 12), bg = "orange", width = 10, command=lambda: Display.Home(self, self.frame, self.window)) 
          self.button_comfirmed.pack(padx=5,pady= 5)           
          self.selectd_question = self.tree.selection()
          messagebox.showinfo("Information", "Comfirm if the question as been Added successfully✅")
             


   
                    

        

     def Display_Questions(self,listbox,old_frame):
            self.selected_indeces = listbox.curselection()
            self.index = self.selected_indeces [0]
            self.value = listbox.get(self.index)
            self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home( self,self.frame,self.window2))
            self.button_Home.place(x=5, y=5, anchor="nw")
            self.selected_Topic = self.value
            conn = sqlite3.connect('Table.db')
            self.TABLE = conn.execute("SELECT * FROM Topic")
            self.Tuple_Table = []
            self.List_Table = []
            self.List_Topic_Answers = []
            self.List_Question = []
            self.List_Selected_Answer = []
            self.counter = 0
            self.Question_and_Answer = []
            self.old_frame2 = old_frame
            if self.selected_Topic:
                self.old_frame2.destroy()
                for words in self.TABLE:
                    self.Tuple_Table.append(words)
                for words in self.Tuple_Table:
                    for words_2 in words:
                        self.List_Table.append(words_2)
                for words in self.List_Table:
                    self.counter = self.counter + 1  
                    if words ==  self.selected_Topic:
                        print(self.selected_Topic)
                        self.str_Question = self.List_Table[self.counter]
                        self.srt_answer = self.List_Table[self.counter + 1]
                self.List_Topic_Answers = json.loads(self.srt_answer)        
                self.List_Question = json.loads(self.str_Question)
                self.counter2 = 0
                self.Question_and_Answer = self.List_Question[self.counter2]
                self.answer = self.List_Topic_Answers[0]
                self.columns = ("Questions", "Options", "Answer")
                self.frame = Frame(self.window2, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
                self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
                self.style = ttk.Style()
                self.style.configure("Treeview",rowheight = 40,font = ("verdana", 10),background ="orange",fieldbackground="orange", foreground="black")
                self.style.configure("Treeview.Heading",font=("verdana", 12,"bold"))
                self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
                self.tree.pack(expand=True, fill='both')
                self.tree_type_question = []
                self.tree_type_answers = ""
                self.index = 0
                if self.selected_Topic == "Energy":
                        self.tree.heading("Questions", text = "Questions")
                        self.tree.column("Questions",width=500,anchor = "w")

                        self.tree.heading("Options", text = "Options")
                        self.tree.column("Options",width=400,anchor = "w")

                        self.tree.heading("Answer", text = "Answer")
                        self.tree.column("Answer",width=120,anchor = "w")
                        self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                        self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                        self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
                if self.selected_Topic == "Material":
                        self.tree.heading("Questions", text = "Questions")
                        self.tree.column("Questions",width=480,anchor = "w")

                        self.tree.heading("Options", text = "Options")
                        self.tree.column("Options",width=460,anchor = "w")

                        self.tree.heading("Answer", text = "Answer")
                        self.tree.column("Answer",width=120,anchor = "w")

                        self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                        self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                        self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
                if self.selected_Topic =="Momentum":
                        self.tree.heading("Questions", text = "Questions")
                        self.tree.column("Questions",width=460,anchor = "w")

                        self.tree.heading("Options", text = "Options")
                        self.tree.column("Options",width=500,anchor = "w")

                        self.tree.heading("Answer", text = "Answer")
                        self.tree.column("Answer",width=120,anchor = "w")

                        self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                        self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                        self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
                if self.selected_Topic =="Waves":
                        self.tree.heading("Questions", text = "Questions")
                        self.tree.column("Questions",width=420,anchor = "w")

                        self.tree.heading("Options", text = "Options")
                        self.tree.column("Options",width=540,anchor = "w")

                        self.tree.heading("Answer", text = "Answer")
                        self.tree.column("Answer",width=120,anchor = "w")

                        self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tags="line")
                        self.tree.tag_configure("line",font = ("courier New",30,"bold"))
                        self.tree.tag_configure("line2",font = ("courier New",15,"bold"))
                for lists in self.List_Question:
                    self.tree_type_question.append(lists[0]) 
                   
                    self.tree_type_answers = f"{lists[1],lists[2],lists[3],lists[4]}"
                    self.tree_type_question.append(self.tree_type_answers)
                    self.tree_type_question.append( self.List_Topic_Answers[self.index])
                    self.tree.insert("",END, values=self.tree_type_question)
                    self.tree.insert("",END, values=("-"*100,"-"*100,"-"*100),tag = "line2")
                    self.index = self.index + 1
                    self.tree_type_answers = ""
                    self.tree_type_question = []
                self.button_done= Button(self.frame, text = "Done", font = ("verdana", 12), bg = "orange", width = 6, command=lambda: Display.Home( self,self.frame,self.window2)) 
                self.button_done.pack(padx=5,pady= 5)

                self.selectd_question = self.tree.selection()


                

class History(Update):   
     def History_options(self,old_frame,window):
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.window = window
          self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
          self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.outer_frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")   
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=25)
          self.information_label = Label(self.outer_frame,text = "View Student History as a?", font = ("verdana", 15), background = "orange")
          self.information_label.pack(padx=5,pady= 5) 
          self.inner_frame = Frame(self.outer_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
          self.inner_frame.pack (pady = 5,padx = 20)            
          self.Button_Teacher = Button (self.inner_frame, text = "Teacher", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 20,command= lambda: self.History_login_teacher(self.outer_frame))  
          self.Button_Teacher.pack(pady = 5, padx = 5)
          self.Button_Student= Button(self.inner_frame, text = "Student", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda:self.history_log_in_as_student(self.outer_frame))
          self.Button_Student.pack(pady = 5, padx = 5)   
     def History_login_teacher(self,old_frame):
          self.class3 = Update()
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.frame1 = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
          self.frame1.pack (pady = 29,padx = 100, fill=BOTH,expand=True)
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=25)
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame1,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.frame = Frame( self.frame1, borderwidth=10,width=0, height=0,bg ="DodgerBlue",pady = 10,padx = 10)  
          self.frame.pack (pady = 20,padx = 20)         

          self.Username_Label = Label(self.frame, text = "USERNAME", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.Username_Label.grid(row = 0, column = 0, pady = 10)
          self.Password_Label = Label(self.frame, text = "PASSWORD", font=("Verdana", 12),width = 12, pady = 10,bg = "orange")
          self.Password_Label.grid(row = 1, column = 0,pady = 10)
          self.Username_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14))
          self.Username_Entry.grid(row = 0, column = 1,pady =10)
          self.Password_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14) , show = "*") 
          self.Password_Entry.grid(row = 1, column = 1,pady = 10)
          self.username= self.Username_Entry.get()
          self.password = self.Password_Entry.get()
          self.ButtonLogin = Button(self.frame1, text = 'LogIn',borderwidth=8, width = 10, bg = "orange", font = ("Verdana", 12),command =lambda : self.Display_teacher_history_option(self.frame1))
          self.ButtonLogin.pack( pady =5, padx = 5)
     
     def Display_teacher_history_option(self,old_frame):
        self.old_frame = old_frame
        self.username= self.Username_Entry.get()
        self.password = self.Password_Entry.get()
        if self.username == "mine":
             if self.password == "1":
                self.old_frame.destroy()
                self.new_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
                self.new_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
                self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.new_frame,self.window))
                self.button_Home.place(x=5, y=5, anchor="nw")
                
                self.Photo_logo = PhotoImage(file="shared image (2).png")
                self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
                self.logo.pack(padx=5,pady=25)
        
                self.inner_frame = Frame(self.new_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
                self.inner_frame.pack (pady = 20,padx = 20) 
                self.Button_View_all_histrory = Button (self.inner_frame, text = "View all history", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 20 , command=lambda: self.Display_TopicList_view_all_history(self.new_frame))  
                self.Button_View_all_histrory.pack(pady = 5, padx = 5)
                self.Button_view_a_student_history= Button(self.inner_frame, text = "View a student history", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda: self.log_in_as_student_input(self.new_frame))
                self.Button_view_a_student_history.pack(pady = 5, padx = 5)
                self.Button_view_top_student = Button(self.inner_frame, text = "View Student AVG score", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda: self.Display_TopicList_AVG_student_score(self.new_frame))
                self.Button_view_top_student.pack(pady = 5, padx = 5)
             else:
               
                self.History_login_teacher(self.old_frame)
                self.show_info()

        else:
               
                self.History_login_teacher(self.old_frame)
                self.show_info()
     
     def Display_TopicList_view_all_history(self,old_frame):
        self.old_frame = old_frame
        
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,  self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves","All Topics"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)

        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda: self.order_type_view_all_history(self.outer_frame,self.listbox))
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)
     


     def order_type_view_all_history(self,old_frame,listbox):
        self.old_frame = old_frame
        
        self.old_frame = old_frame
        self.listbox = listbox      
        self.var = StringVar()
        self.var.set(None) 
        self.selected_indeces =  self.listbox.curselection()
        self.index = self.selected_indeces [0]
        self.value = self.listbox.get(self.index)
        self.topic_list = ["Energy", "Material", "Momentum", "Waves"]
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)  
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,  self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")  
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame = Frame(self.outer_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
        self.inner_frame.pack (pady = 20,padx = 20)
        self.Button_Date = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Date", variable= self.var, value ="Order by Date",padx = 5, pady= 5  )
        self.Button_Date.pack( padx= 20,pady= 5)
        self.Button_Total_mark = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Mark", variable= self.var, value ="Order by Mark",padx = 5, pady= 5  )
        self.Button_Total_mark.pack( padx= 20,pady= 5)    
         
        if self.value in self.topic_list:         
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_each_topic_teacher(self.outer_frame,self.value,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)
        if self.value == "All Topics" :
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_all_topic(self.outer_frame,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)

          

     def dispaly_history_each_topic_teacher(self,old_frame,selected_topic,order_type):  
          self.old_frame = old_frame
          self.order_type = order_type
          self.old_frame.destroy()
          self.order_type2 = self.order_type.get()
          self.order_type3 = ""
          if  self.order_type2 == "Order by Date":
                self.order_type3 = "Date"
          if self.order_type2 == "Order by Mark":
                self.order_type3 = "TotalMark"
         
          self.selected_toipc = selected_topic
          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE TopicName = ?  
                                               ORDER BY {self.order_type3 } """
          
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.selected_toipc ,))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
        
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)         
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side=RIGHT, fill= Y)
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)  
          self.tree.pack(side=LEFT,expand=True, fill='both')
         
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
         
          self.tree.heading("Name", text = "Name",anchor = "w")
          self.tree.column("Name",width=400,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=200,anchor = "w")

          self.tree.heading("Total mark", text = "Total mark",anchor = "w")
          self.tree.column("Total mark",width=300,anchor = "w")

          self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
          self.tree.column("Percentage mark",width=300,anchor = "w")

          self.tree.heading("Date", text = "Date",anchor = "w")
          self.tree.column("Date",width=300,anchor = "w")

          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.list_history.append(tuple[6])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")

     def dispaly_history_all_topic(self,old_frame,order_type):
          self.old_frame = old_frame
          self.order_type = order_type          
          self.order_type2 = self.order_type.get()
          self.order_type3 = ""
          if  self.order_type2 == "Order by Date":
                self.order_type3 = "Date"
          if self.order_type2 == "Order by Mark":
                self.order_type3 = "TotalMark"
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID 
                                            
                                               ORDER BY {self.order_type3 }
                                               """
          
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history)
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showinfo("Information", "No student as attempted this topic yet✅")
          if len(self.list_selected_topic_history2) > 0: 
                    self.old_frame.destroy()
                    self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
                  
                    self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
                    self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
                    self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
                    self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)         
                    self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
                    
                    
                    self.scroller_x_axis.pack(side="bottom", fill= X)
                    self.scroller_y_axis.pack(side=RIGHT, fill= Y)
                    self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
                    self.scroller_y_axis.config(command=self.tree.yview)
                    self.scroller_x_axis.config(command=self.tree.xview)  
                    self.tree.pack(side=LEFT,expand=True, fill='both')
                              
                    self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame,self.window))
                    self.button_Home.place(x=5, y=5, anchor="nw")
                    self.style = ttk.Style()
                    self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
                    self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
               
                    self.tree.heading("Name", text = "Name",anchor = "w")
                    self.tree.column("Name",width=300,anchor = "w")

                    self.tree.heading("Topic", text = "Topic",anchor = "w")
                    self.tree.column("Topic",width=200,anchor = "w")

                    self.tree.heading("Total mark", text = "Total mark",anchor = "w")
                    self.tree.column("Total mark",width=200,anchor = "w")

                    self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
                    self.tree.column("Percentage mark",width=200,anchor = "w")


                    self.tree.heading("Date", text = "Date",anchor = "w")
                    self.tree.column("Date",width=200,anchor = "w")

                    self.list_history = []
                    for tuple in self.list_selected_topic_history2:
                         
                         self.name = tuple[1] + " " + tuple[2]
                         self.list_history.append(self.name)
                         self.list_history.append(tuple[3])
                         self.list_history.append(tuple[4])
                         self.list_history.append(tuple[5])
                         self.list_history.append(tuple[6])
                         self.tree.insert("",END, values= self.list_history)
                         self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")
          

     
           
               


     def log_in_as_student_input(self,old_frame):
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.frame1 = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
          self.frame1.pack (pady = 29,padx = 100, fill=BOTH,expand=True)
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=25)
          self.Student_label = Label(self.frame1, text = "Enter students", font = ("verdana", 15), background = "orange")
          self.Student_label.pack(padx=5,pady= 0)
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame1,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.frame = Frame( self.frame1, borderwidth=10,width=0, height=0,bg ="DodgerBlue",pady = 10,padx = 10)  
          self.frame.pack (pady = 5,padx = 20)         

          self.FirstName_Label = Label(self.frame, text = "FIRST NAME", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.FirstName_Label.grid(row = 0, column = 0, pady = 10)
          self.Surname_Label = Label(self.frame, text = "SURNAME", font=("Verdana", 12),width = 12, pady = 10,bg = "orange")
          self.Surname_Label.grid(row = 1, column = 0,pady = 10)
          self.FirstName_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14))
          self.FirstName_Entry.grid(row = 0, column = 1,pady =10)
          self.Surname_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14) ) 
          self.Surname_Entry.grid(row = 1, column = 1,pady = 10)
          self.ButtonLogin = Button(self.frame1, text = 'Continue',borderwidth=8, width = 10, bg = "orange", font = ("Verdana", 12),command =lambda : self.Display_TopicList_view_all_history2(self.frame1,self.FirstName_Entry,self.Surname_Entry))
          self.ButtonLogin.pack( pady =5, padx = 5)


     def Display_TopicList_view_all_history2(self,old_frame,firstName,LastName):
        self.FirstName = firstName.get().lower()
        self.LastName = LastName.get().lower()
        self.old_frame = old_frame
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves","All Topics"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)

        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda: self.order_type_view_all_history2(self.outer_frame,self.listbox,self.FirstName,self.LastName))
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)
     

     


     def order_type_view_all_history2(self,old_frame,listbox,firstName,Surname):
        self.FirstName = firstName
        self.SurName = Surname
        print(self.FirstName, self.SurName)
        self.old_frame = old_frame
        
        self.old_frame = old_frame
        self.listbox = listbox      
        self.var = StringVar()
        self.var.set(None) 
        self.selected_indeces =  self.listbox.curselection()
        self.index = self.selected_indeces [0]
        self.value = self.listbox.get(self.index)
        self.topic_list = ["Energy", "Material", "Momentum", "Waves"]
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)   
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw") 
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame = Frame(self.outer_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
        self.inner_frame.pack (pady = 20,padx = 20)
        self.Button_Date = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Date", variable= self.var, value ="Order by Date",padx = 5, pady= 5  )
        self.Button_Date.pack( padx= 20,pady= 5)
        self.Button_Total_mark = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Mark", variable= self.var, value ="Order by Mark",padx = 5, pady= 5  )
        self.Button_Total_mark.pack( padx= 20,pady= 5)    
       # self.selected_indeces = self.listbox.curselection()
       # self.index = self.selected_indeces [0]
       # self.value = self.listbox.get(self.index)  
        if self.value in self.topic_list:         
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_each_topic_student(self.outer_frame,self.FirstName, self.SurName,self.value,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)
        if self.value == "All Topics" :
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_all_topic_student(self.outer_frame,self.FirstName, self.SurName,self.value,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)



     def dispaly_history_each_topic_student (self,old_frame,first_name,surname,topic,order_type):
          self.FirstName = first_name
          self.SurName = surname
          self.order = order_type.get()
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.order3 = ""
          if  self.order == "Order by Date":
                self.order3 = "Date"
          if self.order == "Order by Mark":
                self.order3 = "TotalMark"
         
         
          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE TopicName = ? AND  LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               ORDER BY {self.order3 } """
          print( self.str_selected_topic_history)
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.selected_toipc, self.FirstName, self.SurName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)         
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          
          
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side=RIGHT, fill= Y)
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)  
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
          
          self.tree.heading("Name", text = "Name",anchor = "w")
          self.tree.column("Name",width=300,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=200,anchor = "w")

          self.tree.heading("Total mark", text = "Total mark",anchor = "w")
          self.tree.column("Total mark",width=200,anchor = "w")

          self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
          self.tree.column("Percentage mark",width=200,anchor = "w")

          self.tree.heading("Date", text = "Date",anchor = "w")
          self.tree.column("Date",width=200,anchor = "w")

          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.list_history.append(tuple[6])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")

     def dispaly_history_all_topic_student (self,old_frame,first_name,surname,topic,order_type):
          self.FirstName = first_name
          self.SurName = surname
          self.order = order_type.get()
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.order3 = ""
          if  self.order == "Order by Date":
                self.order3 = "Date"
          if self.order == "Order by Mark":
                self.order3 = "TotalMark"
         
         
          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE  LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               ORDER BY {self.order3 } """
          print( self.str_selected_topic_history)
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, ( self.FirstName, self.SurName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview( self.frame, columns=self.columns, show='headings',height= 10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)
          
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          
         
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side=RIGHT, fill= Y)
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)
          self.tree.pack(side=LEFT,expand=True, fill='both')
         
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
          
          self.tree.heading("Name", text = "Name",anchor = "w")
          self.tree.column("Name",width=300,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=200,anchor = "w")

          self.tree.heading("Total mark", text = "Total mark",anchor = "w")
          self.tree.column("Total mark",width=200,anchor = "w")

          self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
          self.tree.column("Percentage mark",width=200,anchor = "w")

          self.tree.heading("Date", text = "Date",anchor = "w")
          self.tree.column("Date",width=200,anchor = "w")

          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.list_history.append(tuple[6])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")
          
          
     def Display_TopicList_AVG_student_score(self,old_frame):
        self.old_frame = old_frame
        
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,  self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves","All Topics"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)

        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda: self.student_topic_AVG_checker(self.listbox,self.outer_frame))
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)


     def student_topic_AVG_checker(self,topic,old_frame ):
          self.old_frame = old_frame
          self.topic = topic
          self.selected_indeces =  self.topic.curselection()
          self.index = self.selected_indeces [0]
          self.value = self.listbox.get(self.index)
          self.topic_list = ["Energy", "Material", "Momentum", "Waves"]
          if self.value in self.topic_list:
               self.display_AVG_each_topic_student(self.old_frame,self.value)
          if self.value == "All Topics" :
                self.display_AVG_all_topic_student(self.old_frame,self.value)
               
          



     
     
    


     def display_AVG_each_topic_student (self,old_frame,topic):
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()

          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, ROUND(AVG(TotalMark), 1) AS average_mark, SUM(CASE WHEN TopicName = '{self.str_selected_topic}' THEN 1 ELSE 0 END) AS {self.selected_toipc}
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE TopicName = ?
                                               GROUP BY StudentFurname, StudentSurname,TopicName
                                               ORDER BY average_mark DESC """
          
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.str_selected_topic,))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
         

          self.columns = ("Student Name", "Topic", "Average score","Attempted_times")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height=10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side="right", fill= Y)
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
         
          self.tree.heading("Student Name", text = "Student Name",anchor = "w")
          self.tree.column("Student Name",width=5,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=5,anchor = "w")

          self.tree.heading("Average score", text = "Average score",anchor = "w")
          self.tree.column("Average score",width=5,anchor = "w")

          self.tree.heading("Attempted_times", text = "Attempted_times",anchor = "w")
          self.tree.column("Attempted_times",width=5,anchor = "w")

         
          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showinfo("Information", "No student as attempted this topic yet✅")


     def display_AVG_all_topic_student (self,old_frame,topic):
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()

          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, ROUND(AVG(TotalMark), 1) AS average_mark, SUM(CASE WHEN TopicName = TopicName  THEN 1 ELSE 0 END) AS TopicName
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               
                                               GROUP BY StudentFurname, StudentSurname, TopicName
                                               ORDER BY average_mark DESC """
        
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history,)
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
        

          self.columns = ("Student Name", "Topic", "Average score","Attempted_times")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height=10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side="right", fill= Y)
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
         
          self.tree.heading("Student Name", text = "Student Name",anchor = "w")
          self.tree.column("Student Name",width=5,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=5,anchor = "w")

          self.tree.heading("Average score", text = "Average score",anchor = "w")
          self.tree.column("Average score",width=5,anchor = "w")

          self.tree.heading("Attempted_times", text = "Attempted_times",anchor = "w")
          self.tree.column("Attempted_times",width=5,anchor = "w")

         
          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")

             



     def history_log_in_as_student(self,old_frame):
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.frame1 = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 10) 
          self.frame1.pack (pady = 29,padx = 100, fill=BOTH,expand=True)
          self.Photo_logo = PhotoImage(file="shared image (2).png")
          self.logo = Label(self.frame1,image= self.Photo_logo,bg ="deep sky blue")
          self.logo.pack(padx=5,pady=25)
          self.Student_label = Label(self.frame1, text = "Enter students", font = ("verdana", 15), background = "orange")
          self.Student_label.pack(padx=5,pady= 0)
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.frame1,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.frame = Frame( self.frame1, borderwidth=10,width=0, height=0,bg ="DodgerBlue",pady = 10,padx = 10)  
          self.frame.pack (pady = 5,padx = 20)         

          self.FirstName_Label = Label(self.frame, text = "FIRST NAME", font=("Verdana", 12),width = 12, pady = 10, bg = "orange")
          self.FirstName_Label.grid(row = 0, column = 0, pady = 10)
          self.Surname_Label = Label(self.frame, text = "SURNAME", font=("Verdana", 12),width = 12, pady = 10,bg = "orange")
          self.Surname_Label.grid(row = 1, column = 0,pady = 10)
          self.FirstName_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14))
          self.FirstName_Entry.grid(row = 0, column = 1,pady =10)
          self.Surname_Entry = Entry(self.frame,borderwidth=8,font=("Verdana", 14) ) 
          self.Surname_Entry.grid(row = 1, column = 1,pady = 10)
          self.ButtonLogin = Button(self.frame1, text = 'Continue',borderwidth=8, width = 10, bg = "orange", font = ("Verdana", 12),command =lambda : self.Display_student_history_option(self.frame1,self.FirstName_Entry,self.Surname_Entry))
          self.ButtonLogin.pack( pady =5, padx = 5)

     
     def Display_student_history_option(self,old_frame,first_name, last_name):
                self.FirstName = first_name.get().lower()
                self.SurName = last_name.get().lower()
                self.old_frame = old_frame
                self.old_frame.destroy()
                self.new_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
                self.new_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True) 
                self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.new_frame,self.window))
                self.button_Home.place(x=5, y=5, anchor="nw")
                
                self.Photo_logo = PhotoImage(file="shared image (2).png")
                self.logo = Label(self.new_frame,image= self.Photo_logo,bg ="deep sky blue")
                self.logo.pack(padx=5,pady=25)
        
                self.inner_frame = Frame(self.new_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
                self.inner_frame.pack (pady = 20,padx = 20) 
                self.Button_View_all_history = Button (self.inner_frame, text = "View all history", borderwidth=8,bg = "orange",font = ("Verdana", 12),width = 20 , command=lambda:self.TopicList_view_student_history(self.new_frame,self.FirstName,self.SurName))  
                self.Button_View_all_history.pack(pady = 5, padx = 5)
                self.Button_view_a_student_history= Button(self.inner_frame, text = "View average score", borderwidth = 8 , bg = "orange", font = ("Verdana", 12), width = 20,command=lambda: self.TopicList_AVG_each_student_score(self.new_frame,self.FirstName,self.SurName))
                self.Button_view_a_student_history.pack(pady = 5, padx = 5)


     def TopicList_view_student_history(self,old_frame,first_Name,Last_Name):
        self.FirstName = first_Name
        self.LastName = Last_Name
        self.Old_frame = old_frame
        self.Old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves","All Topics"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)

        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda: self.order_type_view_a_student_history(self.outer_frame,self.listbox,self.FirstName,self.LastName))
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)


     
     


     def dispaly_history_each_topic_for_each_student (self,old_frame,first_name,surname,topic,order_type):
          self.FirstName = first_name
          self.SurName = surname
          self.order = order_type.get()
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.order3 = ""
          if  self.order == "Order by Date":
                self.order3 = "Date"
          if self.order == "Order by Mark":
                self.order3 = "TotalMark"
         
         
          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE TopicName = ? AND  LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               ORDER BY {self.order3 } """
          print( self.str_selected_topic_history)
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.selected_toipc, self.FirstName, self.SurName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)         
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          
          
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side=RIGHT, fill= Y)
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)  
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
          
          self.tree.heading("Name", text = "Name",anchor = "w")
          self.tree.column("Name",width=300,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=200,anchor = "w")

          self.tree.heading("Total mark", text = "Total mark",anchor = "w")
          self.tree.column("Total mark",width=200,anchor = "w")

          self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
          self.tree.column("Percentage mark",width=200,anchor = "w")

          self.tree.heading("Date", text = "Date",anchor = "w")
          self.tree.column("Date",width=200,anchor = "w")

          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.list_history.append(tuple[6])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "This student as not attempted this topic yet✅")


     def order_type_view_a_student_history(self,old_frame,listbox,firstName,Surname):
        self.FirstName = firstName
        self.SurName = Surname
        print(self.FirstName, self.SurName)
        self.old_frame = old_frame
        
        self.old_frame = old_frame
        self.listbox = listbox      
        self.var = StringVar()
        self.var.set(None) 
        self.selected_indeces =  self.listbox.curselection()
        self.index = self.selected_indeces [0]
        self.value = self.listbox.get(self.index)
        self.topic_list = ["Energy", "Material", "Momentum", "Waves"]
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)   
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw") 
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame = Frame(self.outer_frame,borderwidth=10,width=300, height=300,bg ="DodgerBlue",pady = 10,padx = 10 )
        self.inner_frame.pack (pady = 20,padx = 20)
        self.Button_Date = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Date", variable= self.var, value ="Order by Date",padx = 5, pady= 5  )
        self.Button_Date.pack( padx= 20,pady= 5)
        self.Button_Total_mark = Radiobutton(self.inner_frame,width= 35,bd=10,bg = "orange",cursor = "target",font = ("Verdana", 12), text="Order by Mark", variable= self.var, value ="Order by Mark",padx = 5, pady= 5  )
        self.Button_Total_mark.pack( padx= 20,pady= 5)    
       # self.selected_indeces = self.listbox.curselection()
       # self.index = self.selected_indeces [0]
       # self.value = self.listbox.get(self.index)  
        if self.value in self.topic_list:         
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_each_topic_for_each_student(self.outer_frame,self.FirstName, self.SurName,self.value,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)
        if self.value == "All Topics" :
               self.Button_Continue = Button(self.outer_frame, text = "Continue", font = ("verdana", 12), bg = "orange", width = 12, command = lambda: self.dispaly_history_all_topic_for_each_student(self.outer_frame,self.FirstName, self.SurName,self.var))
               self.Button_Continue.pack( padx=5,pady= 5)


     def dispaly_history_all_topic_for_each_student (self,old_frame,first_name,surname,order_type):
          self.FirstName = first_name
          self.SurName = surname
          self.order = order_type.get()
         
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.order3 = ""
          if  self.order == "Order by Date":
                self.order3 = "Date"
          if self.order == "Order by Mark":
                self.order3 = "TotalMark"
         
         
         
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, TotalMark, PercentageMark, Date
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               ORDER BY {self.order3 } """
          print( self.str_selected_topic_history)
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.FirstName, self.SurName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Name", "Topic", "Total mark", "Percentage mark", "Date")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height= 10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange", )
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree)         
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          
          
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side=RIGHT, fill= Y)
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)  
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
          
          self.tree.heading("Name", text = "Name",anchor = "w")
          self.tree.column("Name",width=300,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=200,anchor = "w")

          self.tree.heading("Total mark", text = "Total mark",anchor = "w")
          self.tree.column("Total mark",width=200,anchor = "w")

          self.tree.heading("Percentage mark", text = "Percentage mark",anchor = "w")
          self.tree.column("Percentage mark",width=200,anchor = "w")

          self.tree.heading("Date", text = "Date",anchor = "w")
          self.tree.column("Date",width=200,anchor = "w")

          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.list_history.append(tuple[6])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "This student as not attempted this topic yet✅")


     def TopicList_AVG_each_student_score(self,old_frame,first_name,last_name):
        self.FirstName= first_name
        self.LastName = last_name
        self.old_frame = old_frame
        self.old_frame.destroy()
        self.outer_frame = Frame(self.window, border=0,width=300, height=300,bg ="deep sky blue",padx = 10, pady = 10) 
        self.outer_frame.pack (pady = 10,padx = 200, fill=BOTH, expand= True)
        self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self,  self.outer_frame,self.window))
        self.button_Home.place(x=5, y=5, anchor="nw")
        self.Photo_logo = PhotoImage(file="shared image (2).png")
        self.logo = Label(self.outer_frame,image= self.Photo_logo,bg ="deep sky blue")
        self.logo.pack(padx=5,pady=25)
        self.inner_frame2 =  Frame(self.outer_frame, borderwidth=10,width=300, height= 300,bg ="DodgerBlue",pady = 10,padx = 10)
        self.inner_frame2.pack(pady = 20,padx = 20)
        self.List_of_Topics = ["Energy", "Material", "Momentum", "Waves","All Topics"]
        self.listbox = Listbox(self.inner_frame2, height= 5)  
        self.topic_label = Label(self.inner_frame2, text = "Select a Topic You would Like To Update.", font = ("verdana", 9), background = "orange")
        self.topic_label.grid(row = 0, column= 0,padx=5,pady= 5)
        for Words in self.List_of_Topics:
            self.listbox.insert(END, Words)
        self.listbox.grid(row = 1 ,column= 0, padx=5,pady= 5)

        self.Button_Enter = Button(self.inner_frame2, text = "Enter", font = ("verdana", 12), bg = "orange", width = 6, command = lambda: self.student_topic_AVG_checks_each_student(self.listbox,self.outer_frame, self.FirstName, self.LastName))
        self.Button_Enter.grid(row = 2, column= 0, padx=5,pady= 5)


     
     def student_topic_AVG_checks_each_student(self,topic,old_frame,first_name,last_name):
          self.FirstName= first_name
          self.LastName = last_name
          self.old_frame = old_frame
          self.topic = topic
          self.selected_indeces =  self.topic.curselection()
          self.index = self.selected_indeces [0]
          self.value = self.listbox.get(self.index)
          self.topic_list = ["Energy", "Material", "Momentum", "Waves"]
          if self.value in self.topic_list:
               self.display_AVG_each_topic_student2(self.old_frame,self.value,self.FirstName,self.LastName)
          if self.value == "All Topics" :
                self.display_AVG_all_topic_student2(self.old_frame,self.FirstName,self.LastName)


     def display_AVG_each_topic_student2 (self,old_frame,topic,first_name,surname):
          self.FirstName = first_name
          self.LastName = surname
          self.selected_toipc = topic
          self.old_frame = old_frame
          self.old_frame.destroy()
          self.str_selected_topic = str(self.selected_toipc)
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, ROUND(AVG(TotalMark), 1) AS average_mark, SUM(CASE WHEN TopicName = '{self.str_selected_topic}' THEN 1 ELSE 0 END) AS {self.selected_toipc}
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE TopicName = ? AND LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               GROUP BY StudentFurname, StudentSurname,TopicName
                                               ORDER BY average_mark DESC """
          print( self.str_selected_topic_history)
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.str_selected_topic,  self.FirstName, self.LastName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
          print(self.list_selected_topic_history2)

          self.columns = ("Student Name", "Topic", "Average score","Attempted_times")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height=10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side="right", fill= Y)
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
         
          self.tree.heading("Student Name", text = "Student Name",anchor = "w")
          self.tree.column("Student Name",width=5,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=5,anchor = "w")

          self.tree.heading("Average score", text = "Average score",anchor = "w")
          self.tree.column("Average score",width=5,anchor = "w")

          self.tree.heading("Attempted_times", text = "Attempted_times",anchor = "w")
          self.tree.column("Attempted_times",width=5,anchor = "w")

         
          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")


     def display_AVG_all_topic_student2 (self,old_frame,first_name,surname):
          self.FirstName = first_name
          self.LastName = surname
          
          self.old_frame = old_frame
          self.old_frame.destroy()
         
          conn = sqlite3.connect('Table.db')
          self.str_selected_topic_history = f"""SELECT History.StudentID, StudentFurname, StudentSurname, TopicName, ROUND(AVG(TotalMark), 1) AS average_mark, SUM(CASE WHEN TopicName = TopicName THEN 1 ELSE 0 END) AS TopicName
                                               FROM History                       
                                               JOIN Student ON  Student.StudentID = History.StudentID
                                               WHERE LOWER(StudentFurname) = ? AND  LOWER(StudentSurname) = ?
                                               GROUP BY StudentFurname, StudentSurname,TopicName
                                               ORDER BY average_mark DESC """
         
          self.list_selected_topic_history = conn.execute(self.str_selected_topic_history, (self.FirstName, self.LastName))
          self.list_selected_topic_history2 = self.list_selected_topic_history.fetchall()
       

          self.columns = ("Student Name", "Topic", "Average score","Attempted_times")
          self.frame = Frame(self.window, border=0,width=10, height=8,bg ="deep sky blue",padx = 10, pady = 20) 
          self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',height=10)
          self.scroller_x_axis = Scrollbar(self.frame, orient= HORIZONTAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_y_axis = Scrollbar(self.frame, orient= VERTICAL, command=self.tree,bg="orange",activebackground = "orange",troughcolor = "orange")
          self.scroller_x_axis.pack(side="bottom", fill= X)
          self.scroller_y_axis.pack(side="right", fill= Y)
          self.tree.configure(xscrollcommand=self.scroller_y_axis.set, yscrollcommand=self.scroller_y_axis.set )
          self.frame.pack (pady = 40,padx = 10, fill=BOTH,expand=True)
          self.scroller_y_axis.config(command=self.tree.yview)
          self.scroller_x_axis.config(command=self.tree.xview)
          self.tree.pack(side=LEFT,expand=True, fill='both')
          self.button_Home = Button(self.window,text="🏠 Home",font=("Arial", 9),bg = "orange",command=lambda: Display.Home(self, self.frame,self.window))
          self.button_Home.place(x=5, y=5, anchor="nw")
          self.style = ttk.Style()
          self.style.configure("Treeview",rowheight = 40,font = ("verdana", 13),background ="orange",fieldbackground="orange", foreground="blue")
          self.style.configure("Treeview.Heading",font=("verdana", 15,"bold"))
          
         
          self.tree.heading("Student Name", text = "Student Name",anchor = "w")
          self.tree.column("Student Name",width=5,anchor = "w")

          self.tree.heading("Topic", text = "Topic",anchor = "w")
          self.tree.column("Topic",width=5,anchor = "w")

          self.tree.heading("Average score", text = "Average score",anchor = "w")
          self.tree.column("Average score",width=5,anchor = "w")

          self.tree.heading("Attempted_times", text = "Attempted_times",anchor = "w")
          self.tree.column("Attempted_times",width=5,anchor = "w")

         
          self.list_history = []
          for tuple in self.list_selected_topic_history2:
               
               self.name = tuple[1] + " " + tuple[2]
               self.list_history.append(self.name)
               self.list_history.append(tuple[3])
               self.list_history.append(tuple[4])
               self.list_history.append(tuple[5])
               self.tree.insert("",END, values= self.list_history)
               self.list_history = []
          if len(self.list_selected_topic_history2) == 0:
                     messagebox.showwarning("Information", "No student as attempted this topic yet✅")
               
               
          




                
           
          
def classes (): 
    app = Display()
   
if __name__== "__main__":
    classes()


                 


                

                 








