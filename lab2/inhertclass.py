class Person:
    def __init__(self,name,money,mood,healthRate):
        self.__name=name;
        self.__money=money;
        self.__mood=mood;
        self.healthRate=healthRate;
    def set_name(self, name):
        self.__name=name
    def set_money(self,money):
        self.__money=employes
    def set_mood(self,mood):
        self.__mood=mood
    def set_healthRate(self,healthRate):
        self.__healthRate=healthRate
    def get_name(self):
        return self.__name

    def get_monay(self):
        return self.__money
    def get_mood(self):
        return self.__mood
    def get_healthRate(self):
        return self.__healthRate

    def sleep(hours):
        if hours == 7:
            print("happy" )
        if hours < 7:
            print("tired")
        if hours >7:
            print("lazy")

    def eat(self,maels):
         if(maels==3):
             return "%100 health"
         if(maels<3):
             return "%75 health"
         return "%50 health"

    def work(self,hour):
        if(hour==8):
            return "happy"
        if(hour>8):
            return "tired"
        return "lazy"

    def healthRate(self,healthRate):
        if(healthRate<0):
            self.healthRate=0
        elif(healthRate>100):
            self.healthRate=100
        else:
            self.healthRate=healthRate


    def buy(self,items):
        if(items==1):
            money=money*0.1
            return money
class Employee(Person):
    def __init__(self,id,name,car,email,salary,distanceTowork,time):
        person.__init__(self,name,money,mood,healthRate);
        self.id=id;
        self.__car=car
        self.__name=name
        self.__email=email
        self.__salary=salary
        self.__distanceTowork=distanceTowork
        self.__time=time

    def salary(self,salary):
        if(salry<1000):
            self.salry=1000


    def work(hours,mood):
        mood('happy','tired','lazy')
        if hours == 7:
            print(mood[0])
        if hours < 7:
            print(mood[1])
        if hours >7:
            print(mood[2])
    def drive(self,distanceTowork,time):
        dis=self.distanceTowork
        time=self.time
        f=car(__car)
        velocity=dis/time;
        print("velocity"+velocity)

    def refuse(self):
            print("my name is"+self.name);


class office():
    def __init__(self, name,employes):
        super(office, self).__init__()
        self.__name =name
        self.__employes=employes
    def set_name(self, name):
         self.__name=name
    def set_employes(self,employes):
         self.__employes=employes
    def get_name(self):
         return self.__name

    def get_employes(self):
         return self.__employess


class car():
    def __init__(self,name,fuelRate, velocity):
        self.__name=name
        self.__fuelRate=fuelRate
        self.__velocity=velocitys

    def set_name(self, name):
        self.__name=name
    def set_fuelRate(self,fuelRate):
        self.__fuelRate=fualRate
    def set_velocity(self,velovity):
        self.__velocity=velocity

    def get_name(self):
        return self.__name

    def get_fuelRate(self):
        return self.__fuelRate

    def get_velocity(self):
        return self.__velocity





emp=Employee(1,'eh','lanser','eh@gmail.com',333333,777,555)
y=emp.drive();
print(y)
p=person("et",88,'helt','cool')
print(p)
print(p.sleep(4))
print(p.eat(55))
print(p.sleep(44))
print(p.healthRate(33))
