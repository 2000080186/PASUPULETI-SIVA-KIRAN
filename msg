class subClass{
String msg="Hello";
String name;
void disp(String myname){
name=myname;
System.out.println(msg+name);
}
}
class Msg{
public static void main(String args[]){
subClass sc1=new subClass();
subClass sc2=new subClass();
subClass sc3=new subClass();
sc1.disp("Siva");
sc2.disp("kiran");
sc3.disp("pasupuleti");
System.out.println(sc1.name+','+sc2.name+','+sc3.name);
}
}
